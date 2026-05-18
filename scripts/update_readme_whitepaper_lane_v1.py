from pathlib import Path

p = Path("README.md")
text = p.read_text(encoding="utf-8")

block = """
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

"""

if "## Whitepaper Claims Review" not in text:
    anchor = "## Official CAW GitHub Submission"
    if anchor in text:
        text = text.replace(anchor, block + "\n" + anchor)
    else:
        text = text.rstrip() + "\n\n" + block

p.write_text(text, encoding="utf-8")
print("README updated")
