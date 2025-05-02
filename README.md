# dbt-prep-flow-converter

[![Release](https://img.shields.io/github/v/release/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/v/release/VDFaller/dbt-prep-flow-converter)
[![Build status](https://img.shields.io/github/actions/workflow/status/VDFaller/dbt-prep-flow-converter/main.yml?branch=main)](https://github.com/VDFaller/dbt-prep-flow-converter/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/VDFaller/dbt-prep-flow-converter/branch/main/graph/badge.svg)](https://codecov.io/gh/VDFaller/dbt-prep-flow-converter)
[![Commit activity](https://img.shields.io/github/commit-activity/m/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/commit-activity/m/VDFaller/dbt-prep-flow-converter)
[![License](https://img.shields.io/github/license/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/license/VDFaller/dbt-prep-flow-converter)

A converter from Tableau Prep Flows to dbt SQL.

- **Github repository**: <https://github.com/VDFaller/dbt-prep-flow-converter/>
- **Documentation** <https://VDFaller.github.io/dbt-prep-flow-converter/>

I've currently only tested with the VSCode mcp client.

## Models
I've tested these models and here's my subjective opinion on how they work with this.

| Model             | Usefulness |
| ----------------- | ---------- |
| GPT-4o | unusable | ---------- |
| Claude Sonnet 3.5 | decent     |

## Running
To get the mcp server up and running. This assumes you have [uv](https://github.com/astral-sh/uv).

1. Clone the repository
   ```bash
   git clone https://github.com/VDFaller/dbt-prep-flow-converter.git
   cd dbt-prep-flow-converter
   uv sync
   ```
2. I find it works best if you also have [dbt-mcp](https://github.com/dbt-labs/dbt-mcp), though it isn't necessary to function.
3. You'll then have to add them to your mcp config (VSCode Shown). More information regarding setting up and using MCP servers in VSCode, visit [this documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).
   ```json
       "mcp": {
			"inputs": [],
			"servers": {
				"dbt": {
					"command": "/home/YOURUSERNAME/.dbt-mcp/.venv/bin/mcp",
					"args": [
						"run",
						"/path/to/your/dbt-mcp/src/dbt_mcp/main.py"
					]
				},
				"dbt-prep-flow-converter": {
					"command": "uv",
					"args": [
						"--directory",
						"/path/to/your/dbt-prep-flow-converter",
						"run",
						"dbt_prep_flow_converter"
					]
				},
			}
		},
	```


Then just let er rip.


## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/VDFaller/dbt-prep-flow-converter/settings/secrets/actions/new).
- Create a [new release](https://github.com/VDFaller/dbt-prep-flow-converter/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
