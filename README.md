# SEC-EDGAR_Analyis_App


- The first task is to process the data, Go to the data_processing directory, first run 1_extra_and_zip.py, and use the zip file to run 2_merge_and_normalize.py. Do this for all tickers separately[e.g. for 3 tickers, 3 merged files]

- Put those inside documents directory in .txt format

- run python load_data.py [uncomment API line, and put your gemini-pro API] (file splitting and creation of embeddings happens here)

- run main.py for Gemini response [uncomment API line, and put your gemini-pro API]

- The above steps were the backend

- To automate it all, run python app.py [it will create a interface for fast analysis]

