from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
).with_structured_output(Facts)

prompt = PromptTemplate(
    template="Give 3 facts about {topic}",
    input_variables=["topic"]
)

chain = prompt | model

result = chain.invoke({"topic": "black hole"})
print(result)
