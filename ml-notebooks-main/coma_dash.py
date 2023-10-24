"""CoMa - Interactive Confusion Matrix
This is a small utility app to visually investigate data points
contributing to TP, FP, TN, and FN.
"""

import argparse
import os

import dash
import pandas as pd
import plotly.figure_factory as ff

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

app = Dash(__name__)

TITLE = "## " + __doc__

HOW_TO = """
### How to use this app?
 - Select any one cell from the confusion matrix.
 - This will populate the 'Filtered Keys' drop-down to ids
  corresponding to clicked cell in confusion matrix.
 - Choose one key from the down to view the raw text.
"""


def plot_confusion_matrix(y_true, y_pred):
    """Plots Confusion Matrix and returns figure"""
    z = confusion_matrix(y_true, y_pred)
    labels = list(unique_labels(y_true, y_pred))
    z_text = [[str(y) for y in x] for x in z]

    fig = ff.create_annotated_heatmap(
        z, x=labels, y=labels, annotation_text=z_text, colorscale="Viridis"
    )

    fig["layout"]["yaxis"]["autorange"] = "reversed"

    fig.update_layout(
        xaxis=dict(title="Predicted label"), yaxis=dict(title="True label")
    )

    fig["data"][0]["showscale"] = True
    return fig


@app.callback(
    Output("dropdown-label", "children"), Input("confusion-matrix", "clickData")
)
def click(clickData):
    if not clickData:
        raise dash.exceptions.PreventUpdate
    coo = {k: clickData["points"][0][k] for k in ["x", "y"]}
    _df = df.loc[(df["y_true"] == coo["y"]) & (df["y_pred"] == coo["x"])]
    return f"Filtered IDs: {len(_df)}"


@app.callback(
    Output("dropdown", "options"),
    Input("confusion-matrix", "clickData"),
)
def click(clickData):
    if not clickData:
        raise dash.exceptions.PreventUpdate
    coo = {k: clickData["points"][0][k] for k in ["x", "y"]}
    _df = df.loc[(df["y_true"] == coo["y"]) & (df["y_pred"] == coo["x"])]
    return [{"label": i, "value": i} for i in _df.id.unique()]


@app.callback(Output("text", "children"), Input("dropdown", "value"))
def load_text_in_view(value):
    if value is not None:
        return df.loc[df["id"] == value]["text"].tolist()[0]


def get_layout(df, cm_fig):
    return html.Div(
        [
            html.Div(
                [
                    dcc.Markdown(TITLE),
                    dcc.Markdown(HOW_TO),
                ],
                style={"background-color": "#e9ede4"},
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id="confusion-matrix", figure=cm_fig),
                        ],
                        style={"display": "inline-block"},
                    ),
                    html.Div(
                        [
                            html.Label(
                                id="dropdown-label",
                                children=["Filtered IDs: 0"],
                                style={"font-weight": "bold", "text-align": "center"},
                            ),
                            dcc.Dropdown(
                                id="dropdown",
                                options=[
                                    {"label": i, "value": i} for i in df[:0].id.unique()
                                ],
                            ),
                            dcc.Markdown(id="text", children=[""]),
                        ],
                        style={
                            "display": "inline-block",
                            "width": "100%",
                            "height": "100vh",
                            "overflow": "scroll",
                        },
                    ),
                ],
                style={"display": "flex", "width": "100%"},
            ),
        ]
    )


def show_coma(df):
    y_true, y_pred = df["y_true"].values, df["y_pred"].values
    cm_fig = plot_confusion_matrix(y_true, y_pred)
    return cm_fig


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--path",
    "-p",
    required=True,
    help="Path to input file. Input file must contain "
    "at least four columns `id`, `text`, `y_true`, `y_pred`.",
)

args = parser.parse_args()

if not os.path.isfile(args.path):
    raise FileNotFoundError(f"File not found at path: {args.path}")
else:
    df = pd.read_csv(args.path)

if len(set(df.columns) & (set(["id", "text", "y_true", "y_pred"]))) != 3:
    raise ValueError(
        "Missing one or more of required columns: `id`, `text`, `y_true`, `y_pred`"
    )

cm_fig = show_coma(df)
app.layout = get_layout(df, cm_fig)
app.run_server(debug=True)
