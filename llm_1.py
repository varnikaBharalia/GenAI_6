# Component we are going to create that will be going to use in futher 
import random

class NakliLLM:
    def __init__(self):
        print('LLM created')

    def predict(self, prompt):
        # List of possible responses
        response_list = [
            'Delhi is the Capital of India',
            'IPL is a cricket league',
            'AI stands for artificial intelligence'
        ]
        return {'response': random.choice(response_list)}

# 1. Instantiate the class using ()
# llm = NakliLLM() 

# 2. Call the method on the instance
# result = llm.predict('What is the capital of India')
# print(result)


# DEMO PROMPT TEMPLATE: - 

class NakliPromptTemplate:

    def __init__(self , template , input_variables):

        self.template = template
        self.input_variables = input_variables
    
    def format(self , input_dict):
        return self.template.format(**input_dict)
        

template = NakliPromptTemplate(
    template='write a poem about {topic}',
    input_variables=['topic']
)

prompt = template.format({'topic' : 'india'})
print(prompt)

# LLM App

llm = NakliLLM()
result = llm.predict(prompt)
print(result)
