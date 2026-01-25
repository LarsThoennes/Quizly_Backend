from pathlib import Path

def load_prompt(name: str, **kwargs) -> str:
    base_path = Path(__file__).resolve().parent.parent / "prompts"
    prompt_path = base_path / name

    template = prompt_path.read_text(encoding="utf-8")

    for key, value in kwargs.items():
        template = template.replace(f"{{{{{key}}}}}", value)

    return template