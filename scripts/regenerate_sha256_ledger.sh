#!/usr/bin/env bash
set +e
set +o pipefail
LC_ALL=C

ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
rc=$?
if [ "$rc" -ne 0 ] || [ -z "$ROOT" ]; then
  echo "ERROR not inside a git repository"
  exit 2
fi

cd "$ROOT" || exit 2
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
OUT="ledgers/SHA256SUMS_${STAMP}.tsv"
TMP="${OUT}.tmp"

printf 'path\tsha256\tsize_bytes\n' > "$TMP"

git ls-files -z | while IFS= read -r -d '' f; do
  case "$f" in
    ledgers/SHA256SUMS_*.tsv) continue ;;
  esac
  [ -f "$f" ] || continue
  h=$(sha256sum "$f" | awk '{print $1}')
  s=$(wc -c < "$f" | tr -d ' ')
  printf '%s\t%s\t%s\n' "$f" "$h" "$s" >> "$TMP"
done

mv "$TMP" "$OUT"
sha256sum "$OUT" > "${OUT}.sha256"

echo "WROTE=$OUT"
echo "LEDGER_SHA256=$(awk '{print $1}' "${OUT}.sha256")"
echo "NOTE=Commit both the ledger and its .sha256 sidecar if you want this snapshot preserved in Git."
