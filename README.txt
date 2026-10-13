# Local AI Support Bot (FastAPI & Ollama)

A lightweight, modular, and privacy-focused local AI chatbot backend built with **FastAPI** that integrates local Large Language Models (LLMs) via **Ollama** to simulate automated customer support for social media platforms (e.g., Instagram Direct Messages).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal?style=flat-square&logo=fastapi)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange?style=flat-square)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Frontend-38B2AC?style=flat-square&logo=tailwind-css)


🚀 Key Features

* Asynchronous Backend Powered by FastAPI and `httpx` for fast, non-blocking asynchronous communication.
* Local LLM Inference Connects seamlessly with Ollama running open-source models (optimized for `qwen2.5:7b`).
* Strict Prompt & Language Control Custom system prompts and sampling parameters configured to maintain fluent Persian language fidelity and prevent hallucinations.
* Interactive Frontend Demo A clean, responsive chat UI styled with Tailwind CSS for testing and live demonstrations.
* Webhook Ready: Includes structured endpoints for Meta/Instagram Webhook verification and event processing.



🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, Pydantic, HTTPX
* **AI Engine:** Ollama (Qwen 2.5:7b)
* **Frontend:** HTML5, Tailwind CSS
* **Environment Management:** `python-dotenv`



📂 Project Structure

Social-Media-LLM/
│
├── main.py              # FastAPI application, routes, and Ollama integration
├── demo.html            # Interactive frontend chat interface
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (Ollama URL, model name)



⚙️ Installation & Running Guide

Choose your preferred method to run the project (with or without Docker).

Method 1: Running Locally (Without Docker)

1. Install Dependencies:

pip install fastapi uvicorn httpx python-dotenv pydantic




2. Run the Ollama Model:
Ensure Ollama is installed and running on your system, then download/run the model with this command

ollama run qwen2.5:7b




3. Start the FastAPI Backend

uvicorn main:app --reload


(The server will run on `http://127.0.0.1:8000`. You can access the interactive API docs at `http://127.0.0.1:8000/docs`.)



4. Run the Frontend Demo
Open a new terminal window, navigate to the project folder, and serve the HTML file using Python:

python -m http.server 3000

*Then open your browser and go to: `http://localhost:3000/demo.html*`




Method 2: Running with Docker

(If you prefer containerized deployment for the backend service)

1. Build the Docker Image:
Make sure a `Dockerfile` is present in your root directory, then run:

docker build -t local-ai-support-bot .


2. Run the Container:

docker run -d -p 8000:8000 --name ai-bot-container local-ai-support-bot
