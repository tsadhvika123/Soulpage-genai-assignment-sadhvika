from agents import data_collector_agent, analyst_agent

def run_company_intelligence(company_name: str):
    collector = data_collector_agent()
    analyst = analyst_agent()

    print("🔹 Collecting company data...")
    company_data = collector.run(f"Get latest information about {company_name}")

    print("\n🔹 Analyzing company data...")
    analysis = analyst.run(
        f"Analyze the following data and provide insights and risks:\n{company_data}"
    )

    return analysis

if __name__ == "__main__":
    result = run_company_intelligence("OpenAI")
    print("\n✅ FINAL COMPANY INSIGHTS:\n")
    print(result)
