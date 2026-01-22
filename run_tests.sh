#!/usr/bin/env bash

set -e

# Run tests inside uv-managed environment
uv run pytest


scripts venv/Scripts/activate

pytest
deactivate