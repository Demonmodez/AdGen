from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import pandas as pd
from stqdm import stqdm


st.set_page_config(page_title="AdGen", page_icon="🤖")
st.title("🤖 AdGen")

description = """
### Welcome to AdGen: 


Unlock the potential of your products with AdGen, the revolutionary tool designed to make ad creation effortless. Whether you're looking to promote a single product or an entire catalog, AdGen has the perfect solution for you.

#### How to Get Started:

1. **Choose Your Ad Generation Mode:**
   - **Single Product Page:** Ideal for generating advertisement copy for individual products. Start by clicking on the "Single Product" button to enter the product name manually.
   - **Multiple Product Page:** Perfect for businesses with multiple products. Select the "Multiple Product" button to upload a CSV file containing your product names and let AdGen handle the rest.

2. **Generate Your Ads:**
   - On the **Single Product Page**, fill in the product name. Press enter to generate the advertisement copy. AdGen will instantly create a tailored ad script for you. The generated ad will appear below the input field. You can then download the result in a markdown (.md) file.
   - On the **Multiple Product Page**, upload your CSV file with product names. Choose which column represents the product name. Click the "Generate Ads" button and AdGen will process the list and generate individualized ad scripts for each product, saving you time and effort. The results will be displayed in a table below the upload section. To download the generated ads in a CSV (.csv) file, click the download button on the top right corner of the table.

3. **Deploy and Watch Your Business Grow:**
   Use the finalized ad scripts across your marketing platforms, from Instagram and YouTube to e-commerce sites like Shopee. Experience increased engagement and drive more sales with compelling advertisements crafted effortlessly by AdGen.

#### Why Choose AdGen?

- **Efficiency:** Streamline your ad creation process with quick and easy script generation.
- **Versatility:** Produce ads suitable for various platforms, ensuring consistent branding and messaging.
- **User-Friendly:** Accessible to users of all skill levels, from novice marketers to experienced professionals.

Join the AdGen community today and revolutionize the way you create advertisements. Click on the "Single Product" or "Multiple Product" button to begin generating high-quality ad scripts that captivate and convert."""

st.markdown(description)