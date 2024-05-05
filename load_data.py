import os
import argparse

from tqdm import tqdm

import chromadb
from chromadb.utils import embedding_functions
import google.generativeai as genai
from llama_index.core.node_parser import SentenceSplitter
import os
import sys
#Uncomment below line
#os.environ["GOOGLE_API_KEY"]=""
def split_large_text(text, max_length=9500):
    """
    Splits a large text into smaller parts, each with a length less than max_length.
    This simple function breaks the text at the last space before max_length.
    """
    parts = []
    while len(text) > max_length:
        # Find the last space within the max_length boundary to split
        place_to_split = text.rfind(' ', 0, max_length)
        if place_to_split == -1:  # No spaces found, force split at max_length
            place_to_split = max_length
        parts.append(text[:place_to_split])
        text = text[place_to_split:].strip()
    parts.append(text)
    return parts

def main(
    documents_directory: str = "documents",
    collection_name: str = "documents_collection",
    persist_directory: str = ".",
    specific_file: str = None
) -> None:
    documents = []
    metadatas = []
    files = os.listdir(documents_directory)

    if specific_file:
        files = [specific_file] if specific_file in files else []

    for filename in files:
        with open(f"{documents_directory}/{filename}", "r") as file:
            for line_number, line in enumerate(tqdm((file.readlines()), desc=f"Reading {filename}"), 1):
                line = line.strip()
                if sys.getsizeof(line) > 9500:
                    line = split_large_text(line)
                if len(line) == 0:
                    continue
                documents.append(line)
                metadatas.append({"filename": filename, "line_number": line_number})

    client = chromadb.PersistentClient(path=persist_directory)

    google_api_key = os.environ.get("GOOGLE_API_KEY")

    embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
        api_key=google_api_key
    )

    collection = client.get_or_create_collection(
        name=collection_name, embedding_function=embedding_function
    )

    count = collection.count()
    ids = [str(i) for i in range(count, count + len(documents))]

    for i in tqdm(range(0, len(documents), 1), desc="Adding documents", unit_scale=1):
        collection.add(
            ids=ids[i : i + 1],
            documents=documents[i : i + 1],
            metadatas=metadatas[i : i + 1]
        )

    new_count = collection.count()
    print(f"Added {new_count - count} documents")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load documents from a directory into a Chroma collection"
    )

    parser.add_argument("--data_directory", type=str, default="documents", help="The directory where your text files are stored")
    parser.add_argument("--collection_name", type=str, default="documents_collection", help="The name of the Chroma collection")
    parser.add_argument("--persist_directory", type=str, default="chroma_storage", help="The directory where you want to store the Chroma collection")
    parser.add_argument("--specific_file", type=str, default=None, help="Specific file to load into the collection")

    args = parser.parse_args()
    main(
        documents_directory=args.data_directory,
        collection_name=args.collection_name,
        persist_directory=args.persist_directory,
        specific_file=args.specific_file
    )
