🍲 Naija Eats

> An AI-powered behavioral simulation system that learns how individual users review restaurants — then predicts and writes reviews in their unique voice for places they have never visited.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [The Problem](#-the-problem)
- [Key Features](#-key-features)
- [User Workflow](#-user-workflow)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [Configuration](#-configuration)
- [Evaluation](#-evaluation)
- [Contributing](#-contributing)
- [Team](#-team)
- [License](#-license)

---

## 🌟 Overview

**Naija Eats** is a behavioral simulation agent built on large language models. It studies a user's review history on a restaurant platform, constructs a detailed behavioral fingerprint of that user, and uses it to generate accurate, voice-matched reviews for restaurants the user has never visited.

The system goes beyond surface-level personalization. It captures tone, rating psychology, complaint patterns, cultural context, and writing style — producing simulated reviews that are statistically and stylistically indistinguishable from the user's real reviews.

A core focus of this project is **cultural authenticity for Nigerian users** — the system understands and replicates Pidgin English, local food culture, and Nigerian rating behavior natively.

---

## 🎯 The Problem

Most AI-driven recommendation and review systems treat users as static profiles. They ignore:

- **Behavioral nuance** — how a user's mood, history, and personality shape their reviews
- **Cultural context** — different cultures rate, complain, and express praise differently
- **Linguistic identity** — a Nigerian reviewer doesn't sound like an American one
- **Contextual signals** — what triggers a 5-star versus a 3-star reaction for *this specific user*

Naija Eats addresses these gaps by building a deeply personalized behavioral model for each user, grounded in their actual review history and enriched with cultural context.

---

## ✨ Key Features

### 🧠 Behavioral Fingerprinting
Extracts a rich, multi-dimensional profile per user including rating distribution, sentiment patterns, preferred cuisines, writing style, and price sensitivity.

### 🔍 Retrieval-Augmented Reasoning
Before generating a review, the system retrieves the user's most semantically similar past reviews, grounding the LLM in real user behavior rather than abstract guessing.

### ✍️ Voice-Matched Review Generation
Produces written reviews and star ratings that match the user's exact tone, length, vocabulary, and personality.

### 🇳🇬 Nigerian Cultural Adaptation Layer
A dedicated post-processing module that adapts reviews to authentic Nigerian English, Pidgin expressions, and local food culture references.

### 📊 Confidence Scoring
Every generated review includes a confidence score and reasoning trace, making the system transparent and auditable.

### 🚀 Containerized API
Fully Dockerized FastAPI service with clean REST endpoints, ready for deployment anywhere.

---

## 👤 User Workflow

Here is how the system works in practice — told as a story.

### Meet Bayo

Bayo Adewale is a 28-year-old software engineer living in Yaba, Lagos. He is a serious foodie. Over the past year, he has reviewed **47 restaurants** on Yelp. From those reviews, Naija Eats has learned:

- He rarely rates below 3 stars unless service was terrible
- He loves amala, ewedu, and authentic Nigerian dishes
- His biggest trigger is slow service
- His reviews are short, blunt, and funny
- He rates ambience higher than price

This is **Bayo's behavioral fingerprint** — silently built and stored by the system.

### Monday Morning

Bayo's friend Chukwuemeka sends him a message:

> *"Bayo abeg, that new restaurant for Surulere — Mama Titi's Kitchen — you don chop there before?"*

Bayo has never been there. But Naija Eats already knows Bayo deeply, so the question becomes:

> *"How would Bayo review this place if he went?"*

### What Happens Behind The Scenes

**Step 1 — Profile Loaded**
The system pulls Bayo's full behavioral fingerprint from storage. His rating patterns, his complaints, his praises, his writing voice — all instantly available.

**Step 2 — Restaurant Details Come In**
The request arrives with details about Mama Titi's Kitchen:
- Location: Surulere, Lagos
- Menu: Amala, gbegiri, assorted meat
- Price: ₦2,500 average
- Ambience: Local bukateria
- Common feedback: Authentic food, but slow service

**Step 3 — Retrieval Layer Activates**
The system searches Bayo's review history for the **5 most similar places** he has been to before. It finds three local bukas he visited, one amala spot, and one restaurant where he complained heavily about waiting. These become evidence for the reasoning step.

**Step 4 — The Agent Reasons**
The LLM thinks through it step by step:

> *"Bayo loves amala — strong positive signal. Price is within his comfort zone — neutral. Ambience is local and authentic — he tends to appreciate this. But slow service is his biggest trigger and three out of five similar past reviews show him dropping stars for this exact reason. Predicted rating: 3 stars."*

**Step 5 — Review Generated**
The system writes a review in Bayo's natural voice:

> *"Mama Titi's amala? Honestly, e dey slap. The gbegiri was on point and the assorted meat was plenty. But this service ehn — I waited 25 minutes before anyone even looked my way. If they fix that thing, this place fit easily be a 5. For now? 3 stars. Potential dey."*

**Step 6 — Cultural Adaptation**
The Nigerian language layer reviews the output, ensuring authentic Pidgin usage and natural local expressions. It is not forced — it sounds like a real Lagosian wrote it.

**Step 7 — Response Returned**
Chukwuemeka receives:

- ⭐⭐⭐ Predicted rating: 3 out of 5
- The full simulated review above
- Confidence score: 87%
- A short reasoning trace explaining the prediction

Chukwuemeka laughs and replies: *"Haha this sounds exactly like Bayo. Make I try the place myself."*

### Why This Matters

The system did not guess. It **understood Bayo** — his personality, his triggers, his tone — and produced a review that is statistically and stylistically indistinguishable from one he would actually write.

This is the foundation of deep, context-aware user modeling.

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    INPUT LAYER                           │
│  User History (Reviews)  +  New Restaurant Details      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              BEHAVIORAL PROFILER                         │
│  Extracts fingerprint: tone, ratings, preferences,      │
│  complaints, writing style, cultural markers            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              RETRIEVAL LAYER                             │
│  ChromaDB vector store retrieves top-K similar past     │
│  reviews using sentence-transformer embeddings          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              LLM REASONING AGENT                         │
│  Claude Sonnet reasons over profile + retrieved         │
│  reviews + new restaurant to predict rating + review    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           CULTURAL ADAPTATION LAYER                      │
│  Refines output to authentic Nigerian voice,            │
│  Pidgin expressions, and local references               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                          │
│  Star Rating  +  Written Review  +  Confidence  +       │
│  Reasoning Trace                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language Model** | Claude Sonnet | Core reasoning and generation |
| **Embeddings** | sentence-transformers (all-MiniLM-L6-v2) | Semantic representation of reviews |
| **Vector Store** | ChromaDB | Fast similarity search over user reviews |
| **Agent Framework** | LangChain | Orchestrates retrieval + reasoning chain |
| **API Framework** | FastAPI | REST endpoints |
| **Container** | Docker | Reproducible deployment |
| **Data Processing** | Pandas, HuggingFace datasets | Yelp dataset handling |
| **Sentiment Analysis** | VADER, TextBlob | User tone extraction |
| **Evaluation** | scikit-learn, BERTScore, ROUGE | Metrics and validation |

---

## 📁 Project Structure

```
naija-eats/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entrypoint
│   ├── profiler.py             # Behavioral fingerprinting logic
│   ├── retriever.py            # Vector similarity retrieval
│   ├── generator.py            # LLM review generation
│   ├── nigerianizer.py         # Cultural adaptation layer
│   ├── schemas.py              # Pydantic request/response models
│   └── config.py               # Settings and environment vars
├── data/
│   ├── raw/                    # Raw Yelp dataset (gitignored)
│   ├── processed/              # Cleaned, filtered data
│   └── pipeline.py             # Data loading and preprocessing
├── models/
│   ├── embeddings.py           # Embedding utilities
│   └── prompts/                # Prompt templates
│       ├── review_generation.txt
│       └── cultural_adaptation.txt
├── evaluation/
│   ├── metrics.py              # RMSE, BERTScore, ROUGE
│   ├── human_eval.py           # Human evaluation framework
│   └── ablation.py             # Ablation study scripts
├── tests/
│   ├── test_profiler.py
│   ├── test_retriever.py
│   └── test_api.py
├── notebooks/
│   └── exploration.ipynb       # Data exploration
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- An Anthropic API key (Claude)
- (Optional) OpenAI API key for fallback

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-org/naija-eats.git
cd naija-eats
```

**2. Set up environment variables**

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
CHROMA_PERSIST_DIR=./data/chroma
LOG_LEVEL=INFO
```

**3. Install dependencies (local development)**

```bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**4. Download and process the dataset**

```bash
python -m data.pipeline --download --process
```

**5. Build user profiles and embed reviews**

```bash
python -m app.profiler --build-all
```

### Running Locally

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### Running with Docker

```bash
docker-compose up --build
```

---

## 📡 API Documentation

### `POST /simulate-review`

Generates a simulated review and rating for a given user and restaurant.

**Request Body:**

```json
{
  "user_id": "bayo_001",
  "restaurant": {
    "name": "Mama Titi's Kitchen",
    "category": "Nigerian",
    "price_range": "₦₦",
    "location": "Surulere, Lagos",
    "menu_highlights": ["amala", "gbegiri", "assorted meat"],
    "common_tags": ["authentic", "slow service"]
  }
}
```

**Response:**

```json
{
  "user_id": "bayo_001",
  "predicted_rating": 3,
  "review_text": "Mama Titi's amala? Honestly, e dey slap. The gbegiri was on point and the assorted meat was plenty. But this service ehn — I waited 25 minutes before anyone even looked my way. If they fix that thing, this place fit easily be a 5. For now? 3 stars. Potential dey.",
  "confidence": 0.87,
  "reasoning": "User has high tolerance for authentic local food (avg 4.2 for Nigerian cuisine) but consistently penalizes slow service (-1 to -2 stars in 8 of 12 similar cases)."
}
```

### `GET /users/{user_id}/profile`

Returns the behavioral fingerprint for a user.

### `GET /health`

Health check endpoint.

---

## ⚙ Configuration

All configuration lives in `.env` and `app/config.py`.

| Variable | Default | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Required for Claude API |
| `LLM_MODEL` | `claude-sonnet-4-20250514` | LLM to use for generation |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence transformer model |
| `TOP_K_RETRIEVAL` | `5` | Number of similar reviews to retrieve |
| `MIN_USER_REVIEWS` | `10` | Minimum review history to build profile |
| `ENABLE_CULTURAL_LAYER` | `true` | Toggle the Nigerian adaptation layer |

---

## 📊 Evaluation

The system is evaluated on three core metrics:

| Metric | Tool | Target |
|---|---|---|
| **Rating Accuracy** | RMSE | < 0.7 |
| **Review Text Quality** | BERTScore F1 | > 0.85 |
| **Behavioral Fidelity** | Human Evaluation | > 80% authentic |

Run the full evaluation suite:

```bash
python -m evaluation.metrics --run-all
```

Run the ablation study:

```bash
python -m evaluation.ablation
```

---

## 🤝 Contributing

We welcome contributions from team members. Please follow these guidelines:

### Workflow

1. **Branch from `develop`** — never commit directly to `main` or `develop`
2. **Naming convention**: `feature/<name>`, `fix/<name>`, `docs/<name>`
3. **Commit messages**: Use conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`)
4. **Pull Requests**: Require at least one review before merge
5. **Code style**: Run `black .` and `flake8` before committing

### Setting Up for Development

```bash
pip install -r requirements-dev.txt
pre-commit install
```

### Running Tests

```bash
pytest tests/ -v --cov=app
```

---

## 👥 Team

| Name | Role | Contact |
|---|---|---|
| _Olayinka Akanji_ | Project Lead | _akanjiolayinka01@gmail.com_ |
| _MicheaL Tunwase_ | ML Engineer | motrned@gmail.com|

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Yelp for the open dataset
- Anthropic for the Claude API
- The open-source ML community for the foundational tools that make this possible

---

<p align="center">Built with care, by people who believe AI should understand culture, not erase it.</p>
