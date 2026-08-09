# Reproduce the August 2026 Gilgamesh V2 live wiring checks

These checks are read-only. They do not send transactions and do not modify chain state.

## Requirements

- Foundry `cast`
- network access
- public RPCs listed below

## Pinned addresses

```text
UPSTREAM_REF=d7a0e05445f13f268b8e0c60a3d4854cb4b206de
DEPLOYER_OPERATOR=0xF71338f3eAa483aA66125598B09BA1988e694a95

PATHWAY_EXPANDER_L1=0x6c10c9cE2ed0652b046C6C6579E29342723d4d7F
PATHWAY_EXPANDER_L2=0xb8e061DB410464e317b9D594Df7697B01A62Af25
PATHWAY_EXPANDER_L2B=0xce971284f1f1DC3a0FF650432Fd03A936e7201ce

CURRENT_PROFILE=0x61C07717210988df782E779cAc8AC67633Ed2a2e
OLD_PROFILE=0x4F853523102577dDaf5fdbc823EDdCB13b35C543

LEDGER_L1=0xdbBE199f301AF59f471A586975e2Bc64b57F917f
LEDGER_L2=0xee2B2E2dE111942b8a1980836894aB1FDa765f24
LEDGER_L2B=0x7E10b26635fC907774798fd30cB76AD1777A502A

CAW_ACTIONS_L1=0x5158eD62E9cB57F2Ddd38B2D841589E4033CCcCc
CAW_ACTIONS_L2=0x106e1895c1aa7D6B044c50d7c7F04a46Ea4CABb7
CAW_ACTIONS_L2B=0x9e1F62917D9f5D6dc83917565c4e8cbC2BDf6AF2
```

## RPCs

```text
SEPOLIA=https://ethereum-sepolia-rpc.publicnode.com
BASE_SEPOLIA=https://sepolia.base.org
ARB_SEPOLIA=https://sepolia-rollup.arbitrum.io/rpc
```

## 1. Check PathwayExpander ownership

```bash
cast call 0x6c10c9cE2ed0652b046C6C6579E29342723d4d7F \
  'owner()(address)' \
  --rpc-url https://ethereum-sepolia-rpc.publicnode.com

cast call 0xb8e061DB410464e317b9D594Df7697B01A62Af25 \
  'owner()(address)' \
  --rpc-url https://sepolia.base.org

cast call 0xce971284f1f1DC3a0FF650432Fd03A936e7201ce \
  'owner()(address)' \
  --rpc-url https://sepolia-rollup.arbitrum.io/rpc
```

Expected reviewed result: each resolves to the deployer/operator address recorded by upstream deploy state:

`0xF71338f3eAa483aA66125598B09BA1988e694a95`

## 2. Check Base Ledger L1 peer

```bash
cast call 0xee2B2E2dE111942b8a1980836894aB1FDa765f24 \
  'peers(uint32)(bytes32)' 40161 \
  --rpc-url https://sepolia.base.org
```

Expected reviewed result: bytes32 padded old Profile:

`0x0000000000000000000000004f853523102577ddaf5fdbc823eddcb13b35c543`

Current declared Profile should instead end with:

`61c07717210988df782e779cac8ac67633ed2a2e`

## 3. Check Arbitrum Ledger L1 peer

```bash
cast call 0x7E10b26635fC907774798fd30cB76AD1777A502A \
  'peers(uint32)(bytes32)' 40161 \
  --rpc-url https://sepolia-rollup.arbitrum.io/rpc
```

Expected reviewed result: same bytes32 padded old Profile.

## 4. Check Ledger `cawActions` trust slots

### L1

```bash
cast call 0xdbBE199f301AF59f471A586975e2Bc64b57F917f \
  'cawActions()(address)' \
  --rpc-url https://ethereum-sepolia-rpc.publicnode.com
```

Reviewed actual:

`0xDA1F1c34Ed283C7aF358Fbb2d2A3A1A27C5Ac1D7`

Declared current `CawActions_L1`:

`0x5158eD62E9cB57F2Ddd38B2D841589E4033CCcCc`

### Base

```bash
cast call 0xee2B2E2dE111942b8a1980836894aB1FDa765f24 \
  'cawActions()(address)' \
  --rpc-url https://sepolia.base.org
```

Reviewed actual:

`0x9A3bE72fEe5f5f7b259FB2889e2F65CDf7380D57`

Declared current `CawActions_L2`:

`0x106e1895c1aa7D6B044c50d7c7F04a46Ea4CABb7`

### Arbitrum

```bash
cast call 0x7E10b26635fC907774798fd30cB76AD1777A502A \
  'cawActions()(address)' \
  --rpc-url https://sepolia-rollup.arbitrum.io/rpc
```

Reviewed actual:

`0xEb0fD584bd1E5793e7fe9eDA33FCA4BEFd65937f`

Declared current `CawActions_L2b`:

`0x9e1F62917D9f5D6dc83917565c4e8cbC2BDf6AF2`

## 5. Check Ledger owner renouncement

```bash
cast call 0xdbBE199f301AF59f471A586975e2Bc64b57F917f \
  'owner()(address)' \
  --rpc-url https://ethereum-sepolia-rpc.publicnode.com

cast call 0xee2B2E2dE111942b8a1980836894aB1FDa765f24 \
  'owner()(address)' \
  --rpc-url https://sepolia.base.org

cast call 0x7E10b26635fC907774798fd30cB76AD1777A502A \
  'owner()(address)' \
  --rpc-url https://sepolia-rollup.arbitrum.io/rpc
```

Reviewed expected result: zero address on all three Ledgers.

This matters because it confirms that wrong constructor-time trust values are not ordinary owner-mutable configuration.

## Machine-readable interpretation

```text
TYPE=PUBLIC_RPC_REPRODUCTION
CLAIM_CLASS=FACT
WRITE_TX=NO
CHAIN_STATE=READ_ONLY
UPSTREAM_REF=d7a0e05445f13f268b8e0c60a3d4854cb4b206de
EXPECTED_CURRENT_PROFILE=0x61C07717210988df782E779cAc8AC67633Ed2a2e
OBSERVED_L2_PEER_PROFILE=0x4F853523102577dDaf5fdbc823EDdCB13b35C543
VERDICT_L2_PEER_MATCH=false
```

## Limits

These commands prove only the returned live values at query time. They do not by themselves prove motive, fraud, official CAW authority, or the full historical root cause. Those conclusions must be established separately from source history and provenance artifacts.
