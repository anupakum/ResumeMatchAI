#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def setup_environment():
    env_file = Path('.env')
    if env_file.exists():
        print("Loading environment variables from .env file...")
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value
                    print(f"Set {key}")
    os.environ.setdefault('FLASK_ENV', 'development')

def check_dependencies():
    try:
        import flask, flask_sqlalchemy, spacy, sklearn, pandas, pdfplumber, docx
        print("All required Python dependencies are installed.")
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_spacy_model():
    try:
        import spacy
        spacy.load("en_core_web_sm")
        print("spaCy model 'en_core_web_sm' is available.")
        return True
    except OSError:
        print("spaCy model 'en_core_web_sm' not found.")
        print("Run: python -m spacy download en_core_web_sm")
        return False

def create_directories():
    for d in ['uploads', 'instance']:
        Path(d).mkdir(exist_ok=True)
        print(f"Directory '{d}' is ready.")

def main():
    print("Starting Resume Match AI - Local Development")
    print("=" * 50)
    setup_environment()
    if not check_dependencies(): sys.exit(1)
    if not check_spacy_model(): sys.exit(1)
    create_directories()
    print("=" * 50)
    print("Access the app at http://localhost:5000")
    from main import app
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
