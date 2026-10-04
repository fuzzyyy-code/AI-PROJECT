# AI PROJECT

A collection of AI projects and experiments, written mainly in Python.

> **Status:** Early setup. No projects have been added yet.

## Repository layout

Put each project in its own folder at the root of the repository:

```
AI PROJECT/
├── README.md          # This file
├── .gitignore         # Python ignore rules (venvs, caches, build output, .env)
├── .gitattributes     # Line-ending normalization
└── <project-name>/    # One folder per project
    ├── README.md      # What it does and how to run it
    ├── requirements.txt
    └── ...
```

## Getting started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Setup

```bash
git clone <repository-url>
cd "AI PROJECT"

# Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# Install a project's dependencies
pip install -r <project-name>/requirements.txt
```

### Secrets and API keys

Keep API keys in a `.env` file inside the project folder. Git already ignores `.env`, so never commit keys directly in code.

```
# <project-name>/.env
ANTHROPIC_API_KEY=your-key-here
```

## Adding a new project

1. Create a folder: `mkdir <project-name>`
2. Add a `README.md` that says what the project does and how to run it.
3. List dependencies in `requirements.txt` (`pip freeze > requirements.txt`).
4. Add a row to the table below.

## Projects

| Project | Description | Status |
| ------- | ----------- | ------ |
| _None yet_ | | |
