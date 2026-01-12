# This is runnable primitive that allows you to apply custom python function into runnabes and this will heps us to connect to other runnable functions within an AI pipeline . 


# Ques - review are given to us --> llm --> sentimnt 
# but our llm is not giving good results---> so we need to do preproccing onto the review data ---> so preprocessig function --> is to be converted into the lambda function. 

# Ques-> joke --> topic --> also print number of words . 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnablePassthrough , RunnableLambda
from dotenv import load_dotenv

load_dotenv()

#1. llm creation 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# prompt -> llm -> parser -> parallel chain --> passthrough 
                #                           --> runnable lambda -> gives us count of words . 


def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke('HI , MY NAME IS VARU '))