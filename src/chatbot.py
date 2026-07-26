import os

from src.logger import get_logger
from src.bedrock import BedrockClient


class BedrockChatbot:
    """
    Command-line chatbot powered by Amazon Bedrock.
    """

    def __init__(self):
        self.version = "0.2.0"
        self.running = True
        self.logger = get_logger()
        self.bedrock = BedrockClient()
        self.logger.info("AWS Bedrock Chatbot started.")

    def ask(self, prompt: str) -> str:
        """Send a prompt to Amazon Bedrock."""
        self.logger.info(f"Prompt: {prompt}")
        return self.bedrock.converse(prompt)

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
                response = self.ask(prompt)

                print("\n🤖 AI >")
                print(response)
                print("\n" + "-" * 60)
                self.logger.info("Response received successfully.")

            except Exception as ex:
                self.logger.exception(ex)
                print("\n❌ Something went wrong.")
                print(str(ex))

    def handle_command(self, command: str) -> bool:

        command = command.lower()

        if command == "help":

            print("""
                Available Commands
                ------------------
                help      Show this help menu
                version   Display application version
                clear     Clear the screen
                exit      Exit the chatbot
            """)

            return True

        if command == "version":
            print(f"\nVersion: {self.version}")
            return True

        if command == "clear":
            self.clear_screen()
            self.print_banner()
            return True

        if command == "exit":
            self.logger.info("Application closed.")
            self.running = False
            print("\n👋🏽 Thanks for using AWS Bedrock Chatbot.")
            return True

        return False

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_banner(self):
        print("=" * 60)
        print("🤖 AWS Bedrock Chatbot")
        print("Building AI Applications on AWS")
        print()
        print(f"Version : v{self.version}")
        print("Model   : Amazon Nova Lite")
        print("=" * 60)