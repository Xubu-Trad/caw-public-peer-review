# Reproducibility Guide

## Goal

A reviewer should be able to reproduce every major claim from public sources and saved artifacts.

The August 2026 review is pinned to upstream V2 commit:

`d7a0e05445f13f268b8e0c60a3d4854cb4b206de`

## Highest-priority current checks

### 1. Live authority and wiring checks

Run:

```bash
bash scripts/check_gilgamesh_v2_live_wiring_2026_08.sh
```

This script is read-only and checks public RPC state for:

- all three PathwayExpander owners,
- the three additional first-party verifier mismatches on L1 (`CawNetworkManager.cawProfile`, `CawNetworkManager.minter`, `CawProfileLedger_L1.cawProfile`),
- both L2 Ledger L1 peer slots,
- all three Ledger `cawActions` trust slots,
- all three Ledger owner-zero states.

A successful reproduction ends with:

`RESULT=REPRODUCED_REVIEW_FINDINGS`

### 2. Re-run Gilgamesh's own deployment verifier

Run:

```bash
bash scripts/reproduce_first_party_wiring_verifier_2026_08.sh
```

The script checks out the exact upstream V2 commit and runs:

`solidity/scripts/verify-deploy-wiring.js`

against the three public testnet RPCs. The reviewed run returned:

`35 passed, 8 failed`

and exit code `1`.

This first-party verifier is important because the failure criteria are defined by Gilgamesh's own deployment tooling, not by this review.

### 3. Detailed August command reference

See:

`reproducibility/gilgamesh_v2_live_wiring_2026_08_v1.md`

It contains the individual `cast call` commands, pinned addresses, expected values, and interpretation limits.

## Historical review checks

### 4. Testsite usage snapshot

The May 2026 review used:

`https://test.caw.social/api/stats`

Observed historical fields included:

- `totalUsers`
- `totalPosts`
- `activeUsersThisWeek`
- `totalCawBurned`

These numbers are a dated snapshot, not asserted here as current August 2026 values.

### 5. cawNAME historical candidate

May 2026 observed candidate:

`0x9fcbb3d6880cd3293f1a731fe6c958a6621a74bf`

Observed at that time on Sepolia:

- name: CAW NAME
- symbol: cawNAME
- totalSupply: 2282
- owner: `0xf71338f3eaa483aa66125598b09ba1988e694a95`

### 6. Acceptance-ratio historical snapshot

The prior ratio calculation used approximately 26,949 CAW holders, 2,281 testsite users, and 958 weekly active users. Those values belong to the earlier review snapshot and should be refreshed before being described as current.

### 7. Historical sync proof status

Current status remains incomplete.

Required proof:

- exact repo commit,
- exact contract addresses,
- exact chain IDs,
- exact start blocks,
- exact RPC assumptions,
- empty DB rebuild command,
- deterministic export hash,
- independent rerun matching the same hash.

## LayerZero status after August review

LayerZero is no longer only a generic unresolved review item. Specific peer and delegate surfaces have now been inspected.

The August findings prove that both current cross-chain Ledgers store the superseded L1 Profile in their L1 peer slot. Direct gate simulation in the local audit further showed current Profile rejected and old Profile accepted for the tested LayerZero receive-authentication path.

Still unresolved for a final production claim:

- final production endpoint/delegate/peer state,
- final DVN/ULN configuration,
- whether all retained authority is renounced or mathematically neutralized,
- final-mainnet bytecode and configuration verification,
- independent historical rebuildability.

## Rule

A read-only RPC result proves the returned chain value at query time. It does not prove motive, identity, fraud, or historical causation by itself. Historical-cause claims require source/state provenance in addition to live reads.
