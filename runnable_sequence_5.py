# Ques - Generate a joke and then give its explaition also . 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

#3. llm creation 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 1. prompt creation 
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Explain the following text - {text}',
    input_variables=['text']
)


# 2. Parser creation 
parser = StrOutputParser()

# 4... Chain with the help of runnable sequence

chain = RunnableSequence(prompt , llm  , parser , prompt2 , llm , parser)
result = chain.invoke({'topic' : 'AI'})
print(result)