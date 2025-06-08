import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel
from tools import get_weather

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
    name="Jarvis",
    instructions="You are a helpful assistant",
    model=model,
)

weather_agent = Agent(
    name="Jarvis",
    instructions="You are a helpful assistant",
    model=model,
    tools=[get_weather]
)