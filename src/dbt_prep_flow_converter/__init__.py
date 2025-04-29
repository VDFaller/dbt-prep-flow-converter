from .fast_mcp_server import mcp


def main() -> None:
    """Main entry point for the package."""
    mcp.run(transport="stdio")


__all__ = ["main"]
