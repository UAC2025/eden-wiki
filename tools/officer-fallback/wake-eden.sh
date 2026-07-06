#!/usr/bin/env bash
# RETIRED — this script cannot change EDEN's engine (her config is
# NixOS-managed and `hermes config set` is blocked; an earlier version
# wrongly printed DONE anyway).
#
# The working method: text EDEN on Telegram:
#
#   /model deepseek/deepseek-v4-pro --provider nous
#
# Then send her a normal message to confirm she answers.
# To switch her back later:  /model gpt-5.5 --provider openai-codex
echo "This script is retired. Text EDEN on Telegram instead:"
echo "  /model deepseek/deepseek-v4-pro --provider nous"
