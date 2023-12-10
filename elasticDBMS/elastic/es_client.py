from elasticsearch import Elasticsearch


"""
Data modelling and engineering for the movement of data between:
1. Sites
2. Services
3. Reporting
4. Users

We've chosen the ELK Stack OSS for visibility
"""


client = Elasticsearch(
    "https://...",  # Elasticsearch endpoint
    api_key=("api-key-id", "api-key-secret"),  # API key ID and secret
)
