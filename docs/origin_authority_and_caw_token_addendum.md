# Origin, Authority, and CAW Token Control-Surface Addendum

## Purpose

This addendum records claims from the public article draft titled `THE INVISIBLE BUILDER` and folds them into the peer-review record with strict evidence boundaries.

This file is not a claim that Gilgamesh is malicious.

This file is not a claim that Gilgamesh controls the original CAW token.

This file is a bounded receipt map for:

- CAW token control-surface claims,
- CAW origin-trail claims,
- deployer-message claims,
- Gilgamesh linkage claims,
- testnet-versus-mainnet authority boundaries,
- public GitHub linkage boundaries,
- the no-proof/no-authority rule.

## Finding A: CAW token no-proxy / no-admin / no-runtime-control evidence

### Status

SUPPORTED by the cited local audit receipts, pending independent rerun.

### Claim

The original CAW token contract does not present a typical upgradeable/proxy admin control surface in the reported audit pack.

The reported evidence includes:

- EIP-1967 proxy admin slot equals zero,
- EIP-1967 implementation slot equals zero,
- `delegatecall` flagged false,
- runtime bytecode length reported as 2278,
- runtime SHA-256 reported as `ac5c77c1372337655d8f0257e34feec1ab0506dc8e8e7f034252cba66390bea1`,
- push-aware opcode probe reporting zero executed counts for `CALL`, `CALLCODE`, `DELEGATECALL`, `STATICCALL`, `CREATE`, `CREATE2`, and `SELFDESTRUCT`,
- runtime equality versus the reported similar-match contract.

### Bounded meaning

This cuts against a classic hidden upgrade/admin switch at the CAW ERC20 token-contract level.

It does not prove safety from every market risk, whale risk, liquidity risk, exchange custody risk, offchain risk, or unrelated contract risk.

## Finding B: CAW origin trail is specific and receipt-based

### Status

SUPPORTED by the cited transaction-hash trail, pending independent onchain recheck.

### Claim

The post records a receipt sequence:

1. SHIB deployer-labeled address funded an intermediary.
2. Intermediary funded the A Hunters Dream / CAW deployer.
3. The CAW deployer created the CAW token contract.
4. The deployer later posted the IDM message linking the manifesto Pastebin and `github.com/cawdevelopment`.

### Key anchors recorded

- CAW token: `0xf3b9569f82b18aef890de263b84189bd33ebe452`
- CAW deployer: `0x36B59455AfeEdf0866FE6E775FE7651bbBe3e005`
- CAW creation tx: `0x4d160fb54fbf45ec2c0cc9d6010c2f215b1d448dcf310ce7019eeac70422515c`
- IDM tx: `0x7903adbb7ab03521da9951d63cc9050ee005dfa871ba3f6d3e20d0bb941f5c37`
- Message anchors: `https://pastebin.com/yhcajZq0` and `https://github.com/cawdevelopment`

### Bounded meaning

The origin trail supports the relevance of `cawdevelopment` and the manifesto anchor.

It does not prove Gilgamesh is the original CAW deployer.

## Finding C: “Gilgamesh controls CAW” is not supported by the captured mainnet touchpoint probe

### Status

NOT_SUPPORTED by the presented probe output.

### Claim

The captured probe found:

- 3 transactions for the tested Gilgamesh-linked EOA,
- direct transactions touching CAW deployer/token: empty,
- CAW token transfers involving that address: zero.

### Bounded meaning

The surfaced snapshot does not establish direct mainnet CAW deployer/token control by the tested Gilgamesh-linked EOA.

This does not prove no relationship exists through another wallet, private account, alternate identity, or untested path.

It means the specific direct linkage claim is unproven from the captured evidence.

## Finding D: Base Sepolia owner signals are testnet-limited

### Status

SUPPORTED as testnet ownership evidence; NOT_SUPPORTED as Ethereum mainnet CAW custody evidence.

### Claim

The Base Sepolia probe recorded five contracts where `owner()==0xf71338f3eaa483aa66125598b09ba1988e694a95`.

The same probe did not show rows where `proxy_admin==0xf713...`.

### Bounded meaning

This supports testnet ownership/admin signals for specific Base Sepolia contracts in that probe set.

It does not prove Base mainnet authority.

It does not prove Ethereum mainnet CAW custody.

It does not prove authority over the original CAW ERC20 contract.

## Finding E: Public GitHub checks do not establish official builder status

### Status

NOT_SUPPORTED by the specific public checks shown.

### Claim

The checked public GitHub surfaces did not establish permissioned linkage:

- public org membership endpoint returned HTTP 404 for the tested handle,
- repo-scoped authored issue/PR search returned zero,
- fork lineage was consistent with permissionless copying.

### Bounded meaning

HTTP 404 means public membership was not established by that endpoint.

Zero authored issues/PRs means none were found in that queried scope.

Fork lineage is consistent with permissionless copying.

None of this rules out private membership, alternate accounts, or private authorization.

It means public permissioned linkage was not proven by the specific tests shown.

## Finding F: No proof means no authority by default

### Status

SUPPORTED as a review decision rule.

### Claim

If a person cannot produce minimal, privacy-preserving proof for a claim of authority, the claim should be treated as unproven.

Not proven true.

Not proven false.

Unproven.

### Review consequence

The cawmmunity should not grant custody, admin authority, official status, or decision power based only on voice, lore, popularity, or supporter repetition.

Contributions should be accepted only when they are reproducible, peer-reviewed, and anchored to receipts.

## Final Addendum Position

The CAW token-origin and authority record strengthens the review.

It shows why `cawdevelopment`, the manifesto, and deployer-linked receipts cannot be hand-waved away.

It also keeps the Gilgamesh question bounded:

GilgameshCaw/Caw may be a serious public build.

But current evidence does not prove Gilgamesh controls original CAW, does not prove official CAW authority, and does not prove manifesto-complete decentralization.

The rule remains:

No proof -> no authority.
