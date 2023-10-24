from google.cloud.bigquery import Client
from google.oauth2 import service_account

KEY_PATH = "../../ashwani-0908-key.json"

class MyClient(Client):
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
            KEY_PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"],)
        super().__init__(credentials=self.credentials, project=self.credentials.project_id)

