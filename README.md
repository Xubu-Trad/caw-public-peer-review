# CAW Public Peer Review Record

## Scope

This repository is a public, reproducible peer-review record comparing the Gilgamesh CAW build against the CAW manifesto standard.

This is not an official decree. CAW has no leader.

This repo exists to preserve evidence, commands, logs, hashes, current claims, unresolved questions, and reproducible findings so the cawmmunity can review the facts in public.

The goal is not to replace cawmmunity review.

The goal is to force the review into the open.

## Core Question

Has the Gilgamesh build been publicly reviewed, accepted, deployed, and proven compatible with the CAW manifesto standard?

Current status: **not proven manifesto-complete**.

## Manifesto Standard Used Here

The CAW manifesto sets a higher bar than “someone wrote code” or “a testsite has users.”

The review standard used here is:

1. public GitHub source,
2. public peer review before final acceptance,
3. cawmmunity review and acceptance,
4. verified deployed bytecode matching reviewed source,
5. deployer/admin keys renounced or mathematically neutralized,
6. no multisig control surface,
7. no upgradeable proxy control surface,
8. no hidden owner/admin/config path,
9. no single builder, frontend, indexer, validator, API, database, or operator stack that can practically shape the record alone,
10. reproducible historical recovery from public chain data.

## Origin And Authority Receipts Matter

This review also includes an origin and authority addendum.

That addendum separates the original CAW token and deployer receipt trail from GilgameshCaw/Caw app claims.

The current bounded position is:

- the original CAW token no-proxy/no-admin evidence matters,
- the CAW deployer-message trail to the manifesto and `cawdevelopment` matters,
- current evidence does not prove Gilgamesh controls the original CAW token or deployer,
- Base Sepolia ownership signals do not prove Ethereum mainnet CAW custody,
- public GitHub surface checks do not prove official builder status,
- no proof means no authority by default.

See:

- `docs/origin_authority_and_caw_token_addendum.md`

## Medium Article Alignment

The current Medium article adds a detailed section on public claims displayed by `test.caw.social`.

Those claims are now mapped into this repo in:

- `docs/testsite_public_claims_and_required_proofs.md`
- `docs/medium_article_alignment_2026_05_17.md`

The review boundary is simple:

The testsite claims are public claims.

They are material.

They require proof.

They are not treated as false.

They are treated as unproven until independently verified.

## Public Trail Matters Too

This review is mostly technical, but it does not ignore public history.

Gilgamesh's public statements, supporter claims, references to Maker, leader-style language, and centralized build posture are relevant governance-context evidence because the manifesto itself warns that people will attempt to claim ownership of a leaderless process.

This public trail does not prove criminal intent or official authority by itself.

It does show why the cawmmunity should require receipts instead of assurances.

See:

- `docs/public_trail_and_governance_context.md`

## Current High-Level Findings

### 1. Gilgamesh testsite usage exists.

The review does not deny usage.

The testsite has shown measurable activity, and that matters as evidence that people are testing or using the system.

But testsite usage is only usage evidence. It is not the same thing as cawmmunity acceptance, final protocol approval, or manifesto compliance.

### 2. Usage is not cawmmunity acceptance.

A public app can have users while still failing the manifesto standard.

For this review, acceptance requires public review, accepted final contracts, deployment verification, and evidence that the cawmmunity broadly accepts the protocol as CAW.

A testsite user count alone does not prove that.

### 3. CAW holder count is much larger than Gilgamesh testsite user count.

The current review treats holder count versus testsite users as an adoption-ratio signal, not as a final vote.

The ratio is relevant because it helps test the claim that Gilgamesh’s build has already been accepted by the cawmmunity.

Current evidence supports the narrower claim: a subgroup is using or testing the system.

Current evidence does not support the broader claim: the cawmmunity has accepted it as CAW.

### 4. Renouncing one owner address is not sufficient proof of decentralization.

Renouncing a single owner address may close one control path.

It does not automatically prove the system is decentralized.

A proper review must check every critical contract and every critical control surface, including:

- owner roles,
- admin roles,
- proxy or upgrade paths,
- multisig authority,
- one-time setup functions,
- unconsumed setup functions,
- privileged configuration functions,
- LayerZero/OApp delegate and peer configuration,
- frontend/API/indexer/operator dependency.

The question is not only “was ownership renounced?”

The question is: **can any human operator still shape, censor, redirect, upgrade, configure, or selectively reconstruct the protocol path?**

### 5. LayerZero/OApp trust assumptions must be reviewed directly.

LayerZero/OApp architecture can be useful, but it introduces specific cross-chain trust and configuration questions.

Those questions cannot be waved away with “wait until renounce.”

The review must verify:

