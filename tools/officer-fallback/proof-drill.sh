#!/usr/bin/env bash
# proof-drill — run ANY officer's proof loop on ANY model. Generalized from
# the s6-proof.sh harness that disqualified hermes-4-405b and proved
# deepseek-v4-pro (2026-07-06).
#
# Usage (operator, needs sudo):
#   sudo bash proof-drill.sh <profile> [model] [provider]
#   sudo bash proof-drill.sh s3_operations                      # doctrine default model
#   sudo bash proof-drill.sh s6_comms qwen/qwen3-plus nous      # model tryout
#
# PASS criteria (judge the output): >0 tool calls in the session summary,
# a real ledger line appended, DATA-RULE-clean claims, real shop work.
set -u
PROFILE="${1:?usage: proof-drill.sh <profile> [model] [provider]}"
MODEL="${2:-deepseek/deepseek-v4-pro}"
PROVIDER="${3:-nous}"
H=/persist/eden/hermes/.hermes
HB=/run/current-system/sw/bin/hermes
LEDGER=/persist/eden/hermes/workspace/ledgers/officers.jsonl
OUT=/home/eden/proof-drill-output.txt
exec > >(tee "$OUT") 2>&1

echo "== proof-drill: $PROFILE on $PROVIDER/$MODEL =="

echo "== 1/4 provider credential in the $PROFILE profile =="
if ! sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile "$PROFILE" auth list "$PROVIDER" 2>/dev/null | grep -q "oauth\|api"; then
  if [ "$PROVIDER" = nous ]; then
    printf 'y\n' | sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile "$PROFILE" auth add nous --type oauth --no-browser || { echo "FAIL: could not hand $PROFILE the nous key"; exit 1; }
  else
    echo "FAIL: $PROFILE has no $PROVIDER credential and auto-import only exists for nous"; exit 1
  fi
fi

echo "== 2/4 ledger present =="
sudo -u hermes mkdir -p "$(dirname $LEDGER)" && sudo -u hermes touch "$LEDGER"

echo "== 3/4 drill (may take minutes) =="
sudo -u hermes env --chdir=/persist/eden/hermes/workspace HOME=/persist/eden/hermes HERMES_HOME=$H \
  $HB --profile "$PROFILE" chat -m "$MODEL" --provider "$PROVIDER" \
  -q "Run one full six-step loop of your primary duty per your PLAYBOOK. Every Act step must be a real tool call. If a tool, credential, or data source is unavailable, report 'BLOCKED — <what is missing>' and stop; never describe work you did not actually perform. Append your loop_tick to the shared officer ledger via: python3 workspace/eden-wiki/tools/ledger_append.py --officer $PROFILE --event loop_tick --loop <name> --step adapt --outcome <ok|fail|blocked|partial> --detail '<one line>' --evidence <path-or-session>. Report BLUF."

echo "== 4/4 last 3 ledger lines =="
sudo -u hermes tail -3 "$LEDGER"
echo "== DRILL COMPLETE — output saved to $OUT =="
