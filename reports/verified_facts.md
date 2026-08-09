# Verified Facts Snapshot

## CAW Contract

Mainnet CAW token:

`0xf3b9569f82b18aef890de263b84189bd33ebe452`

## May 2026 historical holder snapshot

The earlier review used a working local holder-count source of approximately:

`26,949` to `26,950` holders

This is a historical review snapshot, not asserted as the current August 2026 count.

## May 2026 Gilgamesh testsite usage snapshot

Public testsite API evidence at that time showed:

- `totalUsers`: 2,281
- `activeUsersThisWeek`: 958
- `totalPosts`: 16,199
- `totalCawBurned`: 58,977,956,000,000

Likely cawNAME candidate observed at that time:

- chain: Sepolia
- address: `0x9fcbb3d6880cd3293f1a731fe6c958a6621a74bf`
- name: `CAW NAME`
- symbol: `cawNAME`
- totalSupply: 2,282
- owner: `0xf71338f3eaa483aa66125598b09ba1988e694a95`

## Historical acceptance-ratio calculation

Using the May snapshot values:

- total testsite users: 2,281 / 26,949 = about 8.46%
- active users that week: 958 / 26,949 = about 3.55%
- cawNAME supply: 2,282 / 26,949 = about 8.47%

Interpretation:

This showed testsite usage at the time. It did not establish broad cawmmunity acceptance.

## August 2026 V2 testnet facts

Review pin:

`GilgameshCaw/Caw@d7a0e05445f13f268b8e0c60a3d4854cb4b206de`

Current reviewed facts include:

- upstream `.deploy-state.json` records `0xF71338f3eAa483aA66125598B09BA1988e694a95` as `deployerAddress`;
- all three reviewed PathwayExpanders remain owned authority surfaces;
- the upstream README describes the protocol as "trustless and decentralized";
- the preserved first-party `verify-deploy-wiring.js` run returned `35 passed, 8 failed`, exit code `1`;
- both current cross-chain Ledgers store superseded Profile `0x4F853523102577dDaf5fdbc823EDdCB13b35C543` as their L1 peer rather than current Profile `0x61C07717210988df782E779cAc8AC67633Ed2a2e`;
- all three current Ledgers have `cawActions` values different from the declared current CawActions deployments;
- the wrong `cawActions` values match wrong-contract collisions in upstream `predictedAddresses` state;
- current `predictedAddresses.CawProfile` points to `CawProfileLens`, not current CawProfile;
- current PathwayExpander source exposes owner-only peer addition, KYC-verifier addition, new-pathway configuration, and bounded DVN escalation; it is constrained but not ownerless;
- the reviewed deployment is testnet and does not by itself establish final-mainnet failure.

## Deployer receipt trail

The CAW deployer-side trail links the CAW contract, manifesto Pastebin, and `github.com/cawdevelopment`.

This remains part of the authority review because a website/front-end surface does not erase an on-chain deployer receipt.

## Boundaries

These facts do not establish fraudulent intent, Enkidu/Gilgamesh common identity, insider enrichment, or official CAW succession without separate proof.
