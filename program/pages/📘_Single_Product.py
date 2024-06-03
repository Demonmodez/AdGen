from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

def get_response(user_input):
    llm = Ollama(model="llama3")
    prompt_template = """
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are Aegen, an expert marketing strategist bot. You are working on a product's advertisement copy. You are chatting with a client who will provide some information about the product. Use the structure of the advertisement copy as follows:
    - Headline
    - Description
    - Call-to-Action

    Important things:
    - **Use markdown format (.md) to write the advertisement copy and use headings for the main structure**
    - **Directly give the advertisement copy without any chat.**<|eot_id|>

    <|start_header_id|>user<|end_header_id|>
    {input}<|eot_id|>
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"input": user_input})


st.set_page_config(page_title="AdGen", page_icon="🤖")
st.title("🤖 AdGen")
st.header("Single Product Advertisement Copy Generator")
user_query = st.text_input("Type your product's name here...")

single_section = st.empty()
if user_query and 'response' not in st.session_state:
    st.session_state["loading"] = True
    response = get_response(user_query)
    st.session_state['response'] = response
    st.session_state["loading"] = False

if 'response' in st.session_state:
    response = st.session_state['response']
    single_section.markdown(response)
    st.download_button('Download Advertisement Copy', response, 'download.md', disabled=st.session_state['loading'])