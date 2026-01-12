# return the input as output without modifying it . 
# Ques-  we ahev seen there is the problem in the question of joke in runnable sequence as there .. we give joke and get its expaltion .. but only explaitionn is gettinh printed but the joke is not printed this is just made answered by using passThrough 

#  prompt -> llm -> parser --> gets joke thine we willl do a parallel chain 


from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnablePassthrough
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

joke_gen_chain = RunnableSequence(prompt , llm , parser)

paralle_joke_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explain': RunnableSequence(prompt2 , llm , parser)
})

final_chain = RunnableSequence(joke_gen_chain , paralle_joke_chain)

result = final_chain.invoke({"topic" : "India"})
print(result)