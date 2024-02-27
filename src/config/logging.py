import os
from .base import BASE_DIR

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": os.getenv("LOGGING_LEVEL"),
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "shared/infra/django/data/logs/general.log",
        },
        "stream": {
            "level": os.getenv("LOGGING_LEVEL"),
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "level": os.getenv("LOGGING_LEVEL"),
            "handlers": [
                "stream",
                "file",
            ],
            "propagate": True,
        },
    },
}