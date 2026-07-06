#!/usr/bin/env bash
# S6 proof drill — one-shot, run via:  ! bash /home/eden/s6-proof.sh
# Checks the Nous login, creates the officer ledger, runs the S6 test lap,
# and prints the ledger. Asks for your computer password once (sudo).
set -u
exec > >(tee /home/eden/s6-proof-output.txt) 2>&1
H=/persist/eden/hermes/.hermes
HB=/run/current-system/sw/bin/hermes
LEDGER=/persist/eden/hermes/workspace/ledgers/officers.jsonl

echo "== Step 1 of 6: checking the Nous login =="
if ! sudo -u hermes env HERMES_HOME=$H $HB auth list nous; then
  echo "PROBLEM: no Nous login found. Stopping here — nothing was changed."
  exit 1
fi

echo "== Step 2 of 6: creating the officers' shared logbook =="
sudo -u hermes mkdir -p "$(dirname $LEDGER)"
sudo -u hermes touch "$LEDGER"

echo "== Step 3 of 6: recording the earlier failed test in the logbook =="
if ! sudo -u hermes grep -q 20260706_153742_063b14 "$LEDGER" 2>/dev/null; then
  echo '{"ts":"2026-07-06T17:40:00Z","officer":"eden","event":"loop_tick","loop":"s6-proof-drill","step":"adapt","outcome":"fail","detail":"proof run 1 FAIL: 0 tool calls, fabricated dispatch report, ledger claim false; profile flag missing so S6 never loaded","evidence":"session 20260706_153742_063b14","to":null}' | sudo -u hermes tee -a "$LEDGER" > /dev/null
fi

echo "== Step 3b: recording Hermes-4's second failed test in the logbook =="
if ! sudo -u hermes grep -q 20260706_154903_21dd64 "$LEDGER" 2>/dev/null; then
  echo '{"ts":"2026-07-06T17:49:30Z","officer":"eden","event":"loop_tick","loop":"s6-proof-drill","step":"adapt","outcome":"fail","detail":"proof run 2 FAIL (hermes-4-405b DISQUALIFIED as officer brain): profile+tools loaded, 0 tool calls, printed write_file as prose and claimed Logged while ledger unchanged; honored BLOCKED on empty queue","evidence":"session 20260706_154903_21dd64","to":null}' | sudo -u hermes tee -a "$LEDGER" > /dev/null
fi

echo "== Step 4 of 6: handing the Nous key to officer S6 =="
if sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile s6_comms auth list nous 2>/dev/null | grep -q "device_code\|oauth"; then
  echo "S6 already has the key."
else
  printf 'y\n' | sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile s6_comms auth add nous --type oauth --no-browser
fi

echo "== Step 5 of 6: running the S6 test lap on deepseek-v4-pro =="
sudo -u hermes env --chdir=/persist/eden/hermes/workspace HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile s6_comms chat -m deepseek/deepseek-v4-pro --provider nous \
  -q "Run one full six-step loop of your primary dispatch duty. Every Act step must be a real tool call. If a tool, credential, or data source is unavailable, report 'BLOCKED — <what is missing>' and stop; never describe work you did not actually perform. Append a loop_tick line to the shared officer ledger at workspace/ledgers/officers.jsonl at adapt via a real file write, citing evidence. Report BLUF."

echo "== Step 6 of 6: what the logbook says now =="
sudo -u hermes cat "$LEDGER"
echo "== TEST COMPLETE — show this output to Claude =="
