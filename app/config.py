import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
	raise RuntimeError(
		"Missing required environment variable DATABASE_URL. "
		"Set it in your environment or add it to a .env file."
	)
