import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

input = sys.argv
verbose = False
if len(sys.argv) > 3:
    print("please give one input string with optional flag -v")
    sys.exit(1)
if len(sys.argv) == 3:
    if sys.argv[2] == "-v" or sys.argv[2] == "--verbose":
        verbose = True
    else:
        print("please give one input string with optional flag -v")
        sys.exit(1)

input = sys.argv[1]
client = genai.Client(api_key=api_key)

messages = [types.Content(parts = [types.Part.from_text(text=input)], role="user")]

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001', 
    contents = messages
)

print(response.text)
if verbose:
    print(f"User prompt: {input}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")