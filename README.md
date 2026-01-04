# 🧠 Content Creation Pipeline — Groq Edition (100% FREE)

An **AI-powered multi-agent content generation pipeline** built using **Python, Flask, and Groq LLMs (Llama 3.3 70B)**.  
This system automates **research, outlining, content writing, SEO optimization, fact-checking, and image prompts** using a modular agent-based architecture.

---

## 📁 Project Structure

```
CONTENT-PIPELINE-GROQ/
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── outline_agent.py
│   ├── content_agent.py
│   ├── image_agent.py
│   ├── factcheck_agent.py
│   └── seo_agent.py
│
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── orchestrator.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── config.py
├── requirements.txt
├── .env
└── README.md
```

---

## ✨ Features

- 🔬 AI-powered research generation  
- 🧩 Structured outline creation  
- ✍️ Long-form content writing  
- 🧠 Fact-checking agent  
- 🔍 SEO optimization agent  
- 🎨 Image prompt generation  
- ⚙️ Modular multi-agent pipeline  
- 🌐 Web UI using Flask  
- ⚡ Ultra-fast inference using Groq  

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Groq API**
- **Llama 3.3 70B**
- **HTML / Jinja2**
- **python-dotenv**
- **Requests**

---

## 🚀 Step 1: Get Your FREE Groq API Key

### 1.1 Visit Groq Console  
👉 https://console.groq.com

### 1.2 Sign Up (FREE)
- Click **Sign Up**
- Verify email
- ❌ No credit card required

### 1.3 Create API Key
- Go to **API Keys**
- Click **Create API Key**
- Copy the key

Example:
```
gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ⚙️ Step 2: Project Setup

### 2.1 Create Project Folder
```bash
mkdir content-pipeline-groq
cd content-pipeline-groq
```

### 2.2 Create Virtual Environment
```bash
python -m venv venv
```

### Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

## 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Installs:
- Flask
- groq
- requests
- python-dotenv

---

## 🔑 Step 4: Configure API Key

Create `.env` file:
```
GROQ_API_KEY=gsk_your_actual_key_here
```

⚠️ Never commit `.env` to GitHub.

---

## 🔁 Step 5: Update Agent Imports

Replace **everywhere**:

```python
from utils.api_client import GPTClient
```

With:
```python
from utils.api_client import GroqClient
```

And change:
```python
self.client = GPTClient()
```

To:
```python
self.client = GroqClient()
```

### Files to Update
- research_agent.py
- outline_agent.py
- content_agent.py
- image_agent.py
- factcheck_agent.py
- seo_agent.py
- orchestrator.py

---

## ▶️ Step 6: Run the Application

```bash
python app.py
```

Expected output:
```
============================================================
🚀 Content Creation Pipeline - Groq Edition
============================================================
✓ API Key configured: True
✓ Model: llama-3.3-70b-versatile
✓ Server running on http://localhost:5000
============================================================
```

---

## 🌐 Step 7: Use the App

1. Open browser → http://localhost:5000  
2. Enter a topic  
3. Click **Generate Content**  
4. Wait ~30–45 seconds ⚡  
5. View AI-generated content 
```



```

---

## 📜 License (MIT)

MIT License

Copyright (c) 2025 Smart Bandwidth Monitor
```



