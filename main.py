import argparse
import os
from typing import List

import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions
import os
os.environ["GOOGLE_API_KEY"]="AIzaSyBJ2q-LD03Dy6aVQ1AQZp8HMKiWhmTkKoY"

model = genai.GenerativeModel("gemini-pro")


def build_prompt(query: str, context: List[str]) -> str:
    """
    Builds a prompt for the LLM. #

    This function builds a prompt for the LLM. It takes the original query,
    and the returned context, and asks the model to answer the question based on
    on what's in the context, not what's in its weights.

    Args:
    query (str): The original query.
    context (List[str]): The context of the query, returned by embedding search.

    Returns:
    A prompt for the LLM (str).
    """

    base_prompt = {
        "content": "I am going to ask you a question, which I would like you to answer"
        " based mostly on the provided context and  external knowledge if no direct context is there."
        "Only provide response in text form as analyis or json format only [for json response instructions : with proper string headers/columns(with  metric like %, billion etc) and all numerical values/records/rows (dont put billion, dollor sign etc) (if table is there)] not both, no the reponse format"
        'json format : { "X title": ["x1", "x2", "x3", ...], "Y title": ["y1", "y2", "y3", ...] }'
        #"text format : Break your answer up into nicely readable paragraphs",
    }
    user_prompt = {
        "content": f" The question is '{query}'. Here is the context you have but incase no direct context is there get help of other external knowledge:"
        f'{(" ").join(context)}',
    }

    # combine the prompts to output a single prompt string
    system = f"{base_prompt['content']} {user_prompt['content']}"

    return system


def get_gemini_response(query: str, context: List[str]) -> str:
    """
    Queries the Gemini API to get a response to the question.

    Args:
    query (str): The original query.
    context (List[str]): The context of the query, returned by embedding search.

    Returns:
    A response to the question.
    """

    response = model.generate_content(build_prompt(query, context))

    return response.text


def main(
    collection_name: str = "documents_collection", persist_directory: str = ".", specific_file: str = None
) -> None:
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    client = chromadb.PersistentClient(path=persist_directory)

    embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
        api_key=google_api_key
    )

    collection = client.get_collection(name=collection_name, embedding_function=embedding_function)

    while True:
        query = input("Query: ")
        if not query:
            print("Please enter a question. Ctrl+C to Quit.\n")
            continue
        print("\nThinking...\n")

        results = collection.query(query_texts=[query], n_results=5, include=["documents", "metadatas"])
        sources = "\n".join(
            [
                f"{result['filename']}: line {result['line_number']}"
                for result in results["metadatas"][0]
            ]
        )

        response = get_gemini_response(query, results["documents"][0])
        print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Chroma collections with Gemini")
    parser.add_argument("--persist_directory", type=str, default="chroma_storage", help="Directory for Chroma storage")
    parser.add_argument("--collection_name", type=str, default="documents_collection", help="Chroma collection name")
    parser.add_argument("--specific_file", type=str, default=None, help="Specific file to query in the collection")

    args = parser.parse_args()
    main(collection_name=args.collection_name, persist_directory=args.persist_directory, specific_file=args.specific_file)
