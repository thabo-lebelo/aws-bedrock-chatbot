"""
Amazon Bedrock client.
"""

import boto3
import json

from .config import AWS_REGION
from .config import MODEL_ID


def create_client():
    """
    Create and return a Bedrock Runtime client.
    """

    return boto3.client(
        service_name="bedrock-runtime",
        region_name=AWS_REGION
    )


def invoke_model(prompt: str) -> str:
    """
    Send a prompt to Amazon Bedrock using the Converse API.
    """

    client = create_client()

    try:
        response = client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 512,
                "temperature": 0.5
            }
        )

        return response["output"]["message"]["content"][0]["text"]

    except ClientError as e:
        raise RuntimeError(
            f"Failed to invoke model: {e.response['Error']['Message']}"
        ) from e