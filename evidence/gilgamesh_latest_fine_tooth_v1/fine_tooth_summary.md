# GilgameshCaw/Caw Latest Fine-Tooth Review

Generated UTC: `2026-05-28T00:32:05Z`

## Repo Snapshot

- repo: `GilgameshCaw/Caw`
- url: `https://github.com/GilgameshCaw/Caw`
- default branch: `master`
- current head: `e7d55bf5e436eb52baf5e8592e6b1fdf60989305`
- pushedAt: `2026-05-21T08:19:57Z`
- updatedAt: `2026-05-21T08:20:03Z`

## Static Findings

- Solidity files found: `66`
- Static control-surface hits: `6128`

### Control-Surface Hit Counts

```
archive_rebuild 1256
create_selfdestruct 28
layerzero_oapp 738
multisig_or_safe 494
owner_or_ownable 96
pathway 121
pause_or_emergency 7
proxy_or_upgrade 157
validator_queue 3231
```

## Manifesto Review Position

This review does not classify activity as acceptance.

The current status remains:

`NOT_PROVEN_MANIFESTO_COMPLETE`

A build may be serious and still fail the manifesto proof burden.

## Required Closure Proofs

- final deployed addresses
- verified source and bytecode
- owner and admin state for every critical contract
- proxy and upgradeability checks
- multisig checks
- consumed setup proof
- LayerZero endpoint, delegate, peer, trusted remote, and config-finality proof
- validator admission and censorship-resistance proof
- independent node and indexer rebuild
- empty database export hash
- cawmmunity review and acceptance record

## Recent Commits

```
e7d55bf5 (HEAD -> master, origin/master, origin/HEAD) fix(profile-l2): inline one-shot guard on setERC1271Sibling (was 94 bytes over EIP-170)
82e608cd ui(dm-badge): show count of unread CONVERSATIONS in drawer, not messages
9995751d docs(wp): update §6.5-6.6 + threat model for v5 SmartEOA + sponsored minter
3d095164 docs(dm): refresh stale comment on goBackToInbox after direct-state-update fix
dfc36a76 fix(dm): group chat back button — direct state update, not URL-effect-only
f13d84f2 chore(cli): recommend dRPC, anti-recommend Alchemy free tier in RPC prompts
90977526 docs: add Population routing section (FE) to CLAUDE.md
2788dd80 sec(ai-proxy): tight per-route body limit + CDN-fetch timeout
97685195 feat(ai-proxy): BYOK image generation for OpenAI + Grok via backend proxy
56b1ce72 fix(ux): mobile UX fixes and icons polish
b5b999d1 fix(ux): toolbar icon spacing + iPhone bottom-nav padding
e44367a7 test(profile-l2): foundry mainnet-fork gas measurement for setWithdrawable
5b7b0ec7 sec(archive): 10-minute cooldown on checkpointClaimed after slash
92be18ca sec(archive): raise MIN_STAKE 0.01 -> 0.05 ETH
5bced06d sec(profile-l2): OnlyOnce-lock setERC1271Sibling
df8adcfc fix(profile-l2): raise setWithdrawable LZ gas budget to 35_000 + 24_000*n
72281351 fix(profile-l2): MAX_SESSION_SPEND cap on session spendLimit
814d4e4d docs(minter): document why mintAndDepositSponsored permits depositAmount=0
b5d1cfd7 docs(sp1-vendor): add SOURCES.md provenance — closes audit H-19
fc62bc38 docs(7702): align CLAUDE.md + NatSpec with landed v5 reality
12db0d54 test(minter): clarify wallet-permissive vs wallet-agnostic in MinterSponsor docs
300ee440 fix(sponsor): owner-mismatch defense + narrow wallet-agnostic claim
0af05d31 deploy(7702): wire SmartEOA into the deploy manifest
3594b4d6 fix(minter): guard depositForSponsored against zero-amount nonce burn
ce13a5dd test(minter): DOMAIN_SEPARATOR cross-chain isolation regression
c1ebd577 fix(minter): depositForSponsored pull-and-approve CAW from sponsor
83d48766 feat(minter): sponsor entry points for 7702 smart-EOA flows
e3a284ba test(smart-eoa): L-3 tests assert event ABSENCE via vm.recordLogs
24b0e3de feat(profile): authenticateForMinter + organic shrinks for sponsor path
6631ee4a feat(7702): SmartEOA delegate contract — passkey + secp256k1 dual-sig auth
5720d977 ui(feed-tabs): #299 — slide-in animation on tab change
038a12ee fix(bugs): #296 — extend feed scroll-restore budget + scrollY fallback
f4d1b7e0 docs(backup): ecdsaFallback is the ultimate authority — onboarding spec
24f94508 test(7702): foundry gate proving single-tx auth+initialize+ext-call works
22d1efb8 fix(profile): H-1 — depositFor routes auth fee through getAuthFeeAndAddress
c8231a4d ui(dm): raise composer max-height from 96px to 240px (~10 lines)
2096c3db sec(profile): shrink CawProfile under EIP-170 on solc 0.8.30
da162d0d test(marketplace): align with H-15 pull-pattern + add H-17 foundry coverage
7ff0ff49 fix(notifications): roll up thread-reply chunks; strip poll marker from failed-action snippets
88593cdf ui(post-form): group 2 icons pin left (justify-start) instead of centering
17cede2b ui(post-form): split toolbar icons into 3 + 4 groups for clean wrap
ae7d0689 fix(cli): read SHORTURL_DOMAIN, not PUBLIC_URL, for nginx patcher
ee6e3ba8 ui(post-form): wrap icons (not Post button) on narrow contexts
9191adb1 ui(post-form): AI button everywhere; toolbar flex-wraps on narrow contexts
5e86f4a4 ui(tip-icon): apply dim alpha at SVG level to kill stroke overlap hotspots
0807d1ed sec(marketplace): H-15, H-17 — pull pattern for seller ETH + defaulted-auction escape
e46d07b4 ui(post-form): tighten toolbar spacing for reply contexts
4412d2a1 ui(icon): outline-only inactive state for the tip coin
bc52d94f feat(media-modal): ←/→ keys navigate between images
9d40780c sec(contracts): H-2 v2 — narrow LZ silent-drop to underflow case only

```

