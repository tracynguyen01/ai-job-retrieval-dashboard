# 🚀 AI Job Retrieval & Optimization Dashboard

This project explores how different AI search and optimization algorithms (BFS, A*, and Genetic Algorithm) can be applied to retrieve and rank AI-related job postings from large-scale datasets.

👉 The goal is to evaluate trade-offs between runtime efficiency and ranking quality across datasets.

---
## Problem

Given thousands of job postings, how can we efficiently identify high-quality AI-related jobs while balancing multiple criteria such as:

* Salary
* Experience level
* Location
* Work type
* Data completeness

---
## 📂 Project Structure

ai-job-retrieval-dashboard/
│
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Dependencies
├── results/                # Processed results (CSV)
│   ├── algorithm_comparison.csv
│   ├── ga_convergence_dataset1.csv
│   └── ga_convergence_dataset2.csv
│
├── notebooks/              # Original analysis notebook
├── reports/                # Report PDF
└── assets/                 # Images for README

---
## 📊 Dashboard Preview

![Dashboard](assets/dashboard-preview.png)

## 🌐 Live Dashboard

👉 https://baotran-11-ai-job-retrieval-dashboard-app-gq23iv.streamlit.app/

---
## ⚙️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

---
## Methods

Three approaches were implemented and compared:

* **Breadth-First Search (BFS)**
  Systematic exploration of all possible filtering combinations

* **A***
  Heuristic-guided search to prioritize promising job subsets

* **Genetic Algorithm (GA)**
  Evolutionary optimization for multi-objective decision making

---

## Datasets

* **Dataset 1**: ~19,000 job postings (smaller, older dataset)
* **Dataset 2**: ~123,000 job postings (large-scale, modern dataset)

---
## 🧩 Key Features

- Interactive dashboard built with Streamlit
- Compare BFS, A*, and Genetic Algorithm performance
- Dynamic dataset selection
- GA convergence visualization across datasets
- Insight-driven analysis for AI job market trends

## 📊 Key Insights

- A* provides the best balance between runtime and ranking quality
- Genetic Algorithm converges quickly but shows limited improvement after early generations
- Larger datasets enable more reliable evaluation of algorithm performance

---
## Industry Insights

Analysis of job trends reveals:

* Shift from general software roles → specialized AI roles
* Increasing demand for:

  * Machine Learning
  * Deep Learning
  * Python & AI frameworks (TensorFlow, PyTorch)
  * Cloud & distributed systems

---

## Future Work

* Build interactive dashboard using Streamlit
* Improve GA diversity to avoid premature convergence
* Enhance heuristic design for A*

---
## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

---
## 📌Author

```md
## 👤 Author

Ngoc Bao Tran Nguyen  
Data Science & AI Portfolio Project

