from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# ---------------- Models ----------------
model = ChatOpenAI()

# ---------------- Prompts ----------------
prompt_notes = PromptTemplate(
    template="Generate short and simple notes from the following text:\n{text}",
    input_variables=["text"]
)

prompt_quiz = PromptTemplate(
    template="Generate 5 short question-answer pairs from the following text:\n{text}",
    input_variables=["text"]
)

prompt_merge = PromptTemplate(
    template="""
Combine the content below into a study document.

STRICT RULES:
- Keep the quiz as questions and answers
- Do NOT summarize the quiz
- Keep notes and quiz as separate sections

### Notes
{notes}

### Quiz
{quiz}
""",
    input_variables=["notes", "quiz"]
)

# ---------------- Parser ----------------
parser = StrOutputParser()

# ---------------- Parallel Chain ----------------
parallel_chain = RunnableParallel({
    "notes": prompt_notes | model | parser,
    "quiz": prompt_quiz | model | parser,
})

# ---------------- Merge Chain ----------------
merge_chain = prompt_merge | model | parser

# ---------------- Full Chain ----------------
chain = parallel_chain | merge_chain

# ---------------- Input ----------------
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.
Still effective in cases where number of dimensions is greater than the number of samples.
Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
Versatile: different Kernel functions can be specified for the decision function.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, choosing Kernel functions and regularization is crucial.
SVMs do not directly provide probability estimates; these are calculated using expensive cross-validation.
"""

# ---------------- Run ----------------
result = chain.invoke({"text": text})
print(result)

# ---------------- Graph ----------------
chain.get_graph().print_ascii()
