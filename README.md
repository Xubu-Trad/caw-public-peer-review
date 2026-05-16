# CAW Public Peer Review Record

## Scope

This repository is a public peer-review record for comparing the Gilgamesh CAW build against the CAW manifesto standard.

This is not an official decree. CAW has no leader.

This repo exists to preserve evidence, commands, logs, hashes, and reproducible findings so the cawmmunity can review the facts in public.

## Core Question

Has the Gilgamesh build been publicly reviewed, accepted, and proven compatible with the CAW manifesto standard?

Current status: **not proven**.

## Manifesto Standard

The CAW manifesto warns:

> It is strongly recommended that a peer group is formed to develop and review smart contracts.

It also warns:

> as there is no leader in this process, all types will attempt to claim ownership of the process.

And:

> there will those everso helpful who claim to be able to 'do it all' but will write the perfect code with the perfect backdoor

The acceptance standard is:

> Only a cawmmunity reviewed and accepted contract on a public github will be acceptable

## Current High-Level Findings

- Gilgamesh testsite usage exists.
- Usage is not the same as cawmmunity acceptance.
- CAW holder count is much larger than testsite user count.
- Renouncing one owner address is not sufficient proof of decentralization.
- LayerZero/OApp trust assumptions must be reviewed directly.
- Independent historical rebuild is not proven until an empty database can be rebuilt from public chain data and exported with deterministic hashes.
- Peer review must happen before mainnet acceptance, not after.

## Proof Pack Structure

- `docs/` — narrative summaries and public report drafts
- `evidence/` — raw facts, copied outputs, screenshots, receipts
- `scripts/` — reproducible scripts used for analysis
- `reports/` — generated TSV/JSON/Markdown reports
- `logs/` — command outputs
- `ledgers/` — provenance ledger and sha256 records
- `issues/` — public review questions and open findings
- `reproducibility/` — exact commands for independent reruns

## Rule

No claim is accepted without a reproducible artifact, command, hash, or source receipt.
