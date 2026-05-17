from pathlib import Path
import csv

DOC = Path("docs/testsite_public_claims_and_required_proofs.md")
DOC.write_text("""# Testsite Public Claims And Required Proofs

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
""", encoding="utf-8")

ALIGN = Path("docs/medium_article_alignment_2026_05_17.md")
ALIGN.write_text("""# Medium Article Alignment Snapshot

## Purpose

This file records how the GitHub peer-review repository maps to the current Medium article titled `A Technical PUBLIC PEER REVIEW of GilgameshCaw/Caw`.

The article adds a stronger section on public claims displayed by `test.caw.social`.

The repo now reflects those article sections through:

- `docs/testsite_public_claims_and_required_proofs.md`
- `reports/claims_matrix.tsv`
- `reports/claims_matrix_readable.md`
- `README.md`
- `ledgers/SHA256SUMS.tsv`

## Article Findings Now Reflected

The repo now reflects these article findings:

1. The testsite makes strong public claims.
2. The testsite describes CAW as decentralized, permissionless, trustless, unstoppable, unbreakable, on-chain, and censorship-resistant.
3. The testsite describes EIP-712 gasless actions and validator batching.
4. The testsite describes LayerZero cross-chain archiving and Arbitrum archive storage.
5. The testsite says complete action history can be reconstructed from blockchain events.
6. The testsite says contracts are immutable and have no admin keys.
7. The testsite says validators and frontends are permissionless.
8. The testsite describes username NFTs and staking economics.
9. The review does not claim those website statements are false.
10. The review says those website statements remain unproven until independently verified.

## Repo Review Boundary

The GitHub record should not overstate.

The correct boundary is:

The website statements are public claims.

They are material.

They require proof.

They do not become established facts merely because they appear on the testsite.
""", encoding="utf-8")

# Update README with link block.
readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
insert = """## Medium Article Alignment

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

"""
anchor = "## Public Trail Matters Too\n"
if insert.strip() not in text:
    if anchor in text:
        text = text.replace(anchor, insert + anchor)
    else:
        text += "\n\n" + insert
readme.write_text(text, encoding="utf-8")

# Append public claim language.
pcl = Path("docs/public_claim_language.md")
pcl_text = pcl.read_text(encoding="utf-8")
pcl_add = """
## Testsite public-claim language

Safe wording:

The testsite makes strong public claims about decentralization, permissionlessness, gasless actions, immutable contracts, no admin keys, LayerZero archiving, Arbitrum storage, and reconstructable action history.

This review does not claim those public statements are false.

This review records that those claims require independent proof.

A website statement is not a verified control-surface audit.

A homepage slogan is not bytecode proof.

A help page is not an empty-database historical rebuild.

Use the testsite claims as review targets, then require contracts, addresses, hashes, commands, and independent reruns.
"""
if "## Testsite public-claim language" not in pcl_text:
    pcl.write_text(pcl_text + pcl_add, encoding="utf-8")

# Update claims matrix.
path = Path("reports/claims_matrix.tsv")
rows = list(csv.DictReader(path.open(newline="", encoding="utf-8"), delimiter="\t"))
existing = {r["claim_id"] for r in rows}

