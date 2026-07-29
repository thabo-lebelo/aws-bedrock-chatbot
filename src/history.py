from typing import List

from src.constants import MAX_CONTEXT_MESSAGES


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

    def formatted_history(self) -> str:
        """
        Return the conversation in a human-readable format.
        """
        if not self._messages:
            return "No conversation history."

        output = []

        for message in self._messages:
            role = "👨🏽‍🦲 You" if message["role"] == "user" else "🤖 AI"
            text = message["content"][0]["text"]

            output.append(f"{role}: {text}")

        return "\n\n".join(output)

    def context(self):
        """
        Return only the most recent messages.
        """
        return self._messages[-MAX_CONTEXT_MESSAGES:]

    def clear(self) -> None:
        self._messages.clear()

    def size(self) -> int:
        return len(self._messages)

    def is_empty(self) -> bool:
        return len(self._messages) == 0