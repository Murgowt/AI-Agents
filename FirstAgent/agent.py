from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver
model = OllamaLLM(model = 'llama3.2' )

template = """
                You are an 15th centery english poet who is answering questions about a pizza restaurant in a poetic manner.
                Here are some relevant reviews: {reviews}
                Here is the question to answer:{question}
           """

prompt = ChatPromptTemplate.from_template(template)
chain = prompt  | model

for i in range(10):
    question = input("What do you want? \n")
    if(question == 'q'):
        break
    reviews = retriver.invoke(question)
    result = chain.invoke({
        "reviews":reviews,
        "question":question
    })

    print(result)
