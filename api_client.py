from openai import OpenAI
from config import API_KEY, logging


class APIClient:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY)
        self.conversation_thread = None

    def create_thread(self):
        self.conversation_thread = self.client.beta.threads.create()
        logging.info(f"Created new conversation thread: {self.conversation_thread.id}")

    def add_message(self, content):
        if not self.conversation_thread:
            self.create_thread()

        message = self.client.beta.threads.messages.create(
            thread_id=self.conversation_thread.id,
            role="user",
            content=content
        )
        logging.info(f"Added message to conversation: {message.id}")

    def run_conversation(self, assistant_id):
        run = self.client.beta.threads.runs.create(
            thread_id=self.conversation_thread.id,
            assistant_id=assistant_id
        )
        return run.id

    def get_run_status(self, run_id):
        return self.client.beta.threads.runs.retrieve(
            thread_id=self.conversation_thread.id,
            run_id=run_id
        )

    def get_messages(self):
        return self.client.beta.threads.messages.list(thread_id=self.conversation_thread.id)

    def upload_file(self, file_path):
        try:
            with open(file_path, "rb") as file:
                response = self.client.files.create(file=file, purpose="assistants")
            logging.info(f"File uploaded: {response.id}")
            return response.id
        except Exception as e:
            logging.error(f"Error uploading file: {e}")
            return None
