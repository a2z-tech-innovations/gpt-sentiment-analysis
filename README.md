# 🚀 AI-Powered Content Generator & Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)

A powerful web application that harnesses OpenAI's GPT model to generate detailed content on any topic and perform sentiment analysis on text. Built with FastAPI and modern web technologies.

## ✨ Features

- **AI-Powered Content Generation**: Create detailed articles on any topic with a single click
- **Sentiment Analysis**: Analyze text to determine emotional tone and sentiment
- **Readability Assessment**: Get readability scores for your content
- **Clean Modern UI**: User-friendly interface built with Tailwind CSS
- **API-First Design**: Well-structured backend with documented API endpoints
- **Database Storage**: Save all generated content and analysis results for future reference

## 🔧 Tech Stack

- **Backend**: FastAPI, Python 3.10+
- **AI Integration**: OpenAI GPT-3.5-turbo API
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Deployment**: Compatible with Docker, cloud platforms

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Poetry (for dependency management)

## 🚀 Getting Started

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/gpt-sentiment-analysis.git
   cd gpt-sentiment-analysis
   ```

2. **Install dependencies**

   ```bash
   poetry install
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root with the following content:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Application

1. **Start the server**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

2. **Access the application**

   Open your browser and navigate to: http://localhost:8000

## 💻 Usage

### Content Generation

1. Enter a topic in the "Generate Content" section
2. Click the "Generate Content" button
3. View the AI-generated article in the Results section

### Content Analysis

1. Enter or paste text in the "Analyze Content" section, or click "Import Generated Content" to use previously generated text
2. Click the "Analyze Content" button
3. View the sentiment analysis and readability score in the Results section

## 🔌 API Endpoints

- `GET /`: Main web interface
- `POST /generate`: Generate content based on a topic
- `POST /analyze`: Analyze the sentiment and readability of provided content

## 📝 Project Structure

```
gpt-sentiment-analysis/
├── app/
│   ├── __init__.py
│   ├── crud.py            # Database operations
│   ├── database.py        # Database connection
│   ├── main.py            # FastAPI application
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   └── utils.py           # Helper functions
├── templates/
│   └── index.html         # Web interface
├── .env                   # Environment variables
├── pyproject.toml         # Project dependencies
└── README.md             # Project documentation
```

## 🛠️ Customization

### Changing the OpenAI Model

To use a different OpenAI model, modify the `model` parameter in the `generate_content` and `get_sentiment_analysis` functions in `app/utils.py`.

### Expanding Functionality

This project can be extended to include:
- User authentication
- Saving and retrieving past analyses
- Additional text metrics (tone, complexity, etc.)
- Content summarization features

## 📄 License

[MIT License](LICENSE)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Disclaimer

This application uses the OpenAI API, which may incur costs based on usage. Please review OpenAI's pricing structure and set appropriate usage limits.

---

Made with ❤️ by A to Z Tech Innovations, LLC