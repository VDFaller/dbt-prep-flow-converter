# %%
from pathlib import Path
from zipfile import ZipFile

import pytest
from langchain_core.messages import BaseMessage
from langchain_core.runnables.base import RunnableSequence
from pytest_mock import MockerFixture

from dbt_prep_flow_converter.convert import (
    get_flow_file_from_tfl,
    get_human_prompt,
    get_sql_text,
    get_system_prompt,
    run,
)

# %%


@pytest.fixture
def fake_tfl():
    """Fixture to a tfl file."""
    fp = Path("dummy_path.tfl")
    fake_flow = '{"key": "value"}'
    with ZipFile(fp, "w") as zipf:
        zipf.writestr("flow", fake_flow)
    yield fp
    # Cleanup
    fp.unlink(missing_ok=True)


def test_get_flow_file_from_tfl(fake_tfl):
    assert get_flow_file_from_tfl(fake_tfl) == '{"key": "value"}'


def test_get_system_prompt():
    path_to_prompt = Path(__file__).parent.parent / "src/dbt_prep_flow_converter/prompts/system_prompt.txt"
    assert get_system_prompt().prompt.template == path_to_prompt.read_text()


def test_get_human_prompt():
    path_to_prompt = Path(__file__).parent.parent / "src/dbt_prep_flow_converter/prompts/prompt.txt"
    assert get_human_prompt().prompt.template == path_to_prompt.read_text()


def test_get_sql_text():
    """Just going to select a random file in the jaffle_shop_files directory."""
    fp = Path(__file__).parent.parent / "src/dbt_prep_flow_converter/jaffle_shop_files/orders.sql"
    assert fp.read_text() in get_sql_text()


def test_run(mocker: MockerFixture, fake_tfl):
    mock_message = mocker.MagicMock(spec=BaseMessage)
    mock_message.content = "YAY, so much good."
    mock_chain = mocker.MagicMock(spec=RunnableSequence)
    mock_chain.batch.return_value = [mock_message]

    # Mock ChatOpenAI to avoid requiring an API key
    mocker.patch("dbt_prep_flow_converter.convert.ChatOpenAI", return_value=mocker.MagicMock())
    mocker.patch("langchain_core.runnables.base.RunnableSequence", return_value=mock_chain)
    result = run("dummy_path.tfl")
    print(result)
    assert result[0].content == "YAY, so much good."
