from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import pandas as pd
from stqdm import stqdm

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
st.header("Multiple Product Advertisement Copy Generator")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

csv_section = st.empty()

if uploaded_file is not None:
    csv_section.empty()
    if 'response' in st.session_state:
        del st.session_state['response']
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    selected_column = st.selectbox("Select the column for product name", df.columns)
    product_names = df[selected_column].tolist()
    generated_ads = []

    if st.button("Generate Ads"):
        progress_bar = st.progress(0)
        total_products = len(product_names)
        for i, product_name in stqdm(enumerate(product_names)):
            response = get_response(product_name)
            generated_ads.append(response)
            progress = (i + 1) / total_products
            progress_bar.progress(progress)
            
        df_ads = pd.DataFrame({
            'Product Name': product_names,
            'Advertisement Copy': generated_ads
        })

        st.success("Advertisement generation complete!")

        # Display the generated ads dataframe
        csv_section.dataframe(df_ads)
        st.session_state['df_ads'] = df_ads

    # for product_name in product_names:
    #     response = get_response(product_name)
    #     generated_ads.append(response)

# if 'df_ads' in st.session_state:
#     df_ads = st.session_state['df_ads']
#     csv = df_ads.to_csv(index=False)
#     st.download_button('Download CSV', csv, 'download.csv', file_name='generated_ads.csv', mime='text/csv')

# if 'response' in st.session_state:
#     response = st.session_state['response']
#     st.markdown(response)
#     st.download_button('Download Advertisement Copy', response, 'download.md', disabled=st.session_state['loading'])
