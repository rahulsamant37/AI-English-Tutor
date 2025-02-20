import os

# Define the directory structure
directories = [
    
    # Agent-related directories
    "api/agents",
    "api/agents/tools",
    "api/agents/prompts",
    "api/agents/chains",
    
    # Voice processing
    "api/voice",
    "api/voice/processors",
    "api/voice/models",
    
    # English learning content
    "api/content",
    "api/content/lessons",
    "api/content/exercises",
    "api/content/vocabulary",
    
    # Configuration and utilities
    "api/config",
    "api/utils",
    
    # Frontend
    "streamlit-app",
    
    # Testing
    "tests",
    
    # CI/CD and deployment
    ".github/workflows"
]

# Create directories
for directory in directories:
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {directory}: {e}")

# Create empty files where needed
empty_files = [
    # Main API file
    "api/main.py",

    # Agent-related directories
    "api/agents/base_agent.py",
    "api/agents/english_tutor_agent.py",
    "api/agents/tools/__init__.py",
    "api/agents/prompts/__init__.py",
    "api/agents/chains/__init__.py",

    # Voice processing
    "api/voice/processors/speech_to_text.py",
    "api/voice/processors/text_to_speech.py",
    "api/voice/models/__init__.py",

    # Core API structure
    "api/config/settings.py",
    "api/routes/voice.py",
    "api/services/voice_service.py",
    "api/utils/__init__.py",

    # Frontend
    "streamlit-app/Home.py",

    # Testing
    "tests/__init__.py",

    # CI/CD and deployment
    ".github/workflows/.gitkeep"
]

for file in empty_files:
    try:
        # Ensure the parent directory exists before creating the file
        os.makedirs(os.path.dirname(file), exist_ok=True)
        
        # Create the empty file
        with open(file, 'w') as f:
            pass  # Create empty file
    except Exception as e:
        print(f"Error creating file {file}: {e}")

print("Directory structure created successfully!")
