# Whitepaper Claims And Required Proofs

## Purpose

This document records technical claims from:

`https://github.com/GilgameshCaw/Caw/blob/master/docs/WHITEPAPER.md`

The whitepaper is useful because it gives specific claims that can be reviewed.

This document does not treat the whitepaper as proof by itself.

It treats the whitepaper as a specification and claim source.

## Review Boundary

A whitepaper is not deployed bytecode.

A contract on `master` is not a verified deployed contract.

A future renounce is not a current closed control surface.

A design description is not an empty-database rebuild.

The current review position remains:

Under review.

Not proven manifesto complete.

No proof means no authority.

## Whitepaper Claim Set

The whitepaper claims that the protocol is a trustless and decentralized social clearing-house.

It claims the protocol's job is to make the manifesto's claims true in code, not in slogan.

It claims every assertion about durability or censorship resistance reduces to an on-chain fact.

It claims every production contract is renounced post-deploy.

It claims there are no upgradeable proxies.

It claims there is no multisig.

It claims calldata is the source of truth.

It claims indexers reconstruct social state by fetching transaction calldata, validating against `batchHash`, and unpacking actions.

It claims Ethereum mainnet anchors identity, CAW balances, the Network registry, and the price oracle.

It claims L2 chains host action-processing contracts.

It claims archive chains receive long-term optimistic replication of L2 activity.

It claims archive submissions finalize after a two-day challenge window.

It claims any honest observer may slash a fraudulent archive submission.

It claims the PathwayExpander can only call `addPeer()` and cannot call `setPeer()`.

It claims the PathwayExpander can be renounced.

It claims the protocol can extend to new chains through permissionless peer addition but cannot be reconfigured, paused, fee-extracted, or upgraded after final renunciation.

It claims direct messages are end-to-end encrypted and stored off-chain.

It claims validators batch signed actions and submit them to L2.

It claims mirrors index the chain and serve user-facing applications.

It claims the chain is the truth and mirrors are caches.

## Required Proofs

### Deployed Bytecode

Publish final deployed contract addresses for every chain.

Publish verified source.

Publish deployed bytecode hashes.

Publish source-to-bytecode match proof.

### Renounced Ownership

Publish `owner()` results for every Ownable production contract.

Publish renounce transaction hashes.

Publish post-renounce state.

### No Proxies

Publish EIP-1967 admin slot reads.

Publish EIP-1967 implementation slot reads.

Publish proxy-pattern scan results.

Publish upgrade-function review.

### No Multisig

Publish owner and admin address review.

Publish proof that no multisig controls any critical contract.

Publish proof that no privileged operator remains.

### PathwayExpander

Publish the deployed PathwayExpander address.

Publish verified source.

Publish owner state.

Publish allowed function review.

Publish proof it cannot call `setPeer()` or reconfigure existing peers.

Publish renounce proof if renounced.

### LayerZero And OApp Configuration

Publish endpoint addresses.

Publish delegate addresses.

Publish peer configuration.

Publish trusted remote configuration.

Publish archive-chain registration.

Publish message verification path.

Publish config-finality proof.

### Optimistic Archive And Slashing

Publish archive contract addresses.

Publish stake requirements.

Publish challenge window constants.

Publish submission flow.

Publish challenge flow.

Publish slashing proof or test transaction evidence.

### Calldata As Source Of Truth

Publish example L2 transaction hashes.

Publish calldata extraction commands.

Publish `batchHash` validation commands.

Publish unpacking script.

Publish output hash.

### Independent Historical Rebuild

Start from an empty database.

Use public repo.

Use public chain IDs.

Use public deployed addresses.

Use public start blocks.

Use documented RPC assumptions.

Sync from public chain data.

Export the reconstructed record.

Hash the export.

Have another reviewer reproduce the same hash.

### Validators And Mirrors

Publish validator admission rules.

Publish batch submission rules.

Publish queue reconstruction proof.

Publish independent validator setup proof.

Publish mirror indexing proof.

Publish proof that mirrors are caches, not the source of truth.

### Direct Messaging

Publish the DM threat model.

Publish key handling design.

Publish relay trust assumptions.

Publish metadata leakage analysis.

Publish recovery and failure-mode analysis.

## Final Whitepaper Review Position

The whitepaper is a useful technical checklist.

It does not close the review.

The review closes only when the whitepaper claims are verified against final deployed contracts, post-deploy state, public chain data, reproducible scripts, and independent reruns.
