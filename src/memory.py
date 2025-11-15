# Memory storage utilities
import json
from datetime import datetime
import os

MEMORY_FILE = "memory_bank.json"

memory_bank = {
	"lessons": {},
	"quizzes": {},
	"progress": {}
}

def save_memory(path: str = MEMORY_FILE):
	"""Persist memory_bank to disk."""
	with open(path, "w", encoding="utf-8") as f:
		json.dump(memory_bank, f, indent=4)


def load_memory(path: str = MEMORY_FILE):
	"""Load memory_bank from disk if present, otherwise return existing in-memory bank."""
	global memory_bank
	if os.path.exists(path):
		with open(path, "r", encoding="utf-8") as f:
			memory_bank = json.load(f)
	return memory_bank

def memory_agent(day: int, lesson: str, quiz: list):
	"""Store lesson and quiz for a given day into the memory bank and persist."""
	memory_bank['lessons'][str(day)] = lesson
	memory_bank['quizzes'][str(day)] = quiz
	memory_bank['progress'][str(day)] = {
		"timestamp": datetime.utcnow().isoformat() + "Z",
		"status": "completed"
	}
	save_memory()