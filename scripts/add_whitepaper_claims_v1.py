from pathlib import Path
import csv

path = Path("reports/claims_matrix.tsv")

rows = list(
    csv.DictReader(
        path.open(newline="", encoding="utf-8"),
        delimiter="\t"
    )
)

existing = {r["claim_id"] for r in rows}

new_rows = [
    {
        "claim_id": "C32",
        "claim": "Whitepaper claims every durability and censorship-resistance assertion reduces to an on-chain fact",
        "status": "SUPPORTED",
        "evidence": "GilgameshCaw/Caw WHITEPAPER.md states that every assertion about durability or censorship-resistance reduces to an on-chain fact.",
        "required_to_close": "For each whitepaper assertion, publish the deployed address, transaction, bytecode, command, hash, or chain data that proves it."
    },
    {
        "claim_id": "C33",
        "claim": "Whitepaper claims every production contract is renounced post-deploy",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that every production contract is renounced post-deploy, but final deployed V2 state has not yet been verified in this review.",
        "required_to_close": "Publish production addresses, owner() results, renounce transaction hashes, and post-renounce state for every Ownable contract."
    },
    {
        "claim_id": "C34",
        "claim": "Whitepaper claims no upgradeable proxies and no multisig",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that CAW contracts are not behind transparent or UUPS proxies and that no multisig controls the protocol.",
        "required_to_close": "Publish EIP-1967 slot reads, proxy scans, upgrade-function review, owner/admin review, and multisig-control review for final deployed contracts."
    },
    {
        "claim_id": "C35",
        "claim": "Whitepaper claims calldata is the source of truth",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that action bytes live in transaction calldata and indexers reconstruct social state by fetching calldata and validating batchHash.",
        "required_to_close": "Publish example transaction hashes, calldata extraction commands, batchHash validation scripts, unpacked outputs, and output hashes."
    },
    {
        "claim_id": "C36",
        "claim": "Whitepaper claims PathwayExpander can only add peers and cannot reconfigure existing peers",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that PathwayExpander can only call addPeer(), cannot call setPeer(), and can itself be renounced.",
        "required_to_close": "Publish deployed PathwayExpander address, verified source, allowed function review, owner state, and renounce proof if renounced."
    },
    {
        "claim_id": "C37",
        "claim": "Whitepaper claims LayerZero archive replication with a two-day challenge window",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that archive chains receive optimistic replication of L2 activity finalized after a two-day challenge window.",
        "required_to_close": "Publish archive contract addresses, constants, endpoint configuration, submission flow, challenge flow, and finality proof."
    },
    {
        "claim_id": "C38",
        "claim": "Whitepaper claims fraudulent archive submissions can be slashed",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md states that any honest observer may slash fraudulent archive submissions for the validator's full stake.",
        "required_to_close": "Publish slashing contract addresses, stake ledger, challenge commands, proof format, and test or live slashing evidence."
    },
    {
        "claim_id": "C39",
        "claim": "Whitepaper claims complete history can be reconstructed from calldata and events",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md describes the chain as truth and mirrors as caches, with reconstruction from transaction calldata and events.",
        "required_to_close": "Publish empty-database rebuild commands, chain IDs, start blocks, deployed addresses, export command, export hash, and independent matching rerun."
    },
    {
        "claim_id": "C40",
        "claim": "Whitepaper claims validators and mirrors do not require central coordination",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md describes mirrors indexing the chain and validators submitting batches, but independent operation remains to be proven.",
        "required_to_close": "Publish independent validator setup proof, mirror setup proof, queue reconstruction proof, batch submission proof, and failure-mode review."
    },
    {
        "claim_id": "C41",
        "claim": "Whitepaper claims session keys are bounded and cannot delegate withdraw",
        "status": "UNPROVEN",
        "evidence": "WHITEPAPER.md describes Quick Sign session keys with scope bitmap, spend limit, expiry, epoch, and permanent withdraw exclusion.",
        "required_to_close": "Publish final contract address, verified source, tests for withdraw exclusion, spend limits, expiry, revocation, replay protection, and transfer invalidation."
    },
    {
        "claim_id": "C42",
        "claim": "Whitepaper is a specification and claim source until final deployed bytecode and post-deploy state are verified",
        "status": "SUPPORTED",
        "evidence": "The whitepaper states testable design claims, but current public statements indicate V2 contracts were not yet deployed and Etherscan verification would occur after deployment.",
        "required_to_close": "Verify final deployed V2 contracts, bytecode, owner/admin state, proxy status, LayerZero config, archive behavior, and independent rebuild outputs."
    },
]

for row in new_rows:
    if row["claim_id"] not in existing:
        rows.append(row)

with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "claim_id",
            "claim",
            "status",
            "evidence",
            "required_to_close",
        ],
        delimiter="\t"
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"claims rows: {len(rows)}")
