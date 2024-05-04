# SEC-EDGAR_Analyis_App


# Workflow

## **Overview**

This repository contains a streamlined workflow for processing, merging, normalizing, and analyzing data with the Large Language Model [Gemini pro]. The final step involves using Streamlit to visualize results for quicker financial insights of SEC_EDGAR tickers.

## **Backend Process**

1. **Data Extraction and Zipping:**
   - **Go to the `data_processing` directory.**
   - **Run:** `1_extra_and_zip.py`
   - **Output:** This will create a zip file for each ticker.

2. **Merge and Normalize:**
   - **Go to the `data_processing` directory.**
   - **Run:** `2_merge_and_normalize.py` using the zip file created in step 1.

- **Repeat:** Perform this step for each ticker separately.
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
  git clone https://github.com/your-username/your-repository.git

**Install Dependencies:**
pip install -r requirements.txt

**Run app locally:**
streamlit run app.py

If you wish to contribute to this project, please create a pull request or raise an issue to discuss improvements.



