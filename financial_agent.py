from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os

from dotenv import load_dotenv

openai.api_key= os.getenv("OPENAI_API_KEY")
## web search
web_search_agent = Agent(
    name='Web Search Agent',
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

## finance

finance_agent = Agent(
    name='Finance AI Agent',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
        ],
    instructions=["Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True, 
)


multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use Tables to display the data"],
    model=Groq(id="llama-3.1-70b-versatile"),
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarise analyst recommendation and share the latest news for NVIDIA", stream=True)