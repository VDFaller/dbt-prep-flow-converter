# %%
import zipfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts.base import AssistantMessage, Message, UserMessage

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


def prep_flow_converter(
    flow_path: str,
) -> list[Message]:
    "Gets the prompt required to convert a TFL file to a set of SQL files."
    example_flow = get_flow_file_from_tfl(HERE.joinpath("jaffle_shop_files", "jaffle_shop.tfl"))
    sql_text = get_sql_text()
    flow_text = get_flow_file_from_tfl(flow_path)
    system_prompt = HERE.joinpath("prompts", "flow_prompt.md").read_text()
    system_prompt = system_prompt.format(example_flow=example_flow, sql_text=sql_text)
    system_message = UserMessage(content=system_prompt)

    assistant_reply = AssistantMessage(
        content="I understand. Please provide me the flow file and I'll try to convert it"
    )

    user_prompt = HERE.joinpath("prompts", "prompt.md").read_text()
    user_prompt = user_prompt.format(flow_text=flow_text)
    user_message = UserMessage(content=user_prompt)

    return [system_message, assistant_reply, user_message]


@mcp.tool()
async def convert_prep_flow(path_to_flow: str) -> list[Message]:
    """Convert a TFL file to a set of SQL files."""
    path_to_flow = str(Path(path_to_flow).resolve())
    prompt_result: list[Message] = prep_flow_converter(path_to_flow)
    return prompt_result


# %%

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
