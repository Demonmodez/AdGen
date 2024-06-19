# AdGen

AdGen is an innovative application designed to simplify and streamline the creation of advertisement scripts. The application utilizes advanced language models to generate compelling ad copy based on user-provided product information. It supports both individual product advertisements and bulk ad generation through CSV uploads.

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Single Product Page](#single-product-page)
   - [Multiple Product Page](#multiple-product-page)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- Generate ad scripts for individual products.
- Bulk ad generation for multiple products via CSV upload.
- Download generated scripts in markdown (.md) or CSV (.csv) format.
- User-friendly interface with Streamlit.

## Technology Stack

- **Programming Language:** Python with LangChain library
- **Language Model:** LLaMA3 via the Ollama library
- **Web Framework:** Streamlit

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Demonmodez/AdGen.git
   cd adgen
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   cd program
   streamlit run 🏠_Home.py
   ```

## Usage

### Single Product Page

1. **Navigate to the Single Product Page:**
   - Click on the "Single Product" button on the homepage.
2. **Enter Product Information:**
   - Input the product name into the designated field.
3. **Generate Ad Script:**
   - Press enter or click the "Generate" button.
   - The ad script will be generated and displayed below the input field.
4. **Download Ad Script:**
   - Click the "Download" button to save the ad script as a markdown (.md) file.

### Multiple Product Page

1. **Navigate to the Multiple Product Page:**
   - Click on the "Multiple Product" button on the homepage.
2. **Upload CSV File:**
   - Click the "Upload CSV" button to select and upload your CSV file containing product names.
3. **Select Product Name Column:**
   - Choose the column that represents the product names from the dropdown menu.
4. **Generate Ad Scripts:**
   - Click the "Generate Ads" button.
   - The generated ad scripts will be displayed in a table below the upload section.
5. **Download Ad Scripts:**
   - To download the results, click the "Download" button on the top right corner of the table to save the ad scripts as a CSV (.csv) file.