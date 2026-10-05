# Job Board Aggregator

A FastAPI service that pulls job postings from Greenhouse and Lever, normalizes them, and serves them through a searchable API.

## Running Locally

Requires Python 3.12+ and WSL/Linux or maacOS.

'''bash
git clone git@github.com:colebutler0218/job-board-aggregator.git
cd job-board-aggregator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then edit DATABASE_URL
uvicorn app.main:app --reload
'''

Then, open at http://localhost:8000/health. Interactive docs are at /docs.