# Provenance Ledgers

`SHA256SUMS.tsv` is the original repository-wide ledger generated before the August 2026 continuation. It is retained as a historical snapshot and must not be interpreted as a hash manifest for files added or modified after that snapshot.

For the current repository state, regenerate a fresh ledger locally after pulling the target commit:

```bash
bash scripts/regenerate_sha256_ledger.sh
```

The script writes a new dated ledger rather than silently rewriting historical provenance.

## August 2026 review provenance

The August review is pinned to upstream:

`GilgameshCaw/Caw@d7a0e05445f13f268b8e0c60a3d4854cb4b206de`

Critical public-review files include:

- `docs/current_state_update_2026_08_09.md`
- `evidence/gilgamesh_v2_live_wiring_2026_08_v1/findings.md`
- `reproducibility/gilgamesh_v2_live_wiring_2026_08_v1.md`
- `scripts/check_gilgamesh_v2_live_wiring_2026_08.sh`
- `scripts/reproduce_first_party_wiring_verifier_2026_08.sh`
- `reports/claims_matrix_august_2026_addendum.tsv`
- `reports/claims_matrix_august_2026_addendum.md`

A reviewer should pin the peer-review repository commit in addition to checking SHA-256 values because live RPC results can change when upstream testnet deployments change.
