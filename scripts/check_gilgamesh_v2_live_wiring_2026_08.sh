#!/usr/bin/env bash
set +e
set +o pipefail
LC_ALL=C

SEP="https://ethereum-sepolia-rpc.publicnode.com"
BASE="https://sepolia.base.org"
ARB="https://sepolia-rollup.arbitrum.io/rpc"

DEPLOYER="0xF71338f3eAa483aA66125598B09BA1988e694a95"
OLD_PROFILE="0x4F853523102577dDaf5fdbc823EDdCB13b35C543"
CURRENT_PROFILE="0x61C07717210988df782E779cAc8AC67633Ed2a2e"

PE_L1="0x6c10c9cE2ed0652b046C6C6579E29342723d4d7F"
PE_L2="0xb8e061DB410464e317b9D594Df7697B01A62Af25"
PE_L2B="0xce971284f1f1DC3a0FF650432Fd03A936e7201ce"

LEDGER_L1="0xdbBE199f301AF59f471A586975e2Bc64b57F917f"
LEDGER_L2="0xee2B2E2dE111942b8a1980836894aB1FDa765f24"
LEDGER_L2B="0x7E10b26635fC907774798fd30cB76AD1777A502A"

EXP_ACT_L1="0x5158eD62E9cB57F2Ddd38B2D841589E4033CCcCc"
EXP_ACT_L2="0x106e1895c1aa7D6B044c50d7c7F04a46Ea4CABb7"
EXP_ACT_L2B="0x9e1F62917D9f5D6dc83917565c4e8cbC2BDf6AF2"

fail=0

need_cast() {
  command -v cast >/dev/null 2>&1
  rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "ERROR cast not found"
    return 1
  fi
  return 0
}

norm_addr() {
  printf '%s' "$1" | tr '[:upper:]' '[:lower:]'
}

expect_addr() {
  name="$1"
  actual="$2"
  expected="$3"
  if [ "$(norm_addr "$actual")" = "$(norm_addr "$expected")" ]; then
    echo "PASS $name actual=$actual expected=$expected"
  else
    echo "FAIL $name actual=$actual expected=$expected"
    fail=$((fail + 1))
  fi
}

expect_not_addr() {
  name="$1"
  actual="$2"
  not_expected="$3"
  if [ "$(norm_addr "$actual")" != "$(norm_addr "$not_expected")" ]; then
    echo "PASS $name actual=$actual not_expected=$not_expected"
  else
    echo "FAIL $name actual=$actual not_expected=$not_expected"
    fail=$((fail + 1))
  fi
}

bytes32_tail_addr() {
  v=$(printf '%s' "$1" | sed 's/^0x//')
  tail40=$(printf '%s' "$v" | tail -c 41)
  printf '0x%s' "$tail40"
}

check_owner() {
  name="$1"
  addr="$2"
  rpc="$3"
  actual=$(cast call "$addr" 'owner()(address)' --rpc-url "$rpc" 2>/dev/null)
  rc=$?
  echo "RAW $name owner rc=$rc value=$actual"
  if [ "$rc" -ne 0 ]; then
    fail=$((fail + 1))
    return
  fi
  expect_addr "$name.owner" "$actual" "$DEPLOYER"
}

check_peer_old_profile() {
  name="$1"
  addr="$2"
  rpc="$3"
  raw=$(cast call "$addr" 'peers(uint32)(bytes32)' 40161 --rpc-url "$rpc" 2>/dev/null)
  rc=$?
  echo "RAW $name peer rc=$rc value=$raw"
  if [ "$rc" -ne 0 ]; then
    fail=$((fail + 1))
    return
  fi
  actual=$(bytes32_tail_addr "$raw")
  expect_addr "$name.peer_l1" "$actual" "$OLD_PROFILE"
  expect_not_addr "$name.peer_l1_not_current" "$actual" "$CURRENT_PROFILE"
}

check_caw_actions() {
  name="$1"
  addr="$2"
  rpc="$3"
  expected="$4"
  actual=$(cast call "$addr" 'cawActions()(address)' --rpc-url "$rpc" 2>/dev/null)
  rc=$?
  echo "RAW $name cawActions rc=$rc value=$actual"
  if [ "$rc" -ne 0 ]; then
    fail=$((fail + 1))
    return
  fi
  expect_addr "$name.cawActions_expected" "$actual" "$expected"
}

check_zero_owner() {
  name="$1"
  addr="$2"
  rpc="$3"
  actual=$(cast call "$addr" 'owner()(address)' --rpc-url "$rpc" 2>/dev/null)
  rc=$?
  echo "RAW $name owner rc=$rc value=$actual"
  if [ "$rc" -ne 0 ]; then
    fail=$((fail + 1))
    return
  fi
  expect_addr "$name.owner_zero" "$actual" "0x0000000000000000000000000000000000000000"
}

need_cast || exit 2

echo "TYPE=PUBLIC_RPC_REPRODUCTION"
echo "WRITE_TX=NO"
echo "CHAIN_STATE=READ_ONLY"
echo "UPSTREAM_REF=d7a0e05445f13f268b8e0c60a3d4854cb4b206de"

check_owner "PathwayExpander_L1" "$PE_L1" "$SEP"
check_owner "PathwayExpander_L2" "$PE_L2" "$BASE"
check_owner "PathwayExpander_L2b" "$PE_L2B" "$ARB"

check_peer_old_profile "Ledger_L2" "$LEDGER_L2" "$BASE"
check_peer_old_profile "Ledger_L2b" "$LEDGER_L2B" "$ARB"

# These three checks intentionally compare against the declared current CawActions.
# A FAIL reproduces the wiring mismatch finding.
check_caw_actions "Ledger_L1" "$LEDGER_L1" "$SEP" "$EXP_ACT_L1"
check_caw_actions "Ledger_L2" "$LEDGER_L2" "$BASE" "$EXP_ACT_L2"
check_caw_actions "Ledger_L2b" "$LEDGER_L2B" "$ARB" "$EXP_ACT_L2B"

check_zero_owner "Ledger_L1" "$LEDGER_L1" "$SEP"
check_zero_owner "Ledger_L2" "$LEDGER_L2" "$BASE"
check_zero_owner "Ledger_L2b" "$LEDGER_L2B" "$ARB"

echo "FAIL_COUNT=$fail"
if [ "$fail" -eq 0 ]; then
  echo "RESULT=ALL_EXPECTED_CHECKS_PASSED"
  exit 0
fi

echo "RESULT=ONE_OR_MORE_EXPECTED_CHECKS_FAILED"
exit 1
