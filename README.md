---
title: Dream Team Chatbot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.31.0" 
app_file: app.py
pinned: false
---

# 🤖 The Dream Team AI Chatbot 🤖

This project is a unique, persona-driven AI chatbot built with Python, Langchain, and Gradio. Instead of a generic assistant, this application allows users to "chat" with a panel of legendary figures from the world of computer science and embedded systems.

## ✨ The Dream Team

The AI adopts the persona of the figure most relevant to the user's question, providing expert and in-character responses. The team includes:

*   **[Dennis Ritchie]:** The father of C and UNIX.
*   **[Bjarne Stroustrup]:** The father of C++.
*   **[Michael Barr]:** An expert in embedded systems safety.
*   **[Jack Ganssle]:** A pragmatic expert in firmware and debugging.
*   **[Pete Warden]:** The pioneer of TinyML and AI on the edge.

This project demonstrates a powerful use of "system prompts" to create a sophisticated and engaging user experience.

## 🚀 Getting Started

To run this project, you will need an API key for Google Gemini.

1.  **Clone the repository:**
    ```bash
    git clone [Your-GitHub-Repo-URL-Here]
    cd dream-team-chatbot
    ```

2.  **Set up the Python environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    *   Create a file named `.env` in the root of the project.
    *   Add your key to the file in the following format:
    ```
    GEMINI_API_KEY=your_gemini_api_key
    ```

5.  **Launch the Web App:**
    ```bash
    python app.py
    ```
    The application will be running on `http://localhost:8080` or a similar address.

## 🛠️ Technology Stack

*   **AI Framework:** Langchain
*   **LLM:** Google Gemini (`gemini-1.5-flash`)
*   **Web Interface:** Gradio
*   **Core Language:** Python 3
*   **Key Libraries:** `langchain-google-genai`, `gradio`, `python-dotenv`