<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e1b4b,50:7c3aed,100:0d9488&height=220&section=header&text=MCDM%20Algorithms&fontSize=42&fontColor=ffffff&fontAlignY=50&animation=fadeIn" />
</div>

---

# MCDM Algorithms: Multi-Criteria Decision Making code implementations

A curated collection of Multi-Criteria Decision Making (MCDM) algorithm implementations, developed as part of the Decision Making with Multiple Criteria course. The repository includes both classical decision-making methods (AHP, TOPSIS, ANP) and a real-world case study applying MCDM to a network science problem.

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Matrix_Computation-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-Interactive_Interfaces-4B8BBE?style=flat)](https://www.pysimplegui.org/)
[![MCDM](https://img.shields.io/badge/Domain-Multi_Criteria_Decision_Making-0284C7?style=flat)](#)
[![License](https://img.shields.io/badge/License-MIT-4B5563?style=flat)](https://opensource.org/licenses/MIT)

</div>

## Abstract

Multi-Criteria Decision Making (MCDM) provides a formal framework for evaluating and ranking alternatives when multiple, often conflicting, criteria must be considered simultaneously. This repository brings together four MCDM implementations developed to explore the theory and practical application of these methods: the Analytic Hierarchy Process (AHP) for hierarchical pairwise comparisons, TOPSIS for distance-based ranking, the Analytic Network Process (ANP) for modeling interdependent criteria through supermatrix computation, and a real-world case study applying TOPSIS to rank community detection algorithms in complex networks.

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Methods Comparison](#methods-comparison)
4. [Technologies](#technologies)
5. [Getting Started](#getting-started)
6. [License](#license)
7. [Author](#author)
8. [Support](#support)

# Overview

Each module in this repository is a self-contained implementation of an MCDM method, complete with its own interactive interface (where applicable) and documentation. The first three modules (AHP, TOPSIS, ANP) are general-purpose decision-support tools that accept user-defined criteria, sub-criteria, and alternatives at runtime. The fourth module (TOPSIS-Community-Detection-Algorithms) is a applied case study that uses TOPSIS to solve a concrete decision problem: ranking community detection algorithms in complex networks based on performance, runtime, resource consumption, and scalability.

# Repository Structure

```text
DSS_Algorithms
│
├── AHP/
│
├── TOPSIS/
│
├── ANP/
│
├── TOPSIS-Community-Detection-Algorithms/
│
└── README.md
```

# Methods Comparison

| Module | Method | Category | Description |
|:---|:---|:---|:---|
| AHP | Analytic Hierarchy Process | Hierarchical MCDM | Ranks alternatives through pairwise comparisons across a hierarchy of criteria and sub-criteria |
| TOPSIS | Technique for Order of Preference by Similarity to Ideal Solution | Distance-based MCDM | Ranks alternatives by their relative closeness to an ideal and a negative-ideal solution |
| ANP | Analytic Network Process | Network-based MCDM | Extends AHP by modeling interdependencies between criteria and alternatives through supermatrix computation |
| TOPSIS-Community-Detection-Algorithms | Applied TOPSIS Case Study | Applied MCDM | Applies TOPSIS to rank community detection algorithms in complex networks based on real evaluation criteria |

# Technologies

* **Python** — core implementation language across all modules
* **NumPy** — matrix operations, normalization, and numerical computation
* **PySimpleGUI** — interactive graphical interfaces for the AHP, TOPSIS, and ANP modules
* **Tabulate** — formatted tabular output for decision matrices and ranking results

# Getting Started

Each module is self-contained and includes its own README with detailed installation and usage instructions. To explore a specific method:

```bash
git clone https://github.com/ParmidaGh/DSS_Algorithms.git
cd DSS_Algorithms/<module-name>
```

Replace `<module-name>` with `AHP`, `TOPSIS`, `ANP`, or `TOPSIS-Community-Detection-Algorithms`, then follow the instructions in that module's README.

---

# License

This project is licensed under the MIT License.

---

## Author

**Parmida Ghamari**
M.Sc. Student, University of Tehran
Research Assistant @ Social Networks Lab

**Research Interests:** Multi-Criteria Decision Making (MCDM), Decision Support Systems, Analytic Network Process, Complex Networks, Community Detection, Operations Research

📧 [Parmida.ghamari@gmail.com](mailto:Parmida.ghamari@gmail.com) | 💻 [github.com/ParmidaGh](https://github.com/ParmidaGh) | 💼 [www.linkedin.com/in/parmida-ghamari](https://www.linkedin.com/in/parmida-ghamari)

---

# Support

If you find this repository useful, consider giving it a star ⭐️

---

<p align="center">
Built using Python, NumPy, and PySimpleGUI
</p>
