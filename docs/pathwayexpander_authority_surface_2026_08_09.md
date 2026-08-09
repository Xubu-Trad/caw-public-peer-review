# PathwayExpander authority-surface clarification — 2026-08-09

Pinned upstream:

`GilgameshCaw/Caw@d7a0e05445f13f268b8e0c60a3d4854cb4b206de`

## Finding

The reviewed `PathwayExpander.sol` is not accurately summarized by the statement that it can "only add peers."

The current contract exposes owner-gated operations for:

1. `addPeer` / `addPeers` — add a peer only where the target OApp peer slot is still zero;
2. `addKycVerifier` — add a new KYC verifier level through the Minter's additions-only interface;
3. `configureNewPathway` — configure ULN/DVN settings for a previously unconfigured `(oapp, lib, eid)` pathway;
4. `addDvnToPathway` — perform a bounded two-step DVN escalation on an already configured pathway.

## Important constraint

This is not equivalent to arbitrary unrestricted admin control.

The reviewed source deliberately blocks or constrains several actions:

- an existing peer cannot be replaced through `addPeer`;
- an already configured pathway cannot be rewritten through `configureNewPathway`;
- DVN escalation follows a fixed bounded sequence and cannot remove/reorder existing DVNs through the reviewed function;
- no generic arbitrary `execute(address,bytes)` surface was found in the reviewed contract;
- the contract can itself renounce ownership.

## Documentation inconsistency

The contract header describes leaving the door open for "TWO specific operations": adding peers for new EIDs and configuring DVN/ULN settings for new pathways.

The implemented owner-only surface is broader than those two categories because it also includes KYC-verifier addition and bounded DVN escalation.

That does not prove malicious intent. It does mean public descriptions of the authority surface should enumerate the actual callable functions rather than reduce the contract to "only add peers."

## Review classification

- **FACT:** PathwayExpander is an owned authority surface at the reviewed deployment.
- **FACT:** its authority is narrower than unrestricted OApp ownership.
- **FACT:** its owner-only surface includes more than peer addition.
- **NOT SUPPORTED:** a claim that it provides arbitrary unrestricted admin execution.
- **NOT SUPPORTED:** a claim that it is ownerless while `owner()` remains nonzero.
