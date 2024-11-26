# app.py

from dotenv import load_dotenv
from load_document import loader
from rag_chain import create_rag_chain
from text_split import split_documents
from vector_store import create_vector_store
import openlit

openlit.init(
    otlp_endpoint="http://127.0.0.1:4318"
)
load_dotenv()

def main():
    source = "./movies_processed.csv"
    question = "What is a good animated movie similar to Aladdin?"
    chunk_size = 1000
    chunk_overlap = 200
    model_name="sentence-transformers/all-mpnet-base-v2"

    documents = loader(source)
    chunks = split_documents(documents, chunk_size, chunk_overlap)
    retriever = create_vector_store(chunks, model_name)
    rag_chain = create_rag_chain(documents, retriever)
    answer = rag_chain.invoke(question)
    print(f"\nAnswer:{answer}")


    # source = input("Enter the path to the document (PDF, csv, or image): ")
    # documents = process_document(source)
    # while True:
    #     question = input("Ask a question about the document (or type 'quit' to quit): ")
    #     if question.lower() == "quit":
    #         break

    #     # Create rag chain
    #     rag_chain = create_rag_chain(documents)
    #     answer = rag_chain.invoke(question)

    #     # # Print only the answer
    #     # answer_start_index = answer.find("Answer:")
    #     # answer_content = answer[answer_start_index:].strip()
    #     # print(answer_content)   

    #     print(f"\nAnswer:{answer}")

if __name__ == "__main__":
    main()