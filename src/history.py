from typing import List


class ConversationHistory:
    """
    Stores the conversation exchanged between the user and
    Amazon Bedrock using the Converse API message format.
    """

    def __init__(self):
        self._messages: List[dict] = []

    def add_user_message(self, prompt: str) -> None:
        self._messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        )

    def add_assistant_message(self, response: str) -> None:
        self._messages.append(
            {
                "role": "assistant",
                "content": [
                    {
                        "text": response
                    }
                ]
            }
        )

    def messages(self) -> List[dict]:
        """
        Return the conversation history in the format expected
        by the Converse API.
        """
        return self._messages

    def clear(self) -> None:
        self._messages.clear()

    def size(self) -> int:
        return len(self._messages)

    def is_empty(self) -> bool:
        return len(self._messages) == 0