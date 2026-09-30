# Cohere Azure Workshops

Hands-on labs for using **Cohere Embed-V5-Pro** and **Cohere rerank-v4.0** via Microsoft Foundry to build semantic search and reranking applications.

## Labs


| Lab                            | Notebook                                     | Description                                                        |
| ------------------------------ | -------------------------------------------- | ------------------------------------------------------------------ |
| `lab-1a-embed-getting-started` | `lab-1a-embed-getting-started.ipynb`         | Introduction to text embeddings with Cohere on Azure               |
| `lab-1b-embed-business-graphs` | `lab-1b-embed-business-graphs.ipynb`         | Multimodal semantic search — index and query business graph images |
| `lab-2-rerank`                 | `lab-2-rerank-getting-started.ipynb`         | Semantic reranking — improve search relevance with Cohere Rerank   |
| `lab-2-rerank` (optional)      | `optional-lab-rerank_structured_data.ipynb`  | Reranking structured data                                          |
| `lab-3-parse`                  | `lab-3-parse-getting-started.ipynb`          | Document parsing — extract structured blocks from documents        |


> All notebooks use `cohere.ClientV2` and connect to Microsoft Foundry via the `/providers/cohere` endpoint path.

---

## Setup

### Option A — Local (Windows — Command Prompt or PowerShell)

```bash
git clone https://github.com/cohere-ai/cohere-azure-workshops.git
cd cohere-azure-workshops
pip install -r requirements.txt
copy .env.example .env
# edit .env with your Azure credentials
```

> **Lab 1b note (Windows):** Open `lab-1b-embed-business-graphs.ipynb` directly from the `lab-1-embed\` folder in VS Code so the Jupyter kernel's working directory is set to that folder. This ensures relative paths like `./dataset/` and `./chroma_db` resolve correctly.

> **Lab 3 note (Windows):** Open `lab-3-parse-getting-started.ipynb` directly from the `lab-3-parse\` folder in VS Code so the Jupyter kernel's working directory is set to that folder. This ensures the relative path `./sample_inputs/` resolves correctly.

### Option B — Local (macOS / Linux)

```bash
git clone https://github.com/cohere-ai/cohere-azure-workshops.git
cd cohere-azure-workshops
pip install -r requirements.txt
cp .env.example .env
# edit .env with your Azure credentials
```

### Option C — GitHub Codespaces

1. Click **Code → Codespaces → Create codespace on main**
2. Wait for the container to build and `pip install` to complete (~2 min)
3. Copy the env file and fill in your Azure credentials:
  ```bash
   cp .env.example .env
   # edit .env with your Azure endpoint URLs and API keys
  ```

## Microsoft Foundry — Endpoint URL Format

The correct `base_url` for each model uses the `**/providers/cohere`** path (visible on the deployment's **Details** page in the Microsoft Foundry portal under **Target URI**):


| Model type | Target URI pattern             | SDK `base_url`                                              |
| ---------- | ------------------------------ | ----------------------------------------------------------- |
| Embed      | `…/providers/cohere/v2/embed`  | `https://<resource>.services.ai.azure.com/providers/cohere` |
| Rerank     | `…/providers/cohere/v2/rerank` | `https://<resource>.services.ai.azure.com/providers/cohere` |
| Parse      | `…/providers/cohere/v2/parse`  | `https://<resource>.services.ai.azure.com/providers/cohere` |


> **Note:** `cohere.ClientV2` automatically appends `/v2/embed`, `/v2/rerank`, or `/v2/parse` to the `base_url`.

---

## Environment Variables


| Variable          | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `EMBED_MODEL`     | Cohere embed model name (e.g. `Embed-V5-Pro`)             |
| `EMBED_BASE_URL`  | Microsoft Foundry endpoint — up to `/providers/cohere`   |
| `EMBED_API_KEY`   | Azure API key for the embed deployment                   |
| `RERANK_MODEL`    | Cohere rerank model name (e.g. `Cohere-rerank-v4.0-pro`) |
| `RERANK_BASE_URL` | Microsoft Foundry endpoint — up to `/providers/cohere`   |
| `RERANK_API_KEY`  | Azure API key for the rerank deployment                  |
| `PARSE_MODEL`     | Cohere parse model name (e.g. `parse-v5.0`)              |
| `PARSE_BASE_URL`  | Microsoft Foundry endpoint — up to `/providers/cohere`   |
| `PARSE_API_KEY`   | Azure API key for the parse deployment                   |
| `CHROMA_DB_PATH`  | Path to ChromaDB storage (default: `./chroma_db`)        |


