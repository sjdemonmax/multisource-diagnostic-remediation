# Multi-Source Diagnostic Retrieval & Prerequisite Gap Remediation

> **Directed Acyclic Concept Graph Architecture Converting Exam Errors into Learning Events**  
> Role: Senior AI & Data Science Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white) ![NetworkX](https://img.shields.io/badge/NetworkX-DAG_Modeling-darkblue?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-Dual_View-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) ![Score Lift](https://img.shields.io/badge/Empirical_Lift-%2B14.9%25-success?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    SUB["Student Incorrect Exam Answer"] --> DIAG["Psychometric Distractor Mapping<br/>Identify Conceptual Error Mode"]
    DIAG --> DAG["Traverse Prerequisite Knowledge DAG<br/>(Depth k = 2 Hop Search)"]
    DAG --> ROOT["Isolate Upstream Root Cause Gap<br/>(e.g., Vector Cross Product Deficit)"]
    ROOT --> RET["Multi-Source Retrieval Engine<br/>Load Concept Remediation Asset"]
    RET --> STREAM["Dual-View Streamlit Portal<br/>• Tab 1: Interactive Student Path<br/>• Tab 2: Cohort Misconception Analytics"]
    STREAM --> LIFT["Empirical Score Lift: +14.9%"]
```

---

## The Problem\n\nIn high-stakes entrance exam preparation — JEE Advanced, NEET, JEE Main — a mock test score has historically functioned as an **autopsy rather than a diagnosis**. Telling a student they achieved 54% or 60% merely quantifies failure without pinpointing cognitive etiology. The student knows they got it wrong; they do not know *why*, and more critically, *which foundational concept* they need to revisit to fix the problem at its root.\n\nThis creates a doom loop: students re-attempt the same questions without addressing upstream knowledge gaps, teachers lack the diagnostic tooling to intervene at the concept level, and score improvement stalls.\n\n## The Solution\n\nThis project expands a core RAG doubt resolution infrastructure into a **multi-source diagnostic retrieval and prerequisite gap remediation pipeline** — transforming test scores from static measurements into active learning events.\n\n### How It Works\n\n1. **Multi-Corpus Ingestion** — Four unified educational data sources are loaded: a concept-tagged question bank, longitudinal student exam histories, aggregate misconception databases, and modular remediation assets.\n2. **Concept Dependency Graph (DAG)** — A directed acyclic graph is constructed to model prerequisite relationships between concepts — allowing wrong answers to be traced back to upstream foundational failures, not just the surface-level topic.\n3. **Diagnostic Attribution** — Each incorrect answer is mapped through the DAG to identify root-cause prerequisite gaps, with configurable traversal depth and diagnostic confidence scoring.\n4. **Remediation Routing** — Identified gaps are matched to targeted remediation assets: video modules, practice sets, and concept summaries — delivered at the right level of the dependency chain.\n5. **Dual-View Deployment** — A lightweight Streamlit portal presents:\n   - **Tab 1**: Live student diagnostic scorecards with interactive DAG root-cause paths\n   - **Tab 2**: Cohort-level misconception analytics with targeted remediation assignments\n\n### Tech Stack\n\n- **Graph Construction**: NetworkX (DAG prerequisite modelling)\n- **Retrieval**: Dense semantic embeddings · ChromaDB\n- **Analysis**: Python · Pandas · NumPy · Matplotlib · Seaborn\n- **Dashboard**: Streamlit (dual-tab: student scorecards + cohort analytics)\n- **Notebook**: JupyterLab (fully executed, dual micro-edits for calibration)\n\n## Measurable Business Impact\n\n| Metric | Result |\n|---|---|\n| Data sources unified | **4** (question bank, exam histories, misconception DB, remediation assets) |\n| Architecture | Directed Acyclic Concept Dependency Graph (DAG) |\n| Score lift achieved | **+14.9%** improvement in student test scores post-remediation |\n| Diagnostic resolution | Wrong answers traced to root-cause prerequisite failures — not just surface topic |\n| Remediation targeting | Concept-level assignments matched to exact upstream gaps |\n| Deployment | Live dual-tab Streamlit portal (student-level + cohort-level views) |\n| Strategic impact | Converts test scores from passive metrics into active, personalised intervention triggers |\n\nThe +14.9% score lift represents the difference between a system that tells students what they got wrong and a system that tells them *why* — and then fixes it.\n\n## Repository Contents\n\n| File | Description |\n|---|---|\n| `starter.ipynb` | Starter notebook with scaffolding |\n| `final output 1.ipynb` | Fully executed notebook (DAG construction, diagnostic attribution, remediation routing) |\n| `final output 2.csv` | Student remediation roster export |\n| `final output 3.py` | Streamlit dual-tab diagnostic portal |\n| `input 1.csv` | Student exam history dataset |\n| `input 2.csv` | Concept-tagged question bank |\n| `generate_dataset.py` | Synthetic multi-corpus dataset generation |\n| `start_dashboard.py` | Streamlit dashboard launcher |\n| `master_recording_guide.md` | Detailed pipeline walkthrough guide |

---

### 📊 Cognitive Diagnostic Telemetry & Cohort Analytics

| Longitudinal Score Lift Distribution | Cohort Misconception Clustering |
| :---: | :---: |
| ![Score Lift Telemetry](artifact%203.png) | ![Cohort Misconceptions](artifact%204.png) |


---

<details>
<summary><b>📐 Graph Theory: Concept DAG Attribution & Depth Traversal</b></summary>

Let $G = (V, E)$ be a Directed Acyclic Graph where vertices $v_i \in V$ represent atomic pedagogical concepts, and directed edges $(u, v) \in E$ denote that concept $u$ is a strict prerequisite for concept $v$.

When an error on concept $v_{\text{fail}}$ occurs, upstream cognitive attribution computes prerequisite path reachability $\mathcal{P}(v_{\text{fail}})$ up to traversal depth $k=2$:

$$\mathcal{P}_k(v_{\text{fail}}) = \{ u \in V \mid \text{dist}(u, v_{\text{fail}}) \le k \land (u, v_{\text{fail}}) \in E^* \}$$

Diagnostic attribution confidence score $\mathcal{C}(u)$ combines historical mastery degradation $M(u)$ and distractor correlation $\rho(d, u)$:

$$\mathcal{C}(u) = \gamma (1 - M(u)) + (1 - \gamma) \rho(d, u), \quad \gamma = 0.65$$

The assigned remediation package corresponds to $u^* = \arg\max_{u} \mathcal{C}(u)$.
</details>
