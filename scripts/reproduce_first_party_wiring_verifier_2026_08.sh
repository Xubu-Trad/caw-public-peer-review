#!/usr/bin/env bash
set +e
set +o pipefail
LC_ALL=C

UPSTREAM="https://github.com/GilgameshCaw/Caw.git"
REF="d7a0e05445f13f268b8e0c60a3d4854cb4b206de"
WORK="${TMPDIR:-/tmp}/caw_first_party_verifier_${REF:0:12}"

L1_RPC_URL="${L1_RPC_URL:-https://ethereum-sepolia-rpc.publicnode.com}"
L2_RPC_URL="${L2_RPC_URL:-https://sepolia.base.org}"
L2B_RPC_URL="${L2B_RPC_URL:-https://sepolia-rollup.arbitrum.io/rpc}"

command -v git >/dev/null 2>&1 || { echo "ERROR git not found"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "ERROR node not found"; exit 2; }
command -v npm >/dev/null 2>&1 || { echo "ERROR npm not found"; exit 2; }

rm -rf "$WORK"
git clone --no-checkout "$UPSTREAM" "$WORK"
rc=$?
[ "$rc" -eq 0 ] || { echo "ERROR clone rc=$rc"; exit "$rc"; }

cd "$WORK" || exit 2
git checkout --detach "$REF"
rc=$?
[ "$rc" -eq 0 ] || { echo "ERROR checkout rc=$rc"; exit "$rc"; }

ACTUAL_REF=$(git rev-parse HEAD)
echo "TYPE=FIRST_PARTY_VERIFIER_REPRODUCTION"
echo "UPSTREAM=$UPSTREAM"
echo "EXPECTED_REF=$REF"
echo "ACTUAL_REF=$ACTUAL_REF"
echo "WRITE_TX=NO"
echo "CHAIN_STATE=READ_ONLY"

if [ "$ACTUAL_REF" != "$REF" ]; then
  echo "ERROR exact upstream ref mismatch"
  exit 3
fi

cd solidity || exit 2

# The verifier requires ethers and dotenv. npm install uses upstream package.json.
npm install --ignore-scripts
rc=$?
[ "$rc" -eq 0 ] || { echo "ERROR npm install rc=$rc"; exit "$rc"; }

export DEPLOY_ENV=testnet
export L1_RPC_URL
export L2_RPC_URL
export L2B_RPC_URL

node scripts/verify-deploy-wiring.js
VERIFY_RC=$?

echo "VERIFY_EXIT_CODE=$VERIFY_RC"
echo "NOTE=The reviewed 2026-08 run returned 35 passed, 8 failed, exit code 1. A future rerun may differ if public chain state changes."
exit "$VERIFY_RC"
