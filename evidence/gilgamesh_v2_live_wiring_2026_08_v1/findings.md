# Gilgamesh V2 live wiring and authority update — 2026-08

## Scope

This evidence pack updates the public peer review with the strongest August 2026 findings that can be reproduced from the public `GilgameshCaw/Caw` repository and public testnet RPCs.

This is a testnet deployment-integrity and authority review. It is **not** proof of fraud, malicious intent, official CAW succession, or final-mainnet failure.

## Source pin

- upstream repository: `GilgameshCaw/Caw`
- branch reviewed: `v2`
- commit: `d7a0e05445f13f268b8e0c60a3d4854cb4b206de`
- upstream deploy state file: `solidity/.deploy-state.json`
- upstream first-party verifier: `solidity/scripts/verify-deploy-wiring.js`

## FACT 1 — current repository description says "trustless and decentralized"

The current V2 README describes CAW Protocol as a "trustless and decentralized social clearing-house" and lists `Trustless` and `Decentralized` as current key features.

That wording should be evaluated against the live authority surface, not treated as self-proving.

## FACT 2 — deployer/operator address is recorded in upstream deploy state

Upstream `.deploy-state.json` records:

`deployerAddress = 0xF71338f3eAa483aA66125598B09BA1988e694a95`

This evidence supports calling this the **Gilgamesh testnet deployer/operator address**. It does not prove the real-world identity of the human behind the Gilgamesh pseudonym.

## FACT 3 — PathwayExpander remains an owned authority surface

The upstream V2 `PathwayExpander.sol` is `Ownable` and exposes owner-gated operations including:

- adding peers for previously unused EIDs,
- configuring new LayerZero/DVN pathways,
- adding KYC verifier levels,
- bounded DVN escalation on existing configured pathways.

The design intentionally prevents replacement of existing peers and existing configured pathways, so this is narrower than unrestricted admin control. It is nevertheless still a live human-controlled authority surface until `PathwayExpander.owner()` is neutralized.

## FACT 4 — current deploy-state prediction map contains wrong-contract collisions

At the pinned V2 commit, `.deploy-state.json` records:

| prediction key | persisted predicted address | currently declared contract at that address |
|---|---|---|
| `CawProfile` | `0x4C5f2AD9Fe044bF578FD5EA0B2f35370d21AabA9` | `CawProfileLens` |
| `CawActions_L1` | `0xDA1F1c34Ed283C7aF358Fbb2d2A3A1A27C5Ac1D7` | `CawProfileMinter` |
| `CawActions_L2` | `0x9A3bE72fEe5f5f7b259FB2889e2F65CDf7380D57` | `CawChallengeRelay_L2` |
| `CawActions_L2b` | `0xEb0fD584bd1E5793e7fe9eDA33FCA4BEFd65937f` | `CawActionsArchive_L2b` |

This is first-party repository state and does not depend on interpretation of screenshots or Telegram statements.

## FACT 5 — Gilgamesh includes a first-party post-deployment wiring verifier

`solidity/scripts/verify-deploy-wiring.js` explicitly checks, among other things:

- `CawNetworkManager.cawProfile == CawProfile`
- `CawNetworkManager.minter == CawProfileMinter`
- `CawProfileLedger_L1.cawProfile == CawProfile`
- every Ledger `cawActions == declared CawActions`
- every cross-chain Ledger peer for L1 == current CawProfile
- Ledger owner == zero after constructor renouncement
- LayerZero delegate wiring
- Archive/Relay ownership and peer mesh

The script exits `1` if any check fails.

## FACT 6 — reproduced verifier result is 35 passed / 8 failed

The local evidence run preserved in this review returned:

`Verification complete: 35 passed, 8 failed.`

`VERIFY_EXIT_CODE=1`

The eight failure names were:

1. `CawNetworkManager.cawProfile`
2. `CawNetworkManager.minter`
3. `CawProfileLedger_L1.cawProfile`
4. `CawProfileLedger_L1.cawActions`
5. `CawProfileLedger_L2.cawActions`
6. `CawProfileLedger_L2.peers(L1.eid=40161)`
7. `CawProfileLedger_L2b.cawActions`
8. `CawProfileLedger_L2b.peers(L1.eid=40161)`

Primary verifier-output artifact SHA-256 recorded by the local review:

`e611fee88c0d31b7d9f767cffa4b3cc50940877b1bbf28f5c8d1ea2bff12a957`

The raw local output itself is not embedded in this commit because this update is being written through the GitHub connector. The reproduction script below rechecks the highest-signal live values directly from public RPCs.

## FACT 7 — both current cross-chain Ledgers store the superseded L1 Profile as the L1 peer

Current declared Profile in upstream deploy state:

`0x61C07717210988df782E779cAc8AC67633Ed2a2e`

Superseded Profile from the prior deployment:

`0x4F853523102577dDaf5fdbc823EDdCB13b35C543`

Current Ledgers:

- Base Sepolia: `0xee2B2E2dE111942b8a1980836894aB1FDa765f24`
- Arbitrum Sepolia: `0x7E10b26635fC907774798fd30cB76AD1777A502A`

