# Job Board Aggregator

A FastAPI service that pulls job postings from Greenhouse and Lever, normalizes them, and serves them through a searchable API.

## Prerequisites

- Python 3.12+
- PostgreSQL 16
- Linux or WSL2 on Windows

## Database setup

These steps are for Ubuntu/WSL.

```bash
sudo apt update
sudo apt install postgresql
sudo service postgresql start
```

Create a dedicated user and database for the app. You'll be prompted to set a password:

```bash
sudo -u postgres createuser --pwprompt jobs
sudo -u postgres createdb --owner=jobs jobs
```

Check that you can connect:

```bash
psql "postgresql://jobs:YOUR_PASSWORD@localhost:5432/jobs" -c "select version();"
```

> **WSL note:** Postgres may not start automatically when WSL restarts. If the app can't connect, run `sudo service postgresql start`.

## Running locally

```bash
git clone https://github.com/colebutler0218/job-board-aggregator.git
cd job-board-aggregator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then set DATABASE_URL to the URL you tested above
uvicorn app.main:app --reload
```

Then open http://localhost:8000/health. Interactive API docs are at http://localhost:8000/docs.
