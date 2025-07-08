from langchain.prompts import PromptTemplate

template = """
You will be asked questions based on the provided pdf. Answer Those Questions.

Context: {context}
Question: {question}
Answer:

"""

prompt = PromptTemplate(template= template, input_variables= ["context", "question"])