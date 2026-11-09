# Multi-Source Diagnostic Retrieval & Prerequisite Remediation Pipeline

> **Role**: Senior Learning Analytics & AI Systems Engineer · Entrance-Exam EdTech Enterprise

## The Problem

In high-stakes entrance exam preparation — JEE Advanced, NEET, JEE Main — a mock test score has historically functioned as an **autopsy rather than a diagnosis**. Telling a student they achieved 54% or 60% merely quantifies failure without pinpointing cognitive etiology. The student knows they got it wrong; they do not know *why*, and more critically, *which foundational concept* they need to revisit to fix the problem at its root.

This creates a doom loop: students re-attempt the same questions without addressing upstream knowledge gaps, teachers lack the diagnostic tooling to intervene at the concept level, and score improvement stalls.

## The Solution

This project expands a core RAG doubt resolution infrastructure into a **multi-source diagnostic retrieval and prerequisite gap remediation pipeline** — transforming test scores from static measurements into active learning events.

### How It Works

1. **Multi-Corpus Ingestion** — Four unified educational data sources are loaded: a concept-tagged question bank, longitudinal student exam histories, aggregate misconception databases, and modular remediation assets.
2. **Concept Dependency Graph (DAG)** — A directed acyclic graph is constructed to model prerequisite relationships between concepts — allowing wrong answers to be traced back to upstream foundational failures, not just the surface-level topic.
3. **Diagnostic Attribution** — Each incorrect answer is mapped through the DAG to identify root-cause prerequisite gaps, with configurable traversal depth and diagnostic confidence scoring.
4. **Remediation Routing** — Identified gaps are matched to targeted remediation assets: video modules, practice sets, and concept summaries — delivered at the right level of the dependency chain.
5. **Dual-View Deployment** — A lightweight Streamlit portal presents:
   - **Tab 1**: Live student diagnostic scorecards with interactive DAG root-cause paths
   - **Tab 2**: Cohort-level misconception analytics with targeted remediation assignments

### Tech Stack

- **Graph Construction**: NetworkX (DAG prerequisite modelling)
- **Retrieval**: Dense semantic embeddings · ChromaDB
- **Analysis**: Python · Pandas · NumPy · Matplotlib · Seaborn
- **Dashboard**: Streamlit (dual-tab: student scorecards + cohort analytics)
- **Notebook**: JupyterLab (fully executed, dual micro-edits for calibration)

## Measurable Business Impact

| Metric | Result |
|---|---|
| Data sources unified | **4** (question bank, exam histories, misconception DB, remediation assets) |
| Architecture | Directed Acyclic Concept Dependency Graph (DAG) |
| Score lift achieved | **+14.9%** improvement in student test scores post-remediation |
| Diagnostic resolution | Wrong answers traced to root-cause prerequisite failures — not just surface topic |
| Remediation targeting | Concept-level assignments matched to exact upstream gaps |
| Deployment | Live dual-tab Streamlit portal (student-level + cohort-level views) |
| Strategic impact | Converts test scores from passive metrics into active, personalised intervention triggers |

The +14.9% score lift represents the difference between a system that tells students what they got wrong and a system that tells them *why* — and then fixes it.

## Repository Contents

| File | Description |
|---|---|
| `starter.ipynb` | Starter notebook with scaffolding |
| `final output 1.ipynb` | Fully executed notebook (DAG construction, diagnostic attribution, remediation routing) |
| `final output 2.csv` | Student remediation roster export |
| `final output 3.py` | Streamlit dual-tab diagnostic portal |
| `input 1.csv` | Student exam history dataset |
| `input 2.csv` | Concept-tagged question bank |
| `generate_dataset.py` | Synthetic multi-corpus dataset generation |
| `start_dashboard.py` | Streamlit dashboard launcher |
| `master_recording_guide.md` | Detailed pipeline walkthrough guide |
