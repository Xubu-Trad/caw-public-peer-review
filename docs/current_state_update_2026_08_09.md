# CAW public peer review — current-state continuation, 2026-08-09

This document continues the May/June public peer review of `GilgameshCaw/Caw`.

The standard has not changed: public build activity is not the same thing as official CAW authority, and planned decentralization is not the same thing as a system whose meaningful human control has already been closed.

## Current bounded conclusion

The strongest current conclusion is:

> The reviewed Gilgamesh V2 testnet is **not trustless today under this review standard**. Meaningful human-controlled authority remains live, while the current testnet deployment also fails multiple first-party wiring checks.

This statement is about the reviewed testnet and current public source/state. It is not a claim that the original CAW token is a scam, that Gilgamesh has committed fraud, or that a final mainnet deployment is already broken.

## Biggest new findings

### 1. Current V2 still has live human-controlled authority

The pinned upstream deploy state records the testnet deployer/operator address as:

`0xF71338f3eAa483aA66125598B09BA1988e694a95`

The V2 `PathwayExpander` contracts are `Ownable` and expose owner-gated additions/configuration surfaces. Public-RPC reproduction checks are included in this repository.

The PathwayExpander design is deliberately narrower than unrestricted ownership: existing peers cannot simply be overwritten and existing configured pathways cannot simply be rewritten. That limitation is real. It does not make the system ownerless while the PathwayExpander owner remains live.

### 2. Upstream still describes the protocol as "trustless and decentralized"

The current V2 README uses that wording as the top-level protocol description.

This review does not treat the description as self-authenticating. It compares that claim with the actual authority surface and deployment state.

### 3. Gilgamesh's own post-deploy verifier rejects the reviewed deployment

The first-party script `solidity/scripts/verify-deploy-wiring.js` is designed to exit `1` if its expected cross-contract wiring does not match chain state.

The preserved review run returned:

`35 passed, 8 failed`

The failed checks span:

- `CawNetworkManager` links,
- L1 Ledger constructor-linked dependencies,
- all three Ledger `cawActions` relationships,
- both cross-chain Ledger L1 peer mappings.

### 4. Both cross-chain Ledgers trust the superseded Profile

The current Profile declared by upstream deploy state is:

`0x61C07717210988df782E779cAc8AC67633Ed2a2e`

Both current L2 Ledgers instead store the superseded Profile:

`0x4F853523102577dDaf5fdbc823EDdCB13b35C543`

as the L1 LayerZero peer.

Direct public-RPC commands to reproduce the stored values are included under `reproducibility/`.

The local audit also tested the LayerZero receive gate directly: the current Profile was rejected and the old Profile passed. That strengthens the finding from "wrong value stored" to "wrong peer actually controls the receive-authentication path" for the tested call surface.

### 5. All three Ledger `cawActions` trust slots are wrong

The first-party verifier and direct reads showed:

- L1 Ledger points to `CawProfileMinter`, not current `CawActions_L1`.
- Base Ledger points to `CawChallengeRelay_L2`, not current `CawActions_L2`.
- Arbitrum Ledger points to `CawActionsArchive_L2b`, not current `CawActions_L2b`.

Those three wrong values exactly match stale `predictedAddresses` collisions preserved in the pinned upstream `.deploy-state.json`.

### 6. The Profile peer root cause was reproduced

The July 24 cascade retained a stale Profile prediction while clearing the corresponding actual deployment address. Constructor selection then consumed the stale predicted value.

Because the peer is one-shot and Ledger ownership is renounced, the resulting wrong peer is not an ordinary mutable admin setting.

### 7. A related future hazard remains in checked-in deploy state

At the pinned V2 commit, `predictedAddresses.CawProfile` is not the live Profile. It is the current `CawProfileLens` address.

The local offline state-transition simulation reproduced a future Profile-cascade hazard if the audited state-clearing/selection behavior is used again without another code/state change.

This is a future-hazard finding, not a claim that the live Profile currently equals the Lens.

### 8. Independent operator review found another real-node redeploy problem

Public PR `GilgameshCaw/Caw#40`, opened by independent operator `yuceeman`, reproduces a stale-database upgrade condition on a real V2 node after the July redeploy.

That finding is separate from the Ledger wiring defects and is useful evidence that independent operators are testing the deployment path in practice.

## What this review does not claim

The evidence does **not** currently prove:

- that Gilgamesh is the original CAW deployer,
- that Gilgamesh was authorized by the original CAW deployer,
- that Enkidu and Gilgamesh are the same person,
- that Enkidu and Gilgamesh coordinated,
- fraudulent intent,
- deliberate concealment,
- insider enrichment,
- a broken final mainnet deployment.

Those remain separate hypotheses or open questions unless direct evidence closes them.

## Current classification

For the reviewed V2 testnet:

- **centralized at the system level under this review standard:** yes;
- **ownerless / fully control-closed:** no;
- **first-party deploy wiring clean:** no;
- **testnet:** yes;
- **official CAW authority proven:** no;
- **fraud proven:** no.

## Plain-language version

A large amount of real software exists. That is not the dispute.

The dispute is that the current build is described as trustless/decentralized while important human-controlled authority remains active, and its own deployment verifier reports multiple wrong contract relationships. Several of those mistakes affect contracts intentionally designed to make important wiring difficult or impossible to repair in place.

The current evidence therefore supports a direct criticism:

> **the claims are ahead of the proof.**

## Reproduction links in this repository

- `evidence/gilgamesh_v2_live_wiring_2026_08_v1/findings.md`
- `reproducibility/gilgamesh_v2_live_wiring_2026_08_v1.md`
- `scripts/check_gilgamesh_v2_live_wiring_2026_08.sh`
