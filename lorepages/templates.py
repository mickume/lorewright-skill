from pathlib import Path

import jinja2

_TEMPLATES_DIR = Path(__file__).parent / "templates"


def create_jinja_env() -> jinja2.Environment:
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(_TEMPLATES_DIR)),
        autoescape=True,
    )
