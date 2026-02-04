# Soulpage GenAI Assignment

This repository contains my submission for the Soulpage Generative AI assignment.
It includes two tasks demonstrating multi-agent systems and conversational AI
with memory using LangChain.

---

## Repository Structure:
This repository is organized into two main folders, each corresponding to one task in the assignment.

The task1_multi_agent folder contains the implementation of the multi-agent company intelligence system. It includes the main execution file (main.py), agent definitions (agents.py), tool implementations (tools.py), a requirements.txt file for dependencies, and a task-specific README explaining the approach.

The task2_conversational_bot folder contains the conversational knowledge bot. It includes the chatbot entry file (app.py), its dependency list (requirements.txt), and a README describing the conversational architecture and usage.

A .gitignore file is included at the root level to exclude virtual environments and unnecessary files from version control.

---

## Task 1: Multi-Agent Company Intelligence System

### Description
A multi-agent AI system where multiple agents collaborate to generate company
insights.

### Architecture
- Data Collector Agent: Retrieves company data using dummy tools
- Analyst Agent: Analyzes the data and generates insights
- Orchestrator: Controls the execution flow

Dummy/static data is used as permitted by the assignment.

### How to Run
```bash
cd task1_multi_agent
pip install -r requirements.txt
python main.py
```

## Task 2: Conversational Knowledge Bot

### Overview
This task implements a conversational AI bot using LangChain that can answer
factual questions and maintain context across multiple user interactions.
The bot supports follow-up questions using conversation memory.

### Architecture
- ConversationChain for managing the conversational flow
- ConversationBufferMemory to store and reuse conversation history
- Local LLM: Phi, running via Ollama
- Interface: Command-line chat loop

### Features
- Answers factual queries
- Maintains conversation context
- Supports follow-up questions
- Runs locally without paid APIs

### Example
User: Who is the CEO of OpenAI?
Bot: Sam Altman

User: Where did he study?
Bot: (Understands context using memory)

### How to Run

```bash 
cd task2_conversational_bot
pip install -r requirements.txt
python app.py
```
