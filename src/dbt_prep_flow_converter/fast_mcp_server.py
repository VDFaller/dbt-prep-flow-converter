# %%
import zipfile
from pathlib import Path
from typing import cast

from mcp import types
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts.base import UserMessage

# Initialize FastMCP server
mcp = FastMCP("dbt-prep-flow-converter")
HERE = Path(__file__).parent


## helper functions
def get_flow_file_from_tfl(path: Path | str) -> str:
    """Get the JSON content from a TFL file contained in a zip archive.

    Args:
        path (Path | str): A path to the TFL file.

    Returns:
        str: The JSON content extracted from the TFL file.
    """
    with zipfile.ZipFile(Path(path).resolve(), "r") as zip_ref, zip_ref.open("flow") as file:
        json_content = file.read().decode("utf-8")
        return json_content


def get_sql_text() -> str:
    """Get the sql from all the files in jaffle_shop_files/*.sql.

    Returns:
        str: The SQL prompt.
    """
    txt = ""
    for file in (HERE / "jaffle_shop_files").rglob("*.sql"):
        with file.open("r") as f:
            query_txt = f.read()
        txt += f"\n\n```sql\n-- {file.stem}\n\n{query_txt}\n```"
    return txt


@mcp.prompt()
def flow_prompt(flow_path: str) -> UserMessage:
    """Load and return the system message prompt from 'flow_prompt.md'.

    Returns:
        UserMessage: The system prompt
    """
    example_flow = get_flow_file_from_tfl(HERE.joinpath("jaffle_shop_files", "jaffle_shop.tfl"))
    sql_text = get_sql_text()
    flow_text = get_flow_file_from_tfl(flow_path)
    system_prompt = HERE.joinpath("prompts", "flow_prompt.md").read_text()
    system_prompt = system_prompt.format(example_flow=example_flow, sql_text=sql_text, flow_text=flow_text)
    return UserMessage(content=system_prompt)


@mcp.prompt()
async def prep_flow_converter(
    path_to_flow: str,
) -> list[UserMessage]:
    "Gets the prompt required to convert a TFL file to a set of SQL files."
    return [
        flow_prompt(path_to_flow),
    ]


@mcp.tool()
async def convert_prep_flow(path_to_flow: str) -> str:
    """Convert a TFL file to a set of SQL files."""
    path_to_flow = str(Path(path_to_flow).resolve())
    prompt_result: list[UserMessage] = await prep_flow_converter(path_to_flow)
    content = cast(types.TextContent, prompt_result[0].content)
    return content.text


# %%

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
