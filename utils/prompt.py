from langchain.prompts import PromptTemplate

def get_prompt_template():
    template = "Translate the following English text to Korean: {text}"
    return PromptTemplate(template=template, input_variables=["text"])