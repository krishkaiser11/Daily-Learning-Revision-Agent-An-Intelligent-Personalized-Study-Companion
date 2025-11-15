import logging
from typing import Dict, Tuple, List

# imports from local modules
from config import gemini_generate
from memory import memory_agent

logging.basicConfig(level=logging.INFO, format="%(message)s")

def planner_agent(topic: str, days: int) -> Dict[int, str]:
	"""Use Gemini to break a topic into `days` modules.
	Returns a dict mapping day -> subtopic title.
	"""
	logging.info("🧠 Planner Agent activated (Gemini)")

	prompt = (
		f"Break the topic '{topic}' into {days} concise daily learning modules.\n"
		"Return a numbered list, one module per line, with short titles only."
	)

	plan_text = gemini_generate(prompt)
	plan = {}
	idx = 1
	for line in plan_text.splitlines():
		line = line.strip()
		if not line:
			continue
		# remove leading numbering like "1." or "1)"
		cleaned = line.lstrip('0123456789. )\t').strip()
		plan[idx] = cleaned
		idx += 1
		if idx > days:
			break

	# Pad if needed
	while len(plan) < days:
		plan[len(plan)+1] = f"{topic} - Subtopic {len(plan)+1}"

	logging.info(f"📅 Study plan created for {days} days")
	return plan


def content_agent(subtopic: str) -> str:
	"""Create a lesson for the given subtopic using Gemini."""
	logging.info("📘 Content Agent generating lesson (Gemini)")

	prompt = (
		f"Create a clear, easy-to-understand lesson on:\n\n{subtopic}\n\n"
		"Include these sections:\n"
		"- Short introduction (1-2 lines)\n"
		"- Key concepts (3-6 bullet points with short explanations)\n"
		"- One simple example or analogy\n"
		"- Short summary\n"
		"Keep content concise and friendly for learners."
	)

	lesson = gemini_generate(prompt)
	lesson_md = f"# Lesson: {subtopic}\n\n{lesson}"
	return lesson_md


def quiz_agent(lesson_text: str, num_questions: int = 6) -> List[str]:
	"""Generate revision questions from lesson text."""
	logging.info("❓ Quiz Agent generating questions (Gemini)")

	prompt = (
		"Based on the following lesson text, generate "
		f"{num_questions} short MCQ-style or short-answer revision questions. "
		"Output each question on a new line. Do not include answers.\n\n"
		f"Lesson:\n{lesson_text}"
	)

	output = gemini_generate(prompt)
	questions = [q.strip() for q in output.splitlines() if q.strip()]
	if len(questions) > num_questions:
		questions = questions[:num_questions]
	while len(questions) < num_questions:
		questions.append(
			f"What is one key idea from the lesson about {lesson_text.splitlines()[0] if lesson_text else 'this topic'}?"
		)
	return questions


def coordinator(topic: str, days: int, current_day: int, plan: Dict[int, str]) -> Tuple[str, List[str]]:
	"""Coordinate sub-agents for a single day and store results in memory."""
	logging.info(f"\n🚀 Coordinator Agent running for Day {current_day}")

	subtopic = plan[current_day]
	lesson = content_agent(subtopic)
	quiz = quiz_agent(lesson)
	memory_agent(current_day, lesson, quiz)
	return lesson, quiz