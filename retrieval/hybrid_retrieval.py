"""Hybrid retrieval combining vector and structured methods."""

class HybridRetrieval:
    def __init__(self, vector_retrieval, structured_retrieval):
        self.vector = vector_retrieval
        self.structured = structured_retrieval

    def retrieve(self, query):
        return self.vector.retrieve(query) + self.structured.retrieve(query)
