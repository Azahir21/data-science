How does Embedding Layer work?
------------------------------
Embeddings are learned by adding a dense layer to our network that is much smaller than the width of our one hot encoding and the network learns weights to translate from the one hot encoding to a dense floating point representation that captures meaning. The nueral network is trained on an auxiliary task, like predict each word of a sentence given last 4 words, to learn the symantic/syntatic similarity of words.\
\
`Embedding` layer in Keras doesn't learn any embeddings then. Instead, it acts like a lookup table which finds the continuous representation of one-hot encoded vectors from an already pre-trained embedding matrix (?).

See also:
 - [Deep Learning, NLP, and Representations on Colah's blog](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)
 - [RNN W2L05 : Learning word embeddings by Andrew Ng on Youtube](https://www.youtube.com/watch?v=xtPXjvwCt64)
 - [How does Keras 'Embedding' layer work? on Stackoverflow](https://stats.stackexchange.com/a/305032)
 - [How does Embedding Layer work? Issue #3110 on Keras' Github](https://github.com/keras-team/keras/issues/3110#issuecomment-345153450)


Why is f-score geometric mean of Precision & Recall and not arithmetic mean?
----------------------------------------------------------------------------
 - Geometric mean penalises the extreme values more than arithmetic mean. Consider an example where model always returns class A, there are infinite number of class B elements and only one class A element. Therefore, the `Precision = 0.0` and `Recall = 1.0`. The values of A.M. and G.M. in this case would be `0.5` and `0.0` respectively.
 - Theoritically, A.M. would only make sense when comparing metrics with same base i.e. same context in denominator. The denominator of both Precision and Recall is different, while the numerator of both metrics is `TP`.


What are Micro- & Macro- averages in classification problems?
-------------------------------------------------------------
Let's take an example of Precision
 - Micro-average computes global precision of the model by taking proportion of true positives vs true and false positives
$MicroPrecision = \frac{(TP_{1} + TP_{2} + ... + TP_{n})}{(TP_{1} + TP_{2} + ... + TP_{n}) + (FP_{1} + FP_{2} + ... + FP_{n})}$
 - Macro-average treats each class as equal and simply takes an average of individual precision scores.
$MacroPrecision = \frac{Prec_{1} + Prec_{2} + ... + Prec_{n}}{n}$
 - Weighted-Macro average takes the support (number of samples) of each class in consideration and then computes weighted average.

In general, if you are working with an imbalanced dataset where all classes are equally important, using the  **macro** average would be a good choice as it treats all classes equally. 

If you have an imbalanced dataset but want to assign greater contribution to classes with more samples in the dataset, then the **weighted** average is preferred. This is because, in weighted averaging, the contribution of each class to the F1 average is weighted by its size.

Suppose you have a balanced dataset and want an easily understandable metric for overall performance regardless of the class. In that case, you can go with accuracy, which is essentially our  **micro**  F1 score.

Read also:
 - [Micro, Macro & Weighted Averages of F1 Score, Clearly Explained](https://towardsdatascience.com/micro-macro-weighted-averages-of-f1-score-clearly-explained-b603420b292f)


