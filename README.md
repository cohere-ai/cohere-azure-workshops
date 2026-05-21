# Cohere Azure Workshops

Hands-on labs for using **Cohere embed-v4.0** and **Cohere rerank-v4.0** via Azure AI Foundry to build semantic search and reranking applications.

## Labs


| Lab                           | Notebook                                     | Description                                                        |
| ----------------------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| `lab-2-embed-getting-started` | `lab-2-embed.ipynb`                          | Introduction to text embeddings with Cohere on Azure               |
| `lab-3-embed-business-graphs` | `lab-3-embed.ipynb`                          | Multimodal semantic search — index and query business graph images |
| `lab-4-rerank`                | `lab-4-rerank-getting-started.ipynb`         | Semantic reranking — improve search relevance with Cohere Rerank   |
| `lab-4-rerank` (optional)     | `optional-lab-rerank_wikipedia_search.ipynb` | Reranking over Wikipedia search results                            |
| `lab-4-rerank` (optional)     | `optional-lab-ranking_structured_data.ipynb` | Reranking structured data                                          |


> All notebooks use `cohere.ClientV2` and connect to Azure AI Foundry via the `/providers/cohere` endpoint path.

---

## Setup

### Option A — GitHub Codespaces (recommended for workshops)

1. Click **Code → Codespaces → Create codespace on main**
2. Wait for the container to build and `pip install` to complete (~2 min)
3. Copy the env file and fill in your Azure credentials:
  ```bash
   cp .env.example .env
   # edit .env with your Azure endpoint URLs and API keys
  ```

### Option B — Local (macOS / Linux)

```bash
git clone https://github.com/cohere-ai/cohere-azure-workshops.git
cd cohere-azure-workshops
pip install -r requirements.txt
cp .env.example .env
# edit .env with your Azure credentials
```

---

## Lab 2 — Business Graph Search

### Step 1: Index the images

Open and run `**lab-3-embed-business-graphs/lab-3-embed.ipynb**` to embed the dataset and store vectors in ChromaDB.

### Step 2: Launch the search UI

```bash
python lab-3-embed-business-graphs/search_ui.py
```

In Codespaces, the Gradio UI opens automatically in the browser via port forwarding on port **7860**.  
Locally, open [http://localhost:7860](http://localhost:7860).

---

## Azure AI Foundry — Endpoint URL Format

The correct `base_url` for each model uses the `**/providers/cohere`** path (visible on the deployment's **Details** page in the Azure AI Foundry portal under **Target URI**):


| Model type | Target URI pattern             | SDK `base_url`                                              |
| ---------- | ------------------------------ | ----------------------------------------------------------- |
| Embed      | `…/providers/cohere/v2/embed`  | `https://<resource>.services.ai.azure.com/providers/cohere` |
| Rerank     | `…/providers/cohere/v2/rerank` | `https://<resource>.services.ai.azure.com/providers/cohere` |


> **Note:** `cohere.ClientV2` automatically appends `/v2/embed` or `/v2/rerank` to the `base_url`.

---

## Environment Variables


| Variable          | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `EMBED_MODEL`     | Cohere embed model name (e.g. `embed-v-4-0`)             |
| `EMBED_BASE_URL`  | Azure AI Foundry endpoint — up to `/providers/cohere`    |
| `EMBED_API_KEY`   | Azure API key for the embed deployment                   |
| `RERANK_MODEL`    | Cohere rerank model name (e.g. `Cohere-rerank-v4.0-pro`) |
| `RERANK_BASE_URL` | Azure AI Foundry endpoint — up to `/providers/cohere`    |
| `RERANK_API_KEY`  | Azure API key for the rerank deployment                  |
| `CHROMA_DB_PATH`  | Path to ChromaDB storage (default: `./chroma_db`)        |


