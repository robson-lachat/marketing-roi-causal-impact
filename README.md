# 📈 Marketing ROI & Causal Impact Pipeline

![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)
![DuckDB](https://img.shields.io/badge/database-DuckDB-orange.svg)
![Package Manager](https://img.shields.io/badge/package-poetry-blueviolet.svg)
![Build Status](https://img.shields.io/badge/status-4.5k_uplift-brightgreen.svg)
![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)
![OS](https://img.shields.io/badge/OS-WSL2--Ubuntu-linux.svg)

An analytical data pipeline focused on calculating ROI and causal impact for marketing campaigns. This project showcases modern data engineering practices, Linux automation, and advanced statistical modeling using DuckDB.

## 🎯 Project Goal
Provide a resilient infrastructure to isolate the real effect of marketing campaigns on donation volume, using time series models (SARIMAX) to build counterfactual scenarios and ensure accurate ROI calculations.

## 🚀 Technologies & Tools
- **Language:** Python 3.14+
- **Database Engine:** [DuckDB](https://duckdb.org/) (high-performance in-process OLAP processing)
- **Package Manager:** [Poetry](https://python-poetry.org/) (isolated environments and dependency management)
- **QA & Style:** [Ruff](https://github.com/astral-sh/ruff) (ultra-fast linter and formatter)
- **Analytics:** Statsmodels (SARIMAX for causal inference)
- **Automation:** GNU Make (standardized terminal commands)

## 📦 Environment Setup

This project is optimized for **Linux/WSL2** environments.

1.  **Install Poetry** (if not already installed):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2.  **Install the project dependencies**:
    ```bash
    make install
    ```

## 🎮 How to Use (Makefile)

To speed up development and pipeline execution, a `Makefile` is provided with the following targets:

| Command | Description |
| :--- | :--- |
| `make install` | Install dependencies using Poetry. |
| `make load` | Load and clean the data (SQL -> DuckDB). |
| `make analyze` | Run the LTV analysis and generate the causal impact chart. |
| `make lint` | Check for logic and style issues using Ruff. |
| `make check` | **The all-in-one command:** Run lint, load, and analyze in sequence. |
| `make clean` | Remove the database and temporary output files. |

## 🧪 Testing & Data Quality Strategy
The project follows a **Schema-First** and **Fail-Fast** philosophy. Validations cover:
- **Data Integrity:** Using `TRY_CAST` in DuckDB to convert noise values (`'None'`, `'NP'`, `'Error'`) to `NULL` without breaking the pipeline.
- **Statistical Precision:** Calculation of average LTV ($1,482.77) and validation of campaign uplift (+4,578 donations).
- **Automation:** Verifying record volumes after ingestion to ensure no data was lost during the load process.

## 🧠 Architecture Notes (WSL/DuckDB)
The project implements a **Modern Data Stack Lite**. Transformation logic is decoupled from Python code and resides in modular `.sql` files inside the `/models` folder. This allows DuckDB to serve as an efficient modeling layer while Python focuses on orchestration and business-focused data science.

---
**Developer:** Robson Rodrigues Neves Aguiar Lachat