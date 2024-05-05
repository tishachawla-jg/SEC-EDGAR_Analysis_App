# SEC-EDGAR Analysis App :round_pushpin: 


# Workflow

## **Overview**

This repository contains a Retrieval-augmented generation (RAG) app for a streamlined workflow for processing, merging, normalizing, and analyzing SEC_EDGAR  data with Large Language Models [LLM API used - Gemini pro model]. The final step involves using Streamlit to visualize the LLM results for quicker financial insights to better interpret the SEC_EDGAR tickers employed [MSFT, AAPL, GOOGL].

**Demo [SEE HERE] :link:**-https://drive.google.com/file/d/1eMftidtmhJIFWohNr3so_RnMjGIrgeee/view?usp=sharing

**Output 1 :chart_with_downwards_trend:-**

<img width="370" alt="image" src="https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App/assets/76087547/bb8bc956-fb13-47ed-b19e-07e559410b17">

**Output 2 :chart_with_upwards_trend: -**

<img width="330" alt="image" src="https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App/assets/76087547/0173c863-ab4a-4410-8c44-5bff84fa06ce">
<img width="450" alt="image" src="https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App/assets/76087547/61151799-c65d-4cf9-b359-63132ed530d6">
<img width="322" alt="image" src="https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App/assets/76087547/a044385c-551b-4904-8e0a-a7d3db54a8cd">

## **Tech Stack :computer:**

- **Python**: Our primary programming language for application development.

- **Gemini-Pro**: A comprehensive data analysis and insights LLM suited for our RAG app. Offers free access up to a certain number of requests. Additionally, I explored other open-source LLMs like StabilityAI, Camel-AI, and Zephyr 7B. Gemini-Pro provides versatile output formats, including structured JSON/tabular data and well-tuned text analysis, making it highly suitable for our app.

- **Plotly**: Plotly provides interactive and customizable visualizations for our app after converting .json responses to a dataframe.

- **Streamlit**: Enables easy deployment and offers robust visualization features.

**NOTE** - Text Analysis of LLM can be accessed from the pdf 'INSIGHTS WITH TEXT RESPONSES'.

## **Backend Process :file_folder:**

![image](https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App/assets/76087547/64e2ff1a-215e-450b-8687-d7a855d2d2f5)


1. **Data Extraction and Zipping:**
   - **Go to the `data_processing` directory.**
   - **Run:** `1_extra_and_zip.py`
   - **Output:** This will create a zip file for each ticker.

2. **Merge and Normalize:**
   - **Go to the `data_processing` directory.**
   - **Run:** `2_merge_and_normalize.py` using the zip file created in step 1. Here we first convert to .json then .txt for faster processing of embeddings.

- **Repeat:** Perform step 1 and 2 for each ticker separately.
- **Output:** Generates merged and cleaned files that are ready for analysis.

4. **Store Processed Files:**
   - **Save:** Place the merged files inside the `documents` directory in `.txt` format.

5. **Load Data and Create Embeddings:**
   - **Run:** `load_data.py`
   - **Uncomment:** The API line, and provide your `gemini-pro` API key.
   - **Note:** This step involves file splitting and the creation of embeddings.

6. **Analyze Data with Gemini:**
   - **Run:** `main.py`
   - **Uncomment:** The API line, and provide your `gemini-pro` API key.

7. **Automation with Streamlit:**
   - **Run:** `app.py` using Streamlit.
   - **Output:** This creates an interface for fast analysis.

## **Getting Started**

- **Clone the Repository:**
  ```bash
  git clone https://github.com/tishachawla-jg/SEC-EDGAR_Analyis_App.git

**Install Dependencies:**
pip install -r requirements.txt

**Run app locally:**
streamlit run app.py

*If you wish to contribute to this project, please create a pull request or raise an issue to discuss improvements.*

**NOTE TO APP USERS - Make sure to cross check the answers for potential hallucinations!!!**

*Referenes -* 
- **https://github.com/chroma-core/chroma/tree/main/examples/gemini**
- **https://ai.google.dev/gemini-api/docs/get-started/python**

