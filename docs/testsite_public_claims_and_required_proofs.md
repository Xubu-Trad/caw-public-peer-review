# Testsite Public Claims And Required Proofs

## Purpose

This document records public claims displayed on `test.caw.social` and aligns them with the CAW public peer-review record.

This document does not claim the website statements are false.

This document records that the statements are material technical and governance claims that require independent proof before they can be treated as manifesto-complete.

## Public Claims Recorded

The public testsite presents CAW as a decentralized, permissionless, trustless, unstoppable, unbreakable, on-chain, censorship-resistant social network.

The help and resources text describes CAW as a decentralized social protocol built on blockchain smart contracts, designed as a trustless social clearing house focused on freedom of speech, where no single person, entity, or group has ultimate control over the system.

The testsite states that CAW uses EIP-712 signature-based transactions for gasless social interactions.

It states that when users post, like, or follow, they sign a message off-chain with their wallet.

It states that validators collect these signatures and batch them into on-chain transactions on L2 networks such as Base.

It states that all actions are automatically archived to multiple blockchain networks through LayerZero cross-chain messaging.

It states that data is stored on both the L2 network and archive chains such as Arbitrum.

It states that if one storage chain goes offline or censors content, the data remains accessible on other archive chains.

It states that as long as at least one archive chain remains accessible, complete action history can be reconstructed from blockchain events.

It states that contracts are immutable and have no admin keys.

It states that anyone can verify the data, run their own client, or build alternative frontends.

It states that validators and frontends are permissionless and can be run by anyone.

It states that frontends may implement their own content moderation policies, but users blocked on one frontend can access CAW through another frontend or directly through contracts.

It states that users burn CAW tokens through a smart contract to mint an NFT username.

It states that the username NFT becomes the user account identity.

It states that staking CAW allows users to perform platform actions such as posting, liking, and recawing.

It states that CAW spent on the platform is distributed to participants, including stakers and original posters.

It states that CAW has no official socials, partner projects, or further releases beyond what was described in the manifesto.

## Required Proofs

### No Single Controller

Required proof includes deployed contract addresses, verified source, bytecode matches, owner checks, admin checks, proxy checks, multisig checks, setup-function review, validator admission review, API/indexer review, frontend independence review, and LayerZero/OApp configuration review.

### Immutable Contracts And No Admin Keys

Required proof includes final deployed addresses, verified source, owner/admin calls, EIP-1967 slot reads, proxy admin slot checks, implementation slot checks, upgrade function review, multisig review, consumed setup proof, and proof that no critical configuration path remains open.

### Permissionless Validators

Required proof includes validator admission rules, batch submission rules, queue reconstruction, failure persistence, censorship-resistance tests, and proof that a new independent validator can operate without approval from one operator.

### Permissionless Frontends

Required proof includes public read path, public write path, documented validator/API connection path, independent frontend build instructions, and proof that the record can be viewed or reconstructed without one default frontend, private API, private database, or private indexer.

### LayerZero Archiving And Arbitrum Storage

Required proof includes endpoint addresses, delegate addresses, peer configuration, trusted remote configuration, archive-chain registration, message verification path, config-finality proof, and proof that no operator can later change critical routing or trust assumptions.

### Reconstructable Action History

Required proof requires an empty database rebuild using public repo, public chain IDs, public contract addresses, public start blocks, documented RPC assumptions, deterministic sync commands, deterministic export, and independent matching export hash.

### Censorship Resistance

Required proof must address more than storage. It must show that validators cannot silently exclude actions, queues can be independently reconstructed, default APIs cannot define the record, indexers cannot hide canonical actions, and users can bypass default frontends.

### Username NFT Account Identity

Required proof includes final ERC-721 contract address, verified source, owner/admin review, transfer logic review, access assumption review, fee path review, custody review, and deployed bytecode match.

### Staking And Fee Flow

Required proof includes final contract addresses, verified source, accounting logic, distribution logic, fee recipients, withdrawal logic, and proof that no operator can alter distribution parameters.

### No Official Socials Or Partner Projects Beyond Manifesto

This is a website claim that is also relevant to authority review. If true, later authority claims require independent receipts such as a verifiable signature, onchain action, or permissioned cawdevelopment proof. Social repetition is not enough.

## Review Boundary

The review does not claim the testsite statements are false.

The review records that they are strong public claims.

The current repo position is that these claims remain unproven until independently verified with public receipts, reproducible commands, deployed addresses, source verification, hashes, and chain data.

## Summary

The testsite makes strong claims.

Those claims are now part of the review record.

A website statement is not enough.

Show the contracts. Verify the bytecode. Close the control paths. Prove the rebuild.
