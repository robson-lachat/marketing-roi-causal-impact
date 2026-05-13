# 📈 Marketing ROI & Causal Impact Pipeline

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![DuckDB](https://img.shields.io/badge/database-DuckDB-orange.svg)
![Package Manager](https://img.shields.io/badge/package-poetry-blueviolet.svg)
![Build Status](https://img.shields.io/badge/status-4.5k_uplift-brightgreen.svg)
![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)
![OS](https://img.shields.io/badge/OS-WSL2--Ubuntu-linux.svg)

An analytical data pipeline focused on calculating marketing campaign ROI and causal impact. This project demonstrates modern data engineering practices, Linux automation, and advanced statistical modeling using DuckDB.

## 🎯 Project Goal
Provide a resilient infrastructure to isolate the true effect of marketing campaigns on donation volume by using time series models (SARIMAX) to build counterfactual scenarios and ensure precise ROI calculations.

## 🚀 Technologies & Tools
- **Language:** Python 3.13+
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

2.  **Install project dependencies**:
    ```bash
    make install
    ```

## 🎮 How to Use (Makefile)

To streamline development and pipeline execution, a `Makefile` is provided with the following targets:

| Command        | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| `make install` | Installs dependencies via Poetry.                            |
| `make load`    | Runs the data load pipeline (SQL -> DuckDB).                 |
| `make analyze` | Runs the LTV analysis and generates the causal impact chart. |
| `make lint`    | Checks logic and style issues using Ruff.                    |
| `make format`  | Automatically formats code with Ruff.                        |
| `make check`   | Runs FORMAT, LOAD and ANALYZE in sequence.                   |
| `make clean`   | Removes the database and temporary output files.             |

## 🧪 Data Quality Strategy
The project focuses on data integrity through a **Schema-First** philosophy:
- **Data Integrity:** Uses `TRY_CAST` in DuckDB to convert noisy values (`'None'`, `'NP'`, `'Error'`) into `NULL` without breaking the pipeline.
- **Statistical Precision:** Calculates average LTV ($1,482.77) and validates campaign uplift (+4,578 donations).
- **Validation:** Verifies record counts after ingestion to ensure consistency in the loading process.
*Note: Full unit test coverage is planned for future iterations.*

## 🧠 Architecture Notes (WSL/DuckDB)
The project implements a **Modern Data Stack Lite**. Transformation logic is decoupled from Python code and lives in modular `.sql` files inside the `/models` folder. This allows DuckDB to act as an efficient modeling layer while Python focuses on orchestration and business-focused data science.

---
**Developer:** Robson Rodrigues Neves Aguiar Lachat