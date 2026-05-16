# Reproducibility Guide

## Goal

A reviewer should be able to reproduce every major claim from public sources and saved artifacts.

## Current Reproducible Checks

### 1. Testsite user count

Source:

`https://test.caw.social/api/stats`

Expected fields observed:

- totalUsers
- totalPosts
- activeUsersThisWeek
- totalCawBurned

### 2. cawNAME candidate verification

Observed likely cawNAME contract:

`0x9fcbb3d6880cd3293f1a731fe6c958a6621a74bf`

Observed on Sepolia:

- name: CAW NAME
- symbol: cawNAME
- totalSupply: 2282
- owner: 0xf71338f3eaa483aa66125598b09ba1988e694a95

### 3. Acceptance ratio

Formula:

`testsite users / CAW holders`

Known values at time of review:

- CAW holders: about 26,949
- testsite totalUsers: 2,281
- activeUsersThisWeek: 958

Ratios:

- 2,281 / 26,949 = about 8.46%
- 958 / 26,949 = about 3.55%

### 4. Historical sync proof status

Current status:

Architecture references found, but full claim remains unproven.

Required proof:

- exact repo commit
- exact contract addresses
- exact chain IDs
- exact start blocks
- exact RPC assumptions
- empty DB rebuild command
- deterministic export hash
- independent rerun matching same hash

### 5. LayerZero proof status

Current status:

Unresolved review item.

Required proof:

- endpoint addresses
- delegate status
- peer configuration
- trusted remote status
- whether peers/config can change
- whether message routing depends on privileged operators
- finality/renounce proof for cross-chain control paths
