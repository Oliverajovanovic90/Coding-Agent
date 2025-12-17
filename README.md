# Coding-Agent
Build a coding agent that can scaffold and extend projects. Use a Django template as the base project. Learn how agents act as project bootstrappers. 

# 🧠 Django AI Coding Agent

This repository contains a real Django project template and an AI-powered coding agent capable of reading, generating, and modifying Django projects using natural language instructions.

The agent uses OpenAI’s API with a tool-based architecture to safely interact with the filesystem, making it similar in spirit to modern coding agents like Cursor or Devin, but implemented from scratch for learning and extensibility.

## 🚀 What This Project Does
✅ Django Project Template

A reusable Django project scaffold

Proper project/app separation

Templates, URLs, views, and settings configured

Ready to run in a browser

## ✅ AI Coding Agent

Runs from the terminal

Accepts natural language instructions

Can:

Read project files

Create new files

Modify existing Django code

Generate documentation (README, views, templates, etc.)

Uses safe, sandboxed tools (no uncontrolled filesystem access)


📂 Repository Structure

```
.
├── run_agent.py              # Entry point for the AI coding agent (CLI)
├── tools.py                  # Safe agent tools (read/write files, run commands)
├── agent.ipynb               # Notebook version of the agent (experiments / learning)
├── experiments.ipynb         # Additional experiments
├── django_template/          # Reusable Django project template
│   ├── manage.py
│   ├── myproject/
│   ├── myapp/
│   ├── templates/
│   ├── pyproject.toml
│   └── uv.lock
├── my_new_app/               # Generated Django app (real runnable project)
│   ├── manage.py
│   ├── myproject/
│   ├── myapp/
│   ├── templates/
│   ├── pyproject.toml
│   └── uv.lock
└── .gitignore

```

## 🧠 How the AI Agent Works

The agent runs in the terminal (run_agent.py)

You give instructions like:

“Create a README explaining how to run this Django project”

The agent:

Reads relevant files

Decides what to change

Uses explicit tools to modify files

All changes happen inside a sandboxed project folder

This keeps the agent safe, predictable, and debuggable.

### ⚙️ Prerequisites

Python 3.8+

uv (Python package & environment manager)

OpenAI API key

## 🔑 Environment Setup

1️⃣ Set OpenAI API Key

In your terminal:

export OPENAI_API_KEY="sk-xxxx"


(Optional but recommended)

Create a .env file:

OPENAI_API_KEY=sk-xxxx


⚠️ .env is ignored by git and should never be committed.

### 🤖 How to Run the AI Coding Agent

From the repo root:

uv run python run_agent.py


You will see:

You:

Example commands to try:
Summarize the Django project structure.

Create a README.md explaining how to run this Django project using uv and make.

Add an About page using Django best practices and Tailwind CSS.

To exit the agent:
stop


or press Ctrl + C

### 🌐 How to Run the Django App in the Browser

1️⃣ Go into the Django app directory
cd my_new_app

2️⃣ Run database migrations
uv run python manage.py migrate

3️⃣ Start the development server
uv run python manage.py runserver


You should see:

Starting development server at http://127.0.0.1:8000/

4️⃣ Open in browser (Codespaces)

Go to the Ports tab

Forward port 8000

Click Open in Browser

🎉 Your Django app is now running live.

### 🧪 Development Notes

The agent runs in the terminal

Django runs as a web app

This separation is intentional and production-friendly

The project can be extended into:

A web UI for the agent

An API-based agent

A multi-project generator

### 📌 Why This Project Matters

This project demonstrates:

Real Django development

Safe LLM tool usage

Agent-based architecture

Practical AI + backend integration

Clean project organization

