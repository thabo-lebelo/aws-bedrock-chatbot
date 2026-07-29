import os
import time

from src.logger import get_logger
from src.bedrock import BedrockClient
from src.constants import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    DEFAULT_MODEL_NAME,
    DIVIDER,
    AVAILABLE_COMMANDS
)
from src.history import ConversationHistory

class BedrockChatbot:
    """
    Command-line chatbot powered by Amazon Bedrock.
    """

    def __init__(self):
        self.version = "0.2.0"
        self.running = True
        self.logger = get_logger()
        self.bedrock = BedrockClient()
        self.history = ConversationHistory()
        self.logger.info("AWS Bedrock Chatbot started.")

    def ask(self, prompt: str) -> str:
        self.history.add_user_message(prompt)

        response = self.bedrock.converse(
            self.history.messages()
        )

        self.history.add_assistant_message(response)

        return response

    def run(self):
        """Main application loop."""
        self.print_banner()

        while self.running:
            prompt = input("\n👨🏽‍🦲 You > ").strip()

            if not prompt:
                print("⚠️ Please enter a prompt.")
                continue

            if self.handle_command(prompt):
                continue

            try:
                start = time.perf_counter()
                response = self.ask(prompt)
                elapsed = time.perf_counter() - start

                print("\n🤖 AI >")
                print(response)
                print(f"\n⏱ Response generated in {elapsed:.2f} seconds.")
                print("\n" + "-" * 60)
                self.logger.info("Response received successfully.")

            except Exception as ex:
                self.logger.exception(ex)
                print("\n❌ Unable to process your request.")
                print(
                    "\nCheck your internet connection,"
                    " AWS credentials, and Bedrock configuration."
                )

    def handle_command(self, command: str) -> bool:

        command = command.lower()

        if command == "help":

            print("\nAvailable Commands: \n")
            for command, description in AVAILABLE_COMMANDS.items():
                print(f"{command:<10} {description} \n")

            return True

        if command == "version":
            print(f"\nVersion: {self.version}")
            return True

        if command == "history":
            print()

            print("=" * 70)
            print("Conversation History")
            print("=" * 70)

            print(self.history.formatted_history())

            print("=" * 70)

            return True

        if command == "reset":

            self.history.clear()

            self.logger.info("Conversation history cleared.")

            print("\n✅ Conversation history has been cleared.")

            return True    

        if command == "clear":
            self.clear_screen()
            self.print_banner()
            return True

        if command == "exit":
            self.logger.info("Application closed.")
            self.running = False
            print("\n👋🏽 Thanks for using Thabo's chatbot.\n")
            return True

        return False

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_banner(self):
        print("\n" + DIVIDER)
        print("\n" + f"🤖 {APP_NAME}")
        print("\n" + APP_DESCRIPTION)

        print("\n" + f"Version : v{APP_VERSION}")
        print("\n" + f"Model   : {DEFAULT_MODEL_NAME}")

        print("\n" + DIVIDER)

        print("\n" + "Type 'help' to display available commands.")
        print("\n" + "Ready!")