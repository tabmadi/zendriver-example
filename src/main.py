"""Application entry point.

This module provides a small `main()` function and a `__main__` guard.
"""

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the application."""
    logger.info("Hello world!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
