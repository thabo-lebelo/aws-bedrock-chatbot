"""
Amazon Bedrock client.
"""

import boto3

from .config import AWS_REGION


def create_client():
    """
    Create and return a Bedrock Runtime client.
    """

    return boto3.client(
        service_name="bedrock-runtime",
        region_name=AWS_REGION
    )