# AI Job Retrieval & Optimization Dashboard

This project explores how different AI search and optimization algorithms can be applied to retrieve and rank AI-related job postings from large-scale datasets.

## Problem

Given thousands of job postings, how can we efficiently identify high-quality AI-related jobs while balancing multiple criteria such as:

* Salary
* Experience level
* Location
* Work type
* Data completeness

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

## Key Results

### Algorithm Performance

* BFS and A* achieve the highest ranking quality on smaller datasets
* Genetic Algorithm is significantly faster and more memory-efficient on large datasets
* For large datasets, all methods converge to similar solution quality

### Scalability Insight

* BFS and A* do not scale well due to exponential growth
* GA provides stable performance across dataset sizes

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

## Tech Stack

* Python
* Search Algorithms (BFS, A*)
* Genetic Algorithm
* Data Analysis
* Google colab Notebook

---

## Project Structure

```
ai-job-retrieval-dashboard/
│
├── notebooks/
│   └── AT1_analysis.ipynb
│
├── reports/
│   └── AT1_report.pdf
│
├── README.md
```

---

## Future Work

* Build interactive dashboard using Streamlit
* Improve GA diversity to avoid premature convergence
* Enhance heuristic design for A*

---

## Author

Ngoc Bao Tran Nguyen

