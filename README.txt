# Local AI Support Bot (FastAPI & Ollama)

A lightweight, modular, and privacy-focused local AI chatbot backend built with **FastAPI** that integrates local Large Language Models (LLMs) via **Ollama** to simulate automated customer support for social media platforms (e.g., Instagram Direct Messages).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal?style=flat-square&logo=fastapi)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange?style=flat-square)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Frontend-38B2AC?style=flat-square&logo=tailwind-css)

---

## 🚀 Key Features

* **Asynchronous Backend:** Powered by FastAPI and `httpx` for fast, non-blocking asynchronous communication.
* **Local LLM Inference:** Connects seamlessly with Ollama running open-source models (optimized for `qwen2.5:7b`).
* **Strict Prompt & Language Control:** Custom system prompts and sampling parameters configured to maintain fluent Persian language fidelity and prevent hallucinations.
* **Interactive Frontend Demo:** A clean, responsive chat UI styled with Tailwind CSS for testing and live demonstrations.
* **Webhook Ready:** Includes structured endpoints for Meta/Instagram Webhook verification and event processing.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, Pydantic, HTTPX
* **AI Engine:** Ollama (Qwen 2.5:7b)
* **Frontend:** HTML5, Tailwind CSS
* **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
Social-Media-LLM/
│
├── main.py              # FastAPI application, routes, and Ollama integration
├── demo.html            # Interactive frontend chat interface
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (Ollama URL, model name)