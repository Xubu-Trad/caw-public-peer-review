# Gilgamesh Claim Check Addendum

This document mirrors the committed claim-check evidence summary for public review.

# Gilgamesh Claim Check Summary V1

generated_utc: `2026-06-06T04:38:18Z`

## Repo Anchor

- head: `e7d55bf5e436eb52baf5e8592e6b1fdf60989305`
- top_commit: `e7d55bf5 (HEAD -> master, origin/master, origin/HEAD) fix(profile-l2): inline one-shot guard on setERC1271Sibling (was 94 bytes over EIP-170)`

## Findings

| claim | status | finding |
|---|---|---|
| independent validators live | UNVERIFIED | requires wallet txs, live node evidence, RPC separation, and reproducible logs |
| 3 validator wallets | UNVERIFIED | no on-chain or runtime proof captured yet |
| 3 RPCs | UNVERIFIED | no sanitized runtime config captured yet |
| no validator allowlist | SOURCE_SUPPORTED_NARROW | CawActions source excerpt gates validatorId by cawProfile.ownerOf(validatorId), not by observed owner/admin allowlist. Deployed bytecode and runtime state remain unverified. |
| PathwayExpander no setDelegate | SOURCE_SUPPORTED | no setDelegate observed in captured source excerpt |
| PathwayExpander no setPeer | MISLEADING_AS_STATED | no external setPeer, but addPeer/addPeers internally call setPeer for new eids |
| V2 testnet deployment | UNVERIFIED | addresses exist in deployments.ts, but no RPC code/owner probe was completed |
| Etherscan verification | FUTURE_OR_UNVERIFIED | verify after final deployment |
| renounce txs | FUTURE_OR_UNVERIFIED | verify after tx hashes exist |
| one-command rebuild | FUTURE_OR_UNVERIFIED | verify after clean-machine command exists and passes |

## Validator Gate Verdict

```text
VALIDATOR_GATE_VERDICT_V1

VERDICT=LIKELY_PROFILE_EXISTENCE_GATE

TERMS_FOUND=none

SCOPE=CawActions.sol _requireValidatorExists source excerpt only.
DOES_NOT_PROVE=live independent validators, deployed-bytecode match, runtime state, RPC separation.
```

## PathwayExpander Finding

```text
PATHWAYEXPANDER_CLAIM_FINDING_V1

CLAIM:
PathwayExpander has no setPeer or setDelegate.

SOURCE:
repo/Caw/solidity/contracts/PathwayExpander.sol

FINDING_SETDELEGATE:
SUPPORTED_BY_STATIC_SCAN

DETAIL:
No setDelegate function or delegate rotation call was observed in the captured PathwayExpander source excerpt.

FINDING_SETPEER:
MISLEADING_AS_STATED

DETAIL:
PathwayExpander does not expose an external function named setPeer.
However, it defines IOAppOwner.setPeer(uint32 eid, bytes32 peer) and internally calls o.setPeer(eid, peer) inside _addPeer().

The owner-facing functions are addPeer() and addPeers(), both gated by onlyOwner.

The contract checks that o.peers(eid) == bytes32(0), so the captured source indicates an additions-only model for new eids, not reconfiguration of already-set peers.

CONTROL_SURFACE:
PathwayExpander remains an owner-controlled peer expansion path until its own ownership is renounced.

REQUIRED_TO_CLOSE:
Verify deployed PathwayExpander address.
Verify deployed bytecode matches reviewed source.
Verify owner() state.
Verify whether ownership was renounced.
Verify OApp owner() states.
Verify peers(eid) state for every supported eid.
Verify no setDelegate path exists in deployed bytecode or inherited reachable code.
```

## Provenance

- `reports/current_head.txt` sha256 `f5437e0f305c6799abd10d9c2fb3102e77e0b1d00d6901e999eeb8c4b89f89e3` size `41`
- `reports/recent_commits_80.txt` sha256 `02c3a7e7ff6ef1d62e0518826dee37775c42dbf2627016e7904db0f124b22ddf` size `6201`
- `reports/pathwayexpander_source_excerpt.txt` sha256 `a0ef3bfa1721e7d1f4a7ee3f8726bf3aaed036f1305e7434bf7faad26b73c6b9` size `4135`
- `reports/pathwayexpander_claim_finding_v1.txt` sha256 `5d08f9fd67135000f0667b43efe270175efb2b364b9e5764a4df922f6cd42ead` size `1258`
- `reports/require_validator_exists_excerpt.txt` sha256 `eaa4977e1fc5b89ec47d6e6f27479861cc99480e48e56eb03ed930c5d0fee13f` size `2156`
- `reports/validator_gate_verdict_v1.txt` sha256 `2eb433dcdad90c6842d5e5368504058de2aae07c697b2f054a4016de1d163752` size `250`
- `reports/extracted_addresses.tsv` sha256 `b1773400037607736399aff46bf13d38aa22a0511a53b08ab16ae6ea7061828c` size `1353`
