# August 2026 Claims Matrix Addendum

This addendum supersedes older claim statuses where the August 2026 evidence is more specific. The original matrix remains preserved as the earlier review snapshot.

| Claim ID | Claim | Status | Current evidence |
|---|---|---|---|
| C43 | Reviewed V2 testnet is system-level decentralized today | CONTRADICTED_BY_EVIDENCE | All three reviewed PathwayExpanders remain owned authority surfaces and tested network authority remains live. |
| C44 | Current V2 deployment wiring is clean | CONTRADICTED_BY_EVIDENCE | Gilgamesh's own verifier returned `35 passed, 8 failed`, exit code `1`, in the preserved review run. |
| C45 | Both current cross-chain Ledgers trust the current L1 CawProfile | CONTRADICTED_BY_EVIDENCE | Base and Arbitrum Ledgers store the superseded Profile as `peers(40161)`. |
| C46 | All current Ledgers trust the declared current CawActions contracts | CONTRADICTED_BY_EVIDENCE | L1 points to Minter, Base to Relay, Arbitrum to Archive instead of declared CawActions. |
| C47 | Wrong Ledger trust addresses are unrelated to upstream prediction state | CONTRADICTED_BY_EVIDENCE | Wrong values exactly match wrong-contract collisions in `predictedAddresses`. |
| C48 | July 24 L2 Profile peer defect is a reproduced stale-prediction deployment-state failure | SUPPORTED | Historical source/state sequence reproduced the stale prediction surviving redeploy clearing and constructor selection. |
| C49 | Current `predictedAddresses.CawProfile` equals live CawProfile | CONTRADICTED_BY_EVIDENCE | It points to `CawProfileLens`, not the live current Profile. |
| C50 | PathwayExpander only adds peers | CONTRADICTED_BY_EVIDENCE | Current source also has owner-only KYC-verifier addition, new-pathway configuration, and bounded DVN escalation. |
| C51 | PathwayExpander gives unrestricted arbitrary admin control | NOT_SUPPORTED | Current source deliberately constrains peer/pathway replacement and has no generic arbitrary-execute surface in the reviewed contract. |
| C52 | `0xF713...` is proven to be the real-world human Gilgamesh | NOT_SUPPORTED | It is a testnet deployer/operator address in upstream state; human identity is not cryptographically established. |
| C53 | `0xF713...` is the reviewed V2 testnet deployer/operator address | SUPPORTED | Upstream `.deploy-state.json` records it as `deployerAddress`; reviewed authority surfaces resolve to it. |
| C54 | August findings prove fraud, malicious intent, Enkidu/Gilgamesh common identity, or insider enrichment | NOT_SUPPORTED | Current evidence establishes control and deployment-integrity facts, not motive/identity/economic allegations. |
| C55 | Reviewed defects prove a broken final mainnet deployment | NOT_SUPPORTED | The reviewed deployment is testnet. |

## Important supersessions

Older `UNPROVEN` wording should not be read as the current status where the August addendum has now produced direct contradictory evidence. In particular:

- broad no-controller/no-admin descriptions are contradicted for the reviewed testnet by live owned authority surfaces;
- the old generic LayerZero uncertainty is now supplemented by direct peer-state and receive-gate evidence;
- the statement that PathwayExpander only adds peers is contradicted by the current source surface;
- older statements implying V2 was not yet deployed are historical and no longer describe the August testnet state.

## Boundaries

The addendum does not promote fraud, deliberate concealment, official CAW succession, common identity, insider enrichment, or final-mainnet failure without direct proof.
