from langchain.tools import tool


@tool
def get_company_data(company: str) -> str:
    """
    Fetch latest company news and stock performance.
    Dummy data used for demonstration.
    """
    return f"""
Company Name: {company}

Stock Performance:
- Stock increased by 4% over the last month
- Market sentiment: Positive

Recent News:
- Launched a new AI-powered product
- Expanded operations in Europe
- Reported strong quarterly earnings
"""


@tool
def analyze_company_data(data: str) -> str:
    """
    Analyze company data and generate insights.
    """
    return f"""
Analysis Summary:
- Strong growth momentum due to new product launches
- Geographic expansion reduces dependency on single markets
- Potential risks include high competition and market volatility

Input Data:
{data}
"""
