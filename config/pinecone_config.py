import os

class PineconeConfig:
    def __init__(self):
        self.api_key = os.getenv("PINECONE_API_KEY", "your-pinecone-api-key")
        self.environment = os.getenv("PINECONE_ENV", "us-west1-gcp")  # Set your Pinecone environment, e.g., 'us-west1-gcp'

    def get_api_key(self):
        return self.api_key

    def get_environment(self):
        return self.environment

# Usage:
# You can import this class and use its methods wherever you need the Pinecone configuration in your project.
# Example:
# from config.pinecone_config import PineconeConfig
# pinecone_config = PineconeConfig()
# print(pinecone_config.get_api_key())
