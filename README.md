# SEC-EDGAR_Analyis_App


- first merge and normalize your sec_edgar files for a ticker[e.g. for 3 tickers, 3 normalized + merged files]

- Put those inside documents directory in .txt format

- run python load_data.py [file splitting and creation of embeddings happens here]

- run main.py for gemini response

- The above steps were the backend

- To automate it all, run python app.py [it will create a interface for fast analysis]

