#!/bin/bash

set -e

GITREPO=$(basename `git rev-parse --show-toplevel`)

jq -n --arg gitrepo "$GITREPO" '{"name":$gitrepo}'
