# Configuration and Gemini wrapper
from kaggle_secrets import UserSecretsClient
import google.generativeai as genai
import traceback


# Load and configure Gemini using Kaggle Secrets
_user_secrets = UserSecretsClient()
GEMINI_API_KEY = _user_secrets.get_secret("GEMINI_API_KEY")
if not GEMINI_API_KEY:
	raise ValueError("GEMINI_API_KEY not found in Kaggle Secrets. Add it under Notebook Settings -> Secrets.")


# Choose a working model from your available models
MODEL_NAME = "gemini-2.5-flash"


# configure SDK
genai.configure(api_key=GEMINI_API_KEY)




def gemini_generate(prompt, model_name=MODEL_NAME, timeout=30.0):
	"""Generate text from Gemini model. Returns string output.
	Handles common response shapes safely.
	"""
	try:
		model = genai.GenerativeModel(model_name)
		resp = model.generate_content(prompt)
		# prefer .text if available
		if hasattr(resp, "text") and resp.text:
			return resp.text
		# fallback to candidates
		if hasattr(resp, "candidates") and resp.candidates:
			# some SDKs provide candidates with .content
			cand = resp.candidates[0]
			return getattr(cand, "content", str(cand))
		return str(resp)
	except Exception:
		# print stack for debugging and re-raise
		traceback.print_exc()
		raise