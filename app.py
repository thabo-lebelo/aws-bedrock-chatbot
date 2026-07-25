from src.bedrock import create_client


def main():
    print("=" * 50)
    print(" AWS Bedrock Chatbot")
    print("=" * 50)

    print("\nConnecting to Amazon Bedrock...")

    client = create_client()

    print("✅ Connected successfully!")

    print(client)


if __name__ == "__main__":
    main()