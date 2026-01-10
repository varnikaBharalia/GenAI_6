import random

class NakliLLM:
    def __init__(self):
        print('LLM created')

    def predict(self, prompt):
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}

class NakliPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        # Uses unpacking (**) to inject dictionary keys into the string template
        return self.template.format(**input_dict)

class NakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        # 1. Format the template with user input
        final_prompt = self.prompt.format(input_dict)
        # 2. Pass formatted string to the LLM
        result = self.llm.predict(final_prompt)
        # 3. Return only the text response
        return result['response']

# --- Execution ---

# 1. Setup Template
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

# 2. Setup LLM
llm = NakliLLM()

# 3. Setup the Chain (This was the missing piece)
chain = NakliLLMChain(llm=llm, prompt=template)

# 4. Run the Chain
output = chain.run({'length': 'short', 'topic': 'india'})
print(f"Final Output: {output}")