- endpoint addresses,
- delegates,
- peers,
- trusted remotes,
- message verification path,
- archive-chain registration,
- cross-chain configuration finality,
- whether any operator can change routing or message trust assumptions.

LayerZero is not automatically disqualifying by name alone.

But LayerZero/OApp use is also not automatically manifesto-compatible.

It must be proven.

### 6. Independent historical rebuild is not proven until a clean rebuild works.

A protocol claiming permanent, recoverable public records must prove that the record can be rebuilt from public data.

The minimum acceptable proof is:

empty database -> public repo -> public contracts -> public chain data -> deterministic sync -> deterministic export hash

The required proof should include:

- exact repo commit,
- exact chain IDs,
- exact contract addresses,
- exact start blocks,
- exact RPC assumptions,
- exact command sequence,
- database initialization steps,
- export command,
- final export hash,
- independent rerun producing the same hash.

Until that exists, “historical sync works” remains unproven as a decentralization claim.

### 7. Peer review must happen before manifesto-aligned acceptance, not after.

The manifesto standard is not “launch first and review later.”

The standard is public GitHub, public review, cawmmunity acceptance, correct deployment, and then key renouncement or neutralization.

A technical mainnet launch without completed public review does not become manifesto-aligned simply because it exists.

## Proof Pack Structure

This repo is organized so another reviewer can inspect claims without relying on Telegram screenshots or private explanations.

### `docs/`

Narrative summaries, public report drafts, review standards, and human-readable explanations.

Use this folder when you want to understand the argument.

### `evidence/`

Copied proof artifacts from local audits, including raw reports, receipts, and prior generated outputs.

Use this folder when you want to inspect the underlying evidence behind a claim.

### `scripts/`

Reproducible scripts used or intended for analysis.

Use this folder when you want to rerun a test instead of trusting a summary.

### `reports/`

Generated TSV, JSON, Markdown, and text reports.

Use this folder when you want the current claim matrix, current GitHub state, audit summaries, or generated findings.

Important files:

- `reports/claims_matrix.tsv`
- `reports/claims_matrix_readable.md`
- `reports/verified_facts.md`
- `reports/current_state_amendment_2026_05_16.md`
- `reports/current_github_state_v1.txt`

### `logs/`

Command outputs and execution logs.

Use this folder to check what was actually run and what the terminal returned.

### `ledgers/`

SHA-256 provenance records.

Use this folder to verify file integrity and detect later edits.

Main file:

- `ledgers/SHA256SUMS.tsv`

### `issues/`

Public review questions and open findings.

Use this folder for structured questions that should become GitHub issues or peer-review tasks.

### `reproducibility/`

Exact commands and rerun instructions for independent reviewers.

Use this folder when trying to reproduce the review from a clean environment.

## Rule

No claim is accepted because it sounds convincing.

A claim is only accepted when it has at least one of the following:

- reproducible command output,
- contract address,
- transaction hash,
- verified source link,
- deterministic script,
- generated report,
- SHA-256 ledger entry,
- public GitHub record,
- public chain data,
- independently repeatable proof.

If a claim cannot be reproduced, it stays marked as **UNPROVEN**, **NOT_SUPPORTED**, or **INFERENCE**.

## Current Conclusion

GilgameshCaw/Caw appears to be a serious public community build under review.

That does not prove it is official CAW.

That does not prove cawmmunity acceptance.

That does not prove manifesto completion.

That does not prove decentralization.

The current review position is:

**Under review.

Not proven manifesto complete.

No proof means no authority.

The record has been submitted to the official CAW GitHub for acceptance, rejection, or correction.**

Show the proof. Hash the artifacts. Review in public. Correct what is wrong.



## Whitepaper Claims Review

The GilgameshCaw/Caw whitepaper is now recorded as a technical claim source.

The whitepaper is useful because it gives specific claims that can be tested.

It is not treated as proof by itself.

Whitepaper claims are tracked in:

- `docs/whitepaper_claims_and_required_proofs.md`
- claims `C32` through `C42` in `reports/claims_matrix_readable.md`

The review boundary is:

A whitepaper is not deployed bytecode.

A contract on `master` is not a verified deployed contract.

A future renounce is not a current closed control surface.

A design description is not an empty-database rebuild.


## Official CAW GitHub Submission

The peer-review record has been formally submitted to the CAW GitHub for acceptance, rejection, or correction.

Issues were disabled on `cawdevelopment/CawUsernames`, so the submission was made by pull request.

Official submission:

- `https://github.com/cawdevelopment/CawUsernames/pull/5`

Submission receipt:

- `reports/official_caw_github_pr_submission_v1.txt`

Current submission status:

- submitted by pull request
- pending acceptance, rejection, or correction

