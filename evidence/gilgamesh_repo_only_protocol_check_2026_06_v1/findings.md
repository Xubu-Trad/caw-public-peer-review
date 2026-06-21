# Gilgamesh Repo-Only Protocol Check V1

## Scope

Only GilgameshCaw/Caw repo-derived code and config were used.

Third-party operator claims were excluded.

## Repo state

HEAD: e2074718bcea293726ddfcf8764e1499e7b9217c

## Canonical deployment source

Deployment rows were parsed from:

- client/src/abi/deployments.ts
- client/src/abi/addresses.ts.example
- solidity/.deploy-state.json

## Runtime owner findings

The following repo-canonical testnet OApps returned nonzero owner:

- sepolia CawProfile 0x9fcbb3d6880cD3293F1a731Fe6c958a6621a74bF
- sepolia CawProfileL2 0xa99936edD087cE11824232ebD83B036C90163688
- base_sepolia CawProfileL2 0x0c3e245f3939B4D9f30e088988dD9D7C8F86b11d
- base_sepolia CawActionsArchive 0x3b2A9ac4f274eE6E73CbAD198F80f455e70C3C05

Owner for all four:

0xF71338f3eAa483aA66125598B09BA1988e694a95

## Runtime delegate findings

LayerZero endpoint for all four checked OApps:

0x6EDCE65403992e310A62460808c4b910D972f10f

Delegate at endpoint for all four checked OApps:

0xF71338f3eAa483aA66125598B09BA1988e694a95

## setPeer findings

OnlyOnce runtime lock reproduced for configured peer slots:

- sepolia CawProfile eid 40245
- sepolia CawProfile eid 40231
- base_sepolia CawActionsArchive eid 40231

Staticcall succeeded for unset peer slots:

- sepolia CawProfileL2 eid 40245
- sepolia CawProfileL2 eid 40231
- base_sepolia CawProfileL2 eid 40245
- base_sepolia CawProfileL2 eid 40231
- base_sepolia CawActionsArchive eid 40245

## Conclusion

Source hardening exists for once-per-EID setPeer.

Runtime proof shows configured peer slots are locked.

Runtime proof also shows current testnet OApp ownership and LayerZero delegate authority remain with:

0xF71338f3eAa483aA66125598B09BA1988e694a95

Therefore this repo-only lane supports progress, not completion.

It does not prove deployed decentralization, ownership renounce, neutralized delegate authority, or independent reconstruction.
