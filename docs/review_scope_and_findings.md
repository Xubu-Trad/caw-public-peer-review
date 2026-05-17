# Review Scope and Findings

## Purpose

This document explains the public peer-review position in plain language while preserving technical accuracy.

The review is not trying to stop people from building.

The review is asking whether the Gilgamesh CAW build has met the CAW manifesto standard.

## Plain-English Summary

A testsite can be real and still not be accepted CAW.

A GitHub repo can be active and still not be official CAW.

A builder can write serious code and still not prove decentralization.

An owner can renounce one address and still leave other control paths unresolved.

A protocol can use cross-chain messaging and still need proof that no operator can control the path.

A historical-sync system can sound decentralized and still be unproven until a clean rebuild works from public chain data.

## Finding 1: Testsite usage exists, but usage is not acceptance.

### Status

SUPPORTED that usage exists.

NOT_SUPPORTED that usage proves cawmmunity acceptance.

### Explanation for new holders

If a test app has users, that proves people used or tested the app.

It does not prove the entire CAW holder base reviewed it, accepted it, or approved it as the official protocol.

### Technical review requirement

To support cawmmunity acceptance, the project would need public evidence such as:

- final reviewed contracts,
- public review history,
- accepted GitHub issues or pull requests,
- published deployment addresses,
- verified bytecode,
- broad cawmmunity review,
- reproducible proof that the accepted deployment matches the reviewed source.

## Finding 2: Holder count versus testsite count matters, but it is not a vote.

### Status

SUPPORTED as an adoption-ratio signal.

NOT_SUPPORTED as a final vote.

### Explanation for new holders

If CAW has far more holders than testsite users, then the testsite user base should not be presented as “the cawmmunity has accepted this.”

It is more accurate to say: a subgroup is using or testing it.

### Technical review requirement

A stronger acceptance claim would require:

- current CAW holder count source,
- current testsite user count source,
- active-user methodology,
- wallet-level deduplication if available,
- transparent API responses,
- archived raw evidence,
- repeat measurements over time.

## Finding 3: Renouncing one owner address is not enough.

### Status

NOT_SUPPORTED that one renounce proves decentralization.

### Explanation for new holders

Imagine a building has ten control rooms.

Locking one room does not prove nobody can control the building.

Smart contracts are similar. A review must check every control path.

### Technical review requirement

A complete decentralization review must check:

- `owner()` on every critical contract,
- admin functions,
- proxy admin slots,
- implementation slots,
- upgrade functions,
- multisig authority,
- one-time setters,
- whether one-time setters were consumed,
- whether any setup function remains callable,
- privileged LayerZero/OApp configuration,
- frontend/API/indexer/operator dependencies.

## Finding 4: LayerZero/OApp must be reviewed as a control surface.

### Status

UNPROVEN until directly reviewed.

### Explanation for new holders

Cross-chain messaging is not magic decentralization.

If one operator can control peers, delegates, trusted remotes, endpoint configuration, archive routing, or message verification assumptions, then the system may still have centralized control points.

### Technical review requirement

The review needs:

- endpoint addresses,
- delegate addresses,
- peer configuration,
- trusted remote configuration,
- archive-chain configuration,
- message verification path,
- finality of configuration,
- proof that no human operator can later change critical trust assumptions.

## Finding 5: Independent historical rebuild is still missing.

### Status

UNPROVEN.

### Explanation for new holders

If the claim is “anyone can run a node and recover the record,” then someone must prove it from zero.

Not from Gilgamesh’s database.

Not from Gilgamesh’s API.

Not from a private indexer.

From public chain data.

### Technical review requirement

The clean proof is:

1. start with an empty database,
2. use the public repo,
3. use published chain IDs,
4. use published contract addresses,
5. use published start blocks,
6. sync from public RPC or documented RPC assumptions,
7. export the reconstructed record,
8. hash the export,
9. have another reviewer reproduce the same hash.

Until then, independent recoverability remains unproven.

## Finding 6: Peer review must happen before mainnet acceptance.

### Status

SUPPORTED as manifesto-standard interpretation.

### Explanation for new holders

The manifesto does not describe a builder launching first and asking the cawmmunity to trust them until later.

It warns that people will claim ownership of the process, claim they can do it all, and may write perfect code with a perfect backdoor.

### Technical review requirement

Before calling a deployment manifesto-aligned, reviewers need:

- final source code,
- final deployment addresses,
- verified source on explorers,
- public review of critical contracts,
- public review of protocol architecture,
- public review of LayerZero/OApp assumptions,
- admin/key closure proof,
- no proxy/multisig backdoor proof,
- independent reproducibility proof.

## Final Review Position

The current record supports this balanced conclusion:

GilgameshCaw/Caw is a serious public build with real development activity and testsite usage.

But the evidence does not yet prove official CAW authority, cawmmunity acceptance, final deployment, decentralization, LayerZero/OApp finality, or independent historical recoverability.

The correct status is:

**Under review. Not proven manifesto-complete.**
