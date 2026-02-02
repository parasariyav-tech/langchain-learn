from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=0
)

result = model.invoke("What is the capital of India?")

print("Answer:", result.content)

if result.usage_metadata:
    print("Prompt tokens:", result.usage_metadata["input_tokens"])
    print("Completion tokens:", result.usage_metadata["output_tokens"])
    print("Total tokens:", result.usage_metadata["total_tokens"])
