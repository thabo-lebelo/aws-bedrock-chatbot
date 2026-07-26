from src.bedrock import invoke_model


class BedrockChatbot:
    """
    Simple command-line chatbot powered by Amazon Bedrock.
    """

    def __init__(self):
        self.version = "0.2.0"

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to Amazon Bedrock and return the response.
        """
        return invoke_model(prompt)

    def run(self):
        """
        Start the chatbot.
        """
        self.print_banner()

        while True:
            prompt = input("\nYou > ").strip()

            if not prompt:
                continue

            if prompt.lower() == "exit":
                print("\n👋 Thanks for using AWS Bedrock Chatbot.")
                break

            response = self.ask(prompt)

            print("\nAI >")
            print(response)

    def print_banner(self):
        print("=" * 60)
        print("🤖 AWS Bedrock Chatbot")
        print("Building AI Applications on AWS")
        print()
        print(f"Version : v{self.version}")
        print("Model   : Amazon Nova Lite")
        print("=" * 60)