Direct read-only `peers(40161)` checks resolve to the old Profile on both chains, not the currently declared Profile.

This was independently strengthened in the local review with direct `lzReceive` gate simulations: current Profile rejected; old Profile accepted.

## FACT 8 — all three current Ledgers have wrong `cawActions` trust-slot values

Declared current CawActions contracts:

- L1: `0x5158eD62E9cB57F2Ddd38B2D841589E4033CCcCc`
- Base: `0x106e1895c1aa7D6B044c50d7c7F04a46Ea4CABb7`
- Arbitrum: `0x9e1F62917D9f5D6dc83917565c4e8cbC2BDf6AF2`

Observed / first-party verifier mismatches:

- L1 Ledger `cawActions` -> `0xDA1F1c34Ed283C7aF358Fbb2d2A3A1A27C5Ac1D7` (`CawProfileMinter`)
- Base Ledger `cawActions` -> `0x9A3bE72fEe5f5f7b259FB2889e2F65CDf7380D57` (`CawChallengeRelay_L2`)
- Arbitrum Ledger `cawActions` -> `0xEb0fD584bd1E5793e7fe9eDA33FCA4BEFd65937f` (`CawActionsArchive_L2b`)

These actual values exactly match stale prediction-map collisions preserved in `.deploy-state.json`.

The Ledger `cawActions` slot is not merely descriptive. The reviewed code uses it as an authorization boundary for functions that require the caller to be `cawActions`.

## FACT 9 — the cross-chain Profile peer defect is constructor-time / one-shot in character

The V2 architecture deliberately removes ordinary repair paths from the Ledger:

- cross-chain peer is set into a one-time peer slot,
- Ledger ownership is renounced in the constructor path,
- `PathwayExpander` cannot overwrite an existing peer.

Therefore the wrong stored peer is not a normal mutable setting that can simply be changed in place through ordinary peer administration.

## FACT 10 — historical source/state reproduced the Profile-peer causal chain

The local audit reproduced this sequence for the July 24 cascade:

1. previous `predictedAddresses.CawProfile` survived from old deploy state,
2. redeploy clearing removed `addresses.CawProfile` but did not clear the stale prediction,
3. prediction refresh only occurred when the prediction key was absent,
4. cross-chain Ledger constructor argument preferred the persisted predicted Profile,
5. the replacement Profile was deployed later at a different address,
6. live Ledgers therefore retained the superseded Profile as their one-time L1 peer.

Historical causal-chain audit SHA-256 recorded locally:

`f4e29a9715f5d33b06210e4fbe6078a5424cbdb491ed7223ac1a736ae291bed9`

## FACT 11 — current checked-in deploy state still preserves a future Profile prediction hazard

At the pinned V2 commit:

- current `addresses.CawProfile` = `0x61C07717210988df782E779cAc8AC67633Ed2a2e`
- current `predictedAddresses.CawProfile` = `0x4C5f2AD9Fe044bF578FD5EA0B2f35370d21AabA9`
- that predicted address is the current `CawProfileLens`

The local state-transition simulation showed that a Profile-cascade redeploy following the audited clearing/selection behavior would preserve this wrong prediction absent an outside mutation or code change.

Offline simulation artifact SHA-256 recorded locally:

`094675bbcc2243305323126a78a1218ba0b287d98370df6dcd4eafe221103734`

This is a **future hazard finding**, not a claim that the live current CawProfile is the Lens.

## FACT 12 — independent operator review found a separate real-node stale-deployment problem

Public PR `GilgameshCaw/Caw#40` was opened by `yuceeman` after reproducing a stale-database upgrade condition on a real V2 node following the July redeploy.

The PR states that a pre-guard database with old-contract rows and no epoch stamp could be mistaken for a fresh database and stamped as current. The proposed fix refuses that state unless explicitly bypassed.

This is independent of the Ledger wiring findings above.

## Classification

The current evidence supports these bounded conclusions:

- **FACT:** the reviewed V2 deployment is still testnet.
- **FACT:** material human-controlled authority surfaces remain live.
- **FACT:** the repository currently markets the protocol as trustless/decentralized.
- **FACT:** the first-party wiring verifier rejects the current deployment with eight failures in the reproduced run.
- **FACT:** both cross-chain Ledgers store the old Profile as their L1 peer.
- **FACT:** all three Ledgers have `cawActions` values different from the declared current CawActions deployments.
- **FACT:** current deploy state contains stale/wrong-contract prediction entries.
- **FACT:** the Profile-peer root cause was reproduced as a stale-prediction deployment-state failure.
- **INFERENCE:** the present architecture is best classified as centralized at the system level because meaningful human authority remains live, even though some individual contracts have renounced or constrained control.
- **NOT PROVEN:** fraud, malicious intent, deliberate concealment, official CAW authority, Enkidu/Gilgamesh common identity, or a broken final mainnet deployment.

## Plain-language summary

The current testnet does not merely have unfinished features. Its own deployment-checking logic reports incorrect wiring, and several wrong addresses are baked into contracts designed to make important configuration irreversible. At the same time, important human-controlled authority remains active while the repository describes the protocol as trustless and decentralized.

That is the criticism: **claims, control state, and deployment integrity do not presently line up.**
