# 🤖 AWS Bedrock Chatbot

> **Building AI Applications on AWS – A Practical Journey with Amazon Bedrock**

This repository contains the source code for my **Building AI Applications on AWS** blog series, where I document my journey of learning Generative AI on AWS while preparing for the **AWS Certified AI Engineer – Associate** certification.

Rather than building disconnected demos, this project evolves over time. Each article introduces a new capability while improving the same application, taking it from a simple command-line chatbot to a production-inspired AI solution powered by Amazon Bedrock.

---

## 📚 Blog Series

| Part      | Topic                                       | Version  |    Status   |
| --------- | ------------------------------------------- | -------- | :---------: |
| ✅ Part 1  | My First Conversation with Amazon Bedrock | `v0.1.0` |   Complete  |
| ✅ Part 2 | Building an Interactive CLI Chatbot         | `v0.2.0` | In Progress |
| 🚧 Part 3  | Adding Conversation Memory                  | `v0.3.0` |   Planned   |
| ⏳ Part 4  | Streaming Responses                         | `v0.4.0` |   Planned   |
| ⏳ Part 5  | Prompt Engineering                          | `v0.5.0` |   Planned   |
| ⏳ Part 6  | Comparing Foundation Models                 | `v0.6.0` |   Planned   |
| ⏳ Part 7  | Structured Outputs                          | `v0.7.0` |   Planned   |
| ⏳ Part 8  | Document Summarisation                      | `v0.8.0` |   Planned   |
| ⏳ Part 9  | Embeddings                                  | `v0.9.0` |   Planned   |
| ⏳ Part 10 | Retrieval-Augmented Generation (RAG)        | `v1.0.0` |   Planned   |
| ⏳ Part 11 | Amazon Bedrock Knowledge Bases              | `v1.1.0` |   Planned   |
| ⏳ Part 12 | Amazon Bedrock Agents                       | `v1.2.0` |   Planned   |
| ⏳ Part 13 | Guardrails                                  | `v1.3.0` |   Planned   |
| ⏳ Part 14 | Deploying to AWS                            | `v1.4.0` |   Planned   |
| ⏳ Part 15 | Observability & Cost Optimisation           | `v1.5.0` |   Planned   |

---

# 🚀 Project Goal

The objective of this repository is to build a complete AI application while exploring the capabilities of Amazon Bedrock.

Throughout the series we will learn how to:

* Connect to Amazon Bedrock
* Use the Converse API
* Build conversational AI applications
* Compare different foundation models
* Stream responses
* Engineer better prompts
* Build Retrieval-Augmented Generation (RAG) applications
* Use Amazon Bedrock Knowledge Bases
* Build AI Agents
* Deploy AI workloads on AWS

Each feature builds upon the previous one, allowing the application to evolve naturally over time.

---

# ☁️ AWS Services

This project currently uses:

* Amazon Bedrock
* Amazon Bedrock Runtime
* AWS Identity and Access Management (IAM)

Future articles will introduce additional AWS services including:

* Amazon S3
* AWS Lambda
* Amazon CloudWatch
* Amazon Bedrock Knowledge Bases
* Amazon Bedrock Agents
* Amazon API Gateway

---

# 🛠️ Technology Stack

* Python 3.12+
* boto3
* python-dotenv
* Amazon Bedrock
* Amazon Nova Lite
* AWS CLI

---

# 📦 Getting Started

## Clone the repository

```bash
git clone https://github.com/thabo-lebelo/aws-bedrock-chatbot.git

cd aws-bedrock-chatbot
```

## Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure AWS

Ensure that:

* AWS CLI is installed
* AWS credentials are configured
* Amazon Bedrock model access has been enabled

Copy the example environment file.

```bash
cp .env.example .env
```

Update the required values before running the application.

---

# ▶️ Running the Application

```bash
python app.py
```

---

# 📝 Blog Articles

Every article corresponds to a Git tag.

This ensures the code in the article always matches the repository version.

| Blog Article | Git Tag  |
| ------------ | -------- |
| Part 1       | `v0.1.0` |
| Part 2       | `v0.2.0` |
| Part 3       | `v0.3.0` |

When following an article, check out the corresponding version:

```bash
git checkout tags/v0.1.0
```

---

# 🎯 Learning Objectives

This repository focuses on both **Generative AI** and **Software Engineering**.

Beyond simply invoking models, the series explores:

* Clean Architecture
* Python Best Practices
* Cloud Design Patterns
* AI Application Design
* Production Readiness
* AWS Best Practices

---

# 🤝 Contributing

This repository is primarily a personal learning project.

However, suggestions, improvements, and discussions are always welcome.

If you find an issue or have an idea, feel free to open an issue or submit a pull request.

---

# 📖 Follow the Journey

📚 Blog

https://www.thabo-lebelo.com

💼 LinkedIn

https://www.linkedin.com/in/thabolebelo/

⭐ If you find this project useful, consider giving it a star. It helps others discover the repository and motivates me to continue building and documenting the journey.

---

# 📄 License

This project is licensed under the MIT License.
