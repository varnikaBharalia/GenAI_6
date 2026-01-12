# This is used for the the creation of thc conditional chain 
# LIKE --> IF ELSE

# Email -aayega-> prompt bhjege --> llm telss kaisa problem h --> then we make multiple branches for each issue. 

# topic-> prompt -> llm -> parse --> if report >500 words then again summarise otherwise do print that report 


from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnablePassthrough , RunnableLambda , RunnableBranch
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

prompt = PromptTemplate(
    template='Write a detailed report about {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Summarise the following text \n {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

report_gen_chain =  RunnableSequence(prompt , llm ,parser )

# brach_chain = RunnableBranch(
#     (cond , runnable),
#     (),()........
#     default
# )
brach_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100 , RunnableSequence(prompt2 , llm , parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , brach_chain)

print(final_chain.invoke({'topic': 'Russia ukrain war'}))