import importlib.util
import os
from pathlib import Path

from django.conf import settings

ROOT_DIR = Path(__file__).parent.parent.parent.parent
MODELS_FILENAME = "models"
EXCLUDE_DIRS = getattr(settings, "EXCLUDE_MODELS_SEARCH_PATHS", [])


def import_all_models(root: Path, filename: str, exclude_dirs: list) -> None:
    child_dir_names = set(os.listdir(root)) - set(exclude_dirs)
    child_dirs = (root / child for child in child_dir_names)

    for child in child_dirs:
        for child_root, _, files in os.walk(child):
            for file in files:
                if file == f"{filename}.py":
                    module_name = os.path.splitext(file)[0]
                    spec = importlib.util.spec_from_file_location(
                        module_name, os.path.join(child_root, file)
                    )
                    module = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(module)
                    print(f"Imported module: {module}")


import_all_models(
    root=ROOT_DIR,
    filename=MODELS_FILENAME,
    exclude_dirs=EXCLUDE_DIRS,
)