new_rows = [
    ("C20", "Testsite publicly presents CAW as decentralized, permissionless, trustless, unstoppable, unbreakable, on-chain, and censorship-resistant", "SUPPORTED", "The current Medium article records these public testsite claims from test.caw.social and treats them as public claims requiring proof.", "Archive the exact page source or rendered text with timestamp and hash, then verify each technical claim independently."),
    ("C21", "Testsite claim that no single person, entity, or group controls the system", "UNPROVEN", "This is a public website claim. The review has not yet verified every contract, validator, frontend, API, indexer, database, operator, and cross-chain control path.", "Publish final deployed addresses, bytecode verification, owner/admin/proxy/multisig checks, validator admission proof, frontend/API independence proof, and LayerZero/OApp config-finality proof."),
    ("C22", "Testsite claim that contracts are immutable and have no admin keys", "UNPROVEN", "This is a public website claim. Final deployed contract addresses and complete owner/admin/proxy/config review have not yet been proven in the repo.", "Publish all final deployed addresses, verified source, EIP-1967 slot reads, owner/admin calls, upgrade function review, multisig checks, setup proof, and bytecode hashes."),
    ("C23", "Testsite claim that EIP-712 gasless actions are collected by validators and batched on L2", "SUPPORTED", "The current Medium article records the website design claim and the repo already treats validator and TxQueue design as real review subjects.", "Verify deployed signature schema, validator submission path, batch contracts, replay protection, queue behavior, failure persistence, and independent validator operation."),
    ("C24", "Testsite claim that validators are permissionless and can be run by anyone", "UNPROVEN", "This is a public website claim. The repo has not yet proven independent validator admission, operation, censorship resistance, or queue reconstruction.", "Demonstrate a clean independent validator setup, successful batch submission, no allowlist gatekeeping, reproducible queue reconstruction, and bypass path from default validator."),
    ("C25", "Testsite claim that frontends are permissionless and users can use another frontend or contracts directly", "UNPROVEN", "This is a public website claim. The repo has not yet proven a public read/write path independent of the default frontend, API, private indexer, or private database.", "Publish independent frontend build and connect proof, direct contract interaction proof, API independence proof, and canonical record reconstruction proof."),
    ("C26", "Testsite claim that actions are automatically archived via LayerZero to archive chains such as Arbitrum", "UNPROVEN", "This is a public website claim. LayerZero/OApp endpoint, delegate, peer, trusted remote, message verification, and config-finality proofs remain required.", "Publish endpoint/delegate/peer/trusted remote values, archive-chain registration, message verification path, and proof that critical routing/trust config cannot be changed by one operator."),
    ("C27", "Testsite claim that complete action history can be reconstructed from blockchain events", "UNPROVEN", "This is a public website claim. Prior review position remains that empty-database rebuild plus deterministic export hash is missing.", "Publish exact repo commit, chain IDs, contract addresses, start blocks, RPC assumptions, clean DB setup, sync command, export command, export hash, and independent rerun matching hash."),
    ("C28", "Testsite claim that content cannot be censored at the protocol layer", "UNPROVEN", "This is a public website claim. Censorship resistance requires more than storage across chains and must address validators, queues, APIs, indexers, frontends, and direct contract access.", "Prove validator non-exclusion or bypass, queue reconstruction, direct contract access, independent indexing, frontend alternatives, and canonical record availability."),
    ("C29", "Testsite claim that username NFTs control account identity and access", "UNPROVEN", "This is a public website claim. Final ERC-721 contract address, transfer logic, access logic, custody assumptions, and bytecode verification remain required.", "Publish final username NFT contract, verified source, owner/admin/proxy checks, transfer/access review, fee path review, custody review, and deployed bytecode hash."),
    ("C30", "Testsite claim that staking and platform actions distribute CAW to stakers and posters", "UNPROVEN", "This is a public website claim. Contract-level fee flow and accounting verification remain required.", "Publish final staking/economic contracts, verified source, distribution logic, fee recipients, withdrawal logic, accounting tests, and proof parameters cannot be changed by an operator."),
    ("C31", "Testsite statement that CAW has no official socials, partner projects, or further releases beyond the manifesto is relevant to authority review", "SUPPORTED", "The Medium article records this public website statement and applies it as an authority boundary, not as proof of any person identity.", "Archive exact website text with hash and require authority claims to be supported by verifiable signature, onchain action, or permissioned cawdevelopment proof."),
]

for claim_id, claim, status, evidence, required in new_rows:
    if claim_id not in existing:
        rows.append({
            "claim_id": claim_id,
            "claim": claim,
            "status": status,
            "evidence": evidence,
            "required_to_close": required,
        })

with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["claim_id", "claim", "status", "evidence", "required_to_close"], delimiter="\t")
    w.writeheader()
    w.writerows(rows)

# Regenerate readable matrix.
out = Path("reports/claims_matrix_readable.md")
with out.open("w", encoding="utf-8") as f:
    f.write("# Claims Matrix\n\n")
    f.write("This is the human-readable copy of `reports/claims_matrix.tsv`.\n\n")
    f.write("| Claim ID | Claim | Status | Evidence | Required to Close |\n")
    f.write("|---|---|---|---|---|\n")
    for r in rows:
        clean = {k: v.replace("|", "\\|").replace("\n", " ") for k, v in r.items()}
        f.write("| {claim_id} | {claim} | {status} | {evidence} | {required_to_close} |\n".format(**clean))

print(f"WROTE {DOC}")
print(f"WROTE {ALIGN}")
print(f"CLAIMS_ROWS={len(rows)}")
