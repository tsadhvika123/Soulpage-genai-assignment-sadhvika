from langchain.memory import ConversationBufferMemory
from tools import get_company_data, analyze_company_data

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

class DataCollectorAgent:
    def run(self, query: str):
        company = query.replace("Get latest information about ", "")
        return get_company_data.run(company)

class AnalystAgent:
    def run(self, data: str):
        return analyze_company_data.run(data)

def data_collector_agent():
    return DataCollectorAgent()

def analyst_agent():
    return AnalystAgent()
