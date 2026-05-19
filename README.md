# NYC Taxi Demand Pipeline

**Goal:** Build a single end-to-end ML pipeline as a proper software project, not a notebook.

This means ingesting raw data, validating it, engineering features, training a demand forecasting model, evaluating it, and saving artifacts — all in modular Python scripts with clean separation between stages.

## Pipeline Stages

| Stage | Description |
|---|---|
| `ingest` | Load raw NYC taxi CSV data into a structured format |
| `validate` | Schema and quality checks with Pandera — reject bad rows before they corrupt downstream stages |
| `transform` | Feature engineering: extract hour, bin coordinates into zones, aggregate to trips-per-zone-per-hour |
| `train` | Train a demand forecasting model with scikit-learn and save it as an artifact |
| `evaluate` | Evaluate model performance and log metrics |

## Project Structure

```
pipeline/        # One module per stage
data/
  raw/           # Input CSVs (not tracked by git)
  validated/     # Output of validate stage
  transformed/   # Output of transform stage
  models/        # Saved model artifacts
configs/         # Stage configuration
tests/           # Unit tests mirroring pipeline structure
notebooks/       # Exploratory analysis only — not part of the pipeline
main.py          # Runs all stages end to end
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```
