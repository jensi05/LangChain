import os
from dotenv import load_dotenv

load_dotenv()

# Try to list available models using the API
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # List all available models
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"- {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Supported Methods: {model.supported_generation_methods}")
        print()
except Exception as e:
    print(f"Error listing models: {e}")
    print("\nTrying alternative approach...")
    
    # If that doesn't work, show common model names
    common_models = [
        "gemini-pro",
        "gemini-1.5-flash", 
        "gemini-1.5-pro",
        "gemini-2.0-flash",
        "gemini-2.5-flash"
    ]
    print("Common available models:")
    for model in common_models:
        print(f"- {model}")
