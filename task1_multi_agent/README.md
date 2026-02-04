## Task 1: Multi-Agent Company Intelligence System

### Overview
This project demonstrates a multi-agent AI system built using LangChain.
The system is designed to showcase agent orchestration, role separation,
tool usage, and context flow using dummy data as permitted by the assignment.

The focus of this task is on **agent workflows and system design**, not on
external API integrations.

---

### Agent Architecture

The system consists of the following components:

- **Data Collector Agent**
  - Responsible for fetching company-related information
  - Uses a tool that returns dummy company news and stock data

- **Analyst Agent**
  - Consumes the output of the Data Collector Agent
  - Generates insights and potential risk factors based on the provided data

- **Orchestrator**
  - Controls the execution flow
  - Ensures agents run in the correct sequence
  - Passes context between agents

---

### Tools
- Tools are deterministic and return dummy data
- This design keeps the system reproducible and avoids external dependencies
- Dummy data usage is explicitly allowed as per the assignment instructions

---

### Memory
- `ConversationBufferMemory` is used to maintain shared context
- This enables information flow between agents across steps

---

### LLM & Agent Design Note
While the architecture supports integration with LLMs (such as OpenAI or
local models via Ollama), the final implementation uses **tool-first agents**
for stability and reproducibility.

This approach aligns with best practices when using lightweight models or
dummy data and keeps the focus on agent orchestration rather than text
generation.

---

### How to Run

```bash
pip install -r requirements.txt
python main.py
