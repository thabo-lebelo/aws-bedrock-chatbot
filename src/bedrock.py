import boto3

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

    def converse(self, prompt: str) -> str:
        """
        Send a prompt to Amazon Bedrock using the Converse API.
        """

        response = self.client.converse(
            modelId=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        return response["output"]["message"]["content"][0]["text"]