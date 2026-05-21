from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import os
import cohere
import chromadb
import gradio as gr
from PIL import Image

# Paths are relative to this script so the app works regardless of working directory
_HERE = os.path.dirname(os.path.abspath(__file__))

CHROMA_DB_PATH = os.environ.get('CHROMA_DB_PATH', os.path.join(_HERE, 'chroma_db'))
COLLECTION_NAME = 'Business_Graphs'
MODEL = os.environ['EMBED_MODEL']
IMAGES_FOLDER = os.path.join(_HERE, 'dataset')
TOP_K = 5

co = cohere.Client(
    base_url=os.environ['EMBED_BASE_URL'],
    api_key=os.environ['EMBED_API_KEY'], 
    timeout=300)
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_collection(name=COLLECTION_NAME)


def search(query: str):
    if not query.strip():
        return []

    result = co.embed(
        texts=[query],
        model=MODEL,
        input_type='search_query',
        embedding_types=['float']
    )
    query_embedding = result.embeddings.float_[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=['metadatas', 'distances']
    )

    images = []
    for metadata in results['metadatas'][0]:
        filepath = os.path.join(IMAGES_FOLDER, metadata['filename'])
        if os.path.exists(filepath):
            images.append(Image.open(filepath))
    return images


demo = gr.Interface(
    fn=search,
    inputs=gr.Textbox(
        placeholder="e.g. bar chart showing quarterly revenue growth",
        label="Search Query"
    ),
    outputs=gr.Gallery(
        label=f"Top {TOP_K} Matching Business Graphs",
        columns=3,
        height="auto"
    ),
    title="Business Graph Search",
    description=(
        "Search through indexed business graphs using natural language. "
        "Powered by Cohere embed-v4.0 and ChromaDB.\n\n"
        "**Run `index_dataset.ipynb` first to build the index before searching.**"
    ),
    examples=[
        ["bar chart showing quarterly revenue"],
        ["pie chart with market share breakdown"],
        ["line graph showing growth over time"],
        ["stacked bar chart comparing regions"],
        ["scatter plot with trend line"],
    ]
)

if __name__ == "__main__":
    # server_name="0.0.0.0" is required for GitHub Codespaces port forwarding.
    # Gradio will still be accessible via localhost when running locally.
    demo.launch(server_name="0.0.0.0", server_port=7860)
