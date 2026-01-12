# Ques - topic given --> llm1-->tweet kare and llm2 --> linkedIn pr post daale 
# execuation of chains prallely independently dege but ye input ek hi rhega .. but output is a dict .

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel
from dotenv import load_dotenv

load_dotenv()

#1. llm creation 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

#2.  prompt creation 
prompt = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template=' Generate a  linkedIn post about {topic}',
    input_variables=['topic']
)


# 3. Parser creation 
parser = StrOutputParser()


# Parallel chian  = is a dictonary 
parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt , llm , parser),
    'linkedIn': RunnableSequence(prompt2 , llm , parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)
