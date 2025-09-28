# QuickNotes

A Django application for managing quick notes.

## Setup Instructions

### Prerequisites
- Python 3.x
- Git (for cloning the repository)

### Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/sonpt-afk/quicknotes-Caleb.git
   cd quicknotes-Caleb
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Install dependencies**:
   - On Bash (MINGW64/Git Bash):
     ```bash
     ./venv/Scripts/python.exe -m pip install -r requirements.txt
     ```
   - On Windows Command Prompt:
     ```cmd
     venv\Scripts\activate && pip install -r requirements.txt
     ```

4. **Run the Django development server**:
   - On Bash (MINGW64/Git Bash):
     ```bash
     ./venv/Scripts/python.exe manage.py runserver
     ```
   - On Windows Command Prompt:
     ```cmd
     venv\Scripts\activate && python manage.py runserver
     ```

## Notes
- The project uses a virtual environment to avoid dependency conflicts with other installed packages.
- Ensure you're using the correct path separators for your shell (forward slashes `/` in Bash, backslashes `\` in Command Prompt).
- If you encounter issues, the environment is set up to isolate project dependencies.
