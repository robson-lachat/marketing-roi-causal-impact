# 📈 Marketing ROI & Causal Impact Pipeline

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![DuckDB](https://img.shields.io/badge/database-DuckDB-orange.svg)
![Package Manager](https://img.shields.io/badge/package-poetry-blueviolet.svg)
![Build Status](https://img.shields.io/badge/status-4.5k_uplift-brightgreen.svg)
![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)
![OS](https://img.shields.io/badge/OS-WSL2--Ubuntu-linux.svg)

Um pipeline de dados analítico focado no cálculo de ROI e impacto causal de campanhas de marketing. Este projeto demonstra práticas modernas de engenharia de dados, automação em Linux e modelagem estatística avançada utilizando DuckDB.

## 🎯 Project Goal
Prover uma infraestrutura resiliente para isolar o efeito real de campanhas de marketing sobre o volume de doações, utilizando modelos de séries temporais (SARIMAX) para criar cenários contrafactuais e garantir cálculos de ROI precisos.

## 🚀 Technologies & Tools
- **Language:** Python 3.13+
- **Database Engine:** [DuckDB](https://duckdb.org/) (Processamento OLAP in-process de alta performance)
- **Package Manager:** [Poetry](https://python-poetry.org/) (Ambientes isolados e gestão de dependências)
- **QA & Style:** [Ruff](https://github.com/astral-sh/ruff) (Linter e formatter ultra-rápido)
- **Analytics:** Statsmodels (SARIMAX para inferência causal)
- **Automation:** GNU Make (Padronização de comandos de terminal)

## 📦 Environment Setup

Este projeto é otimizado para ambientes **Linux/WSL2**.

1.  **Instalar o Poetry** (caso não possua):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2.  **Instalar dependências do projeto**:
    ```bash
    make install
    ```

## 🎮 How to Use (Makefile)

Para agilizar o desenvolvimento e a execução do pipeline, um `Makefile` é fornecido com os seguintes alvos:

| Command        | Description                                                          |
| :------------- | :------------------------------------------------------------------- |
| `make install` | Instala dependências via Poetry.                                     |
| `make load`    | Executa a carga e limpeza dos dados (SQL -> DuckDB).                 |
| `make analyze` | Roda a análise de LTV e gera o gráfico de impacto causal.            |
| `make lint`    | Verifica erros de lógica e estilo usando Ruff.                       |
| `make check`   | **O comando definitivo:** Executa lint, load e analyze em sequência. |
| `make clean`   | Remove o banco de dados e arquivos temporários de saída.             |

## 🧪 Data Quality Strategy
O projeto foca na integridade dos dados através de uma filosofia de **Schema-First**:
- **Data Integrity:** Uso de `TRY_CAST` no DuckDB para converter ruídos (`'None'`, `'NP'`, `'Error'`) em `NULL` sem quebrar o pipeline.
- **Statistical Precision:** Cálculo de LTV Médio ($1,482.77) e validação do uplift da campanha (+4,578 doações).
- **Validation:** Verificação de volume de registros pós-ingestão para garantir a consistência do processo de carga.
*Nota: A cobertura total de testes unitários está planeada para futuras iterações.*

## 🧠 Architecture Notes (WSL/DuckDB)
O projeto implementa uma **Modern Data Stack Lite**. A lógica de transformação é desacoplada do código Python e reside em arquivos `.sql` modulares dentro da pasta `/models`. Isso permite que o DuckDB atue como uma camada de modelagem eficiente, enquanto o Python foca na orquestração e na ciência de dados aplicada ao negócio.

---
**Developer:** Robson Rodrigues Neves Aguiar Lachat