from pathlib import Path
import csv

src = Path("reports/claims_matrix.tsv")
out = Path("reports/claims_matrix_readable.md")

rows = list(
    csv.DictReader(
        src.open(newline="", encoding="utf-8"),
        delimiter="\t"
    )
)

with out.open("w", encoding="utf-8") as f:
    f.write("# Claims Matrix\n\n")
    f.write("This is the human-readable copy of `reports/claims_matrix.tsv`.\n\n")
    f.write("| Claim ID | Claim | Status | Evidence | Required to Close |\n")
    f.write("|---|---|---|---|---|\n")

    for r in rows:
        clean = {}
        for k, v in r.items():
            clean[k] = v.replace("|", "\\|").replace("\n", " ")

        f.write(
            "| {claim_id} | {claim} | {status} | {evidence} | {required_to_close} |\n".format(
                **clean
            )
        )

print(f"rendered rows: {len(rows)}")
