# dbt-prep-flow-converter

[![Release](https://img.shields.io/github/v/release/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/v/release/VDFaller/dbt-prep-flow-converter)
[![Build status](https://img.shields.io/github/actions/workflow/status/VDFaller/dbt-prep-flow-converter/main.yml?branch=main)](https://github.com/VDFaller/dbt-prep-flow-converter/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/VDFaller/dbt-prep-flow-converter/branch/main/graph/badge.svg)](https://codecov.io/gh/VDFaller/dbt-prep-flow-converter)
[![Commit activity](https://img.shields.io/github/commit-activity/m/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/commit-activity/m/VDFaller/dbt-prep-flow-converter)
[![License](https://img.shields.io/github/license/VDFaller/dbt-prep-flow-converter)](https://img.shields.io/github/license/VDFaller/dbt-prep-flow-converter)

A converter from Tableau Prep Flows to dbt SQL.  Currently running on dbt-duckdb/dbt-databricks and openAI only.

- **Github repository**: <https://github.com/VDFaller/dbt-prep-flow-converter/>
- **Documentation** <https://VDFaller.github.io/dbt-prep-flow-converter/>

## Running
It has a cli tool so you should be able to run it like this:

```bash
uv run rip_flow "/home/faller/repos/tab-flow-converter/src/tab_flow_converter/shipment_example.tfl"
```

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/VDFaller/dbt-prep-flow-converter/settings/secrets/actions/new).
- Create a [new release](https://github.com/VDFaller/dbt-prep-flow-converter/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
