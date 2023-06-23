#!/usr/bin/env bash

source venv/bin/activate

sphinx-build -Wb html docs public
