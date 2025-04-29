import zipfile
from pathlib import Path

import pytest
from mcp.server.fastmcp.prompts.base import UserMessage

from dbt_prep_flow_converter.fast_mcp_server import flow_prompt, get_flow_file_from_tfl, get_sql_text


@pytest.fixture
def fake_tfl(tmp_path: Path):
    """Fixture to a tfl file."""
    fp = tmp_path / "dummy_path.tfl"
    fake_flow = '{"key": "value"}'
    with zipfile.ZipFile(fp, "w") as zipf:
        zipf.writestr("flow", fake_flow)
    yield fp


def test_get_sql_text():
    """Just going to select a random file in the jaffle_shop_files directory."""
    fp = Path(__file__).parent.parent / "src/dbt_prep_flow_converter/jaffle_shop_files/mart/orders.sql"
    assert fp.read_text() in get_sql_text()


def test_get_flow_file_from_tfl(fake_tfl):
    assert get_flow_file_from_tfl(fake_tfl) == '{"key": "value"}'


def test_flow_prompt(fake_tfl: Path):
    """Test the flow prompt."""
    prompt = flow_prompt(fake_tfl)
    assert isinstance(prompt, UserMessage)
    assert prompt.role == "user"
    assert prompt.content.type == "text"
    assert '{"key": "value"}' in prompt.content.text
