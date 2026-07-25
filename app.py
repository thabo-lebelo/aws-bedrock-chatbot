from src.bedrock import invoke_model


def main():

    print("=" * 60)
    print(" AWS Bedrock Chatbot")
    print("=" * 60)

    prompt = "What is Amazon Bedrock?"

    print(f"\nYou: {prompt}")

    response = invoke_model(prompt)

    print("\nClaude:\n")

    print(response)


if __name__ == "__main__":
    main()