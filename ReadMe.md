# Runnables:-

1) Chains are impletemeted through the runnables . 

2) Why runnables exist ? - The team of LangChain observed that in the future there will be a incresed demansd of the LLM based apps . And each comapny big tech have ther apis and they have differnet codes .. so they thought of creating a framnework that will contain the apis of all imporant comanies LLM apps and they have a same code base . so there will be a vety minimal code changes we have to do . 

3) Interaction with the LLM is one part and there are also some other parts and some other tasks we have to do and langchain thought of helping the developers to help in the other tasks by creating the differnt components . 
        eg:- pdf loader , text splitter , embedding etc . 

        
4) Propmts are created manually  by the AI engineeres and this is the step that is done everytime so this  was automated  so make it that it just make the prompt -> send to llm -> gives response --> hence chain is created. 

5) Chains --> the components are connetcte through some builtin function is callled as chain 

        eg: - LLMChain is one of the example
                LLMChian(llm = llm , prompt = prompt)

                and then this chain is made to run 

6) Problem in LangCjain -> Firstly they have added the chains as they see new use cases . so too many chians . SO the codebase becomes larger . Also , for AI engg it becomes difficult to learn all these stuff . All components are developed individually hence we face problem in connecting the two components . 

7) So they created all the components , should be standarised and they must be connected seemlessly nad this was done by the help of runnables . 

8) Runnables :-
    1) Runnable is unit of work . 
    2) Every runnable has a work - input -> process -> output  
    3) Common interface in every runnable . eg: invoke() , batch() , stream()
    4) These runnables can be connected easily . and automatically the output of 1 act as a input od 2 . 
    5) and the workflow we created to create but connecting r1,2,3 and these also act as a runnable individually 
    6) Make a abstract class named Runnable . and we'll add our invoke method to it and all other classes must inherit runnable class and this runnable class method invoke must be overwritten byt the other classes. 

-------------------------------------------------

1)  Standardizing all the components so taht it will used to made life of AI eng easrier .  So then comes the  Runnable - a abstract class that is the parent to all the components 

2) Runnables --> Task specific runnables 
             --> Runnalbe primitivies 



3) RunnableSequence - we can use this for connecting runnables in sequence. 
        eg: prompt -> llm 


4) 
























