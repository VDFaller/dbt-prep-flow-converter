import zipfile
from pathlib import Path

import pytest
from mcp.server.fastmcp.prompts.base import UserMessage

from dbt_prep_flow_converter.fast_mcp_server import get_flow_file_from_tfl, get_sql_text, prep_flow_converter


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


def test_prep_flow_converter(fake_tfl: Path):
    """Test the flow prompt."""
    messages = prep_flow_converter(fake_tfl)
    assert len(messages) >= 3, "Should have at least 3 messages. Users/Assistant/User"
    message = messages[0]
    assert isinstance(message, UserMessage)
    assert message.role == "user"
    assert message.content.type == "text"
    assert '{"key": "value"}' in messages[2].content.text
