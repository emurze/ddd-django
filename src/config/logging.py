import os
from .base import DATA_DIR

LOG_LEVEL = os.getenv("LOGGING_LEVEL", "WARNING")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": LOG_LEVEL,
            "class": "logging.FileHandler",
            "filename": DATA_DIR / "logs/general.log",
        },
        "stream": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "level": LOG_LEVEL,
            "handlers": [
                "stream",
                "file",
            ],
            "propagate": True,
        },
    },
}
