from pinecone import Pinecone, ServerlessSpec

class EmbeddingHelper:
    def __init__(self, api_key, environment):
        # Initialize Pinecone instance
        self.pinecone = Pinecone(api_key=api_key)
        self.environment = environment
        self.index_name = 'my-index'  # Valid index name (lowercase, alphanumeric, hyphens allowed)
        self._create_index()

    def _create_index(self):
        # Create the index if it doesn't exist already
        if self.index_name not in self.pinecone.list_indexes().names():
            self.pinecone.create_index(
                name=self.index_name,
                dimension=1536,  # Adjust dimension according to your embeddings
                metric='euclidean',
                spec=ServerlessSpec(
                    cloud='aws',  # Adjust cloud provider if necessary
                    region='us-east-1'  # Specify the region
                )
            )
            print(f"Index '{self.index_name}' created.")
        else:
            print(f"Index '{self.index_name}' already exists.")
