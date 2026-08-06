import boto3

from typing import List
from src.config import AWS_REGION, MODEL_ID


class BedrockClient:
    """
    Wrapper around the Amazon Bedrock Runtime client.
    """

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION
        )

        self.model_id = MODEL_ID

    def converse(self, messages: List[dict]) -> str:
        """
        Send the full conversation history to Amazon Bedrock.
        """

        response = self.client.converse(
            modelId=self.model_id,
            messages=messages,
        )

        return response["output"]["message"]["content"][0]["text"]

    def converse_stream(self, messages):
        """
        Yield text chunks from Amazon Bedrock.
        """

        response = self.client.converse_stream(
            modelId=self.model_id,
            messages=messages,
        )

        for event in response["stream"]:

            if "contentBlockDelta" not in event:
                continue

            delta = event["contentBlockDelta"]["delta"]

            if "text" not in delta:
                continue

            yield delta["text"]