import asyncio

from . import server
from .convert import run_cli, run_convert


def main() -> None:
    """Main entry point for the package."""
    asyncio.run(server.main())


__all__ = ["main", "run_cli", "run_convert", "server"]
