#!/usr/bin/env bash
# Hand the Nous key to officers S1-S5 (S6 already has his).
# Run with:  sudo bash give-keys.sh
set -u
H=/persist/eden/hermes/.hermes
HB=/run/current-system/sw/bin/hermes
for p in s1_personnel s2_intel s3_operations s4_logistics s5_plans; do
  echo "== handing the Nous key to $p =="
  if sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile $p auth list nous 2>/dev/null | grep -q oauth; then
    echo "$p already has the key."
  else
    printf 'y\n' | sudo -u hermes env HOME=/persist/eden/hermes HERMES_HOME=$H $HB --profile $p auth add nous --type oauth --no-browser
  fi
done
echo "== ALL KEYS HANDED OUT =="
