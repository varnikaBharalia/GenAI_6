# Joke andno. of words as well . 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnablePassthrough , RunnableLambda
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence( prompt | llm | parser)

paralle_chain = RunnableParallel({
        'joke' : RunnablePassthrough(),
        'word_count' : RunnableLambda( lambda x: len(x.split()))
})
final_chain = RunnableSequence(joke_gen_chain | paralle_chain)

result = final_chain.invoke({'topic' : 'AI'})
print(result)




