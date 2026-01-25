from pathlib import Path

def load_prompt(name: str, **kwargs) -> str:
    """
    Loads and formats a prompt template from the prompts directory.

    - Reads a prompt file by its name
    - Replaces placeholder variables with provided keyword arguments
    - Returns the formatted prompt as a string
    """
    base_path = Path(__file__).resolve().parent.parent / "prompts"
    prompt_path = base_path / name

    template = prompt_path.read_text(encoding="utf-8")

    for key, value in kwargs.items():
        template = template.replace(f"{{{{{key}}}}}", value)

    return template