## Evidence Hashes

- `reports/github_repo_meta.json` sha256 `8acb64916dd654fe7f2ea0d726c77343578dc4039ec0b3ff5178c6e50fa7f363` size `359`
- `reports/recent_commits_50.txt` sha256 `e3d639a35640007160f6e6ce9c76b1d8cd9e5ad1592a9389b3ed79b35594b445` size `3912`
- `reports/static_control_surface_hits.tsv` sha256 `e0181d293c79dadf98a543b18160a2578ad75977dbdcea4aa5bb4e8692e96276` size `920027`
- `reports/docs_claim_scan.txt` sha256 `902c47022bc80b571abcf4d77808f6dbe85659b8a7d7a680628425f65715f629` size `108763`
- `reports/deploy_address_scan.txt` sha256 `4ec0e09b28af6ac0ae64317c47bcfd05119b8aa3e96c469c4dba1bd255e9dcf1` size `540768`
- `reports/solidity_files.txt` sha256 `88084c0096aa5c08cb137c3e8323449a33ed29e05cdfa328f05aabc96f7c9f81` size `3459`
- `evidence_testsite/help_resources.html` sha256 `c72b72c33238ce1422497c278e2e7b92eba7e00792338f2ce7cbe14201ce1d2b` size `6005`
- `evidence_testsite/api/stats.json` sha256 `44fdda043efd4bb72a3c8e3ea514aba4b521b79b29223f4b0e0f05fc26bea9c8` size `139`
- `evidence_testsite/api/health.json` sha256 `a29ee2b15c494311c52521766e44af56a3ad2248e7a8ab465e5206463c13d288` size `15`
