import asyncio

from . import server
from .convert import convert, run_cli


def main() -> None:
    """Main entry point for the package."""
    asyncio.run(server.main())


__all__ = ["convert", "main", "run_cli", "server"]
