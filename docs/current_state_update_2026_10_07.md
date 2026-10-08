# CAW public peer review — active engineering handoff, 2026-10-07

This document is the current operational handoff for the active GilgameshCaw/Caw decentralization review.

It supersedes `docs/current_state_update_2026_08_09.md` for the active PR #221 / PR #276 engineering lane. The August document remains a historical snapshot of the reviewed testnet state.

The purpose is continuity: a new reviewer or bot should be able to continue the work without reconstructing the full conversation history.

---

## 0. Read this first

**FACT:** Do not merge, push a combined integration commit, or resume final evidence sealing yet.

**FACT:** Upstream PR #221 is open, unmerged, and mergeable at:

`f0815a8e0ced5beb4cf195798518f21f8344d613`

branch:

`docs/pathwayexpander-trust-boundary`

title:

`fix(decentralization): close PathwayExpander post-deploy authority`

**FACT:** Upstream PR #276 is open, unmerged, and mergeable at:

`d32727842fa242411068fa1ed0d8d8b495a7d0f0`

branch:

`fix/lz-message-library-pinning`

title:

`fix(decentralization): remove LayerZero default-library dependency`

**FACT:** Both currently target base:

`97cd13f3a1423f702d411472fdd2b2a2e7bfbd59`

**FACT:** A combined #221 + #276 integration artifact was reconciled and extensively validated locally.

Exact staged patch:

`c93ec642a94045734d0151c659afb9848d3d3082a6104729068ffc7f1e8a82d3`

Size:

`19368` bytes

Changed paths:

- `solidity/contracts/PathwayExpander.sol`
- `solidity/scripts/lz-dvn-config.js`
- `solidity/scripts/verify-deploy-wiring.js`

**FACT:** That artifact is now historical validation evidence, not merge-ready evidence. A new reviewer question exposed a sealed-generation failure-boundary defect in `deploy.js`, and that defect was reproduced deterministically against the exact current `deployPhase()` implementation.

**FACT:** Xubu-Trad publicly acknowledged that finding on PR #221 and committed to a deterministic fix and regression coverage.

**FACT:** A corrective #221 worktree now exists, but the first deterministic patcher stopped before writing the intended production change because its source anchor was ambiguous.

**NEXT:** verify the corrective worktree stayed clean, preserve the failed patcher lane, then make a V2 patcher that changes only the anchor-selection logic.

---

## 1. Repositories and local paths

### Public peer-review record

Repository:

`Xubu-Trad/caw-public-peer-review`

Default branch:

`main`

This file is the active handoff entrypoint.

### Upstream implementation

Repository:

`GilgameshCaw/Caw`

Active PRs:

- #221 — PathwayExpander post-deploy authority closure
- #276 — explicit LayerZero message-library pinning

### Xubu fork used by the PR heads

Repository:

`Xubu-Trad/CawUsernames`

### Main combined worktree

`~/gilg/IN/PR221_PR276_INTEGRATION_V1`

### Main combined evidence root

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1`

### Active #221 corrective worktree

`~/gilg/IN/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1`

Local corrective branch:

`fix/pr221-sealed-failure-boundary-v1`

### Active #221 corrective output root

`~/gilg/OUT/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1`

---

## 2. PR #221 — current design and history

### Current head

**FACT:** #221 head:

`f0815a8e0ced5beb4cf195798518f21f8344d613`

**FACT:** proof-integrity correction commit:

`701ba35ea8bf019db03013f54ba1e6e41651c8d0`

**FACT:** common base used by #221 and #276:

`97cd13f3a1423f702d411472fdd2b2a2e7bfbd59`

### Contract-level intent

**FACT:** #221 treats PathwayExpander authority as bootstrap-only for sealed generations.

**FACT:** `transferOwnership(address)` is overridden to revert, preventing transfer of bootstrap authority to a replacement human-controlled owner.

**FACT:** `finalizeBootstrap()` is owner-only, transfers ownership to `address(0)`, and emits `BootstrapFinalized(formerOwner)`.

**FACT:** inherited `renounceOwnership()` also closes bootstrap authority.

### Lifecycle correction at f0815a8

Reviewer nyaromesama correctly pointed out that the prior version finalized every testnet deployment even though testnet remains an evolving topology.

**FACT:** f0815a8 changed the lifecycle so:

- mainnet always seals;
- testnet/dev remain unsealed by default;
- non-mainnet may explicitly request sealing with `FINALIZE_BOOTSTRAP=true` or `1`;
- once sealing intent is recorded or any finalization proof exists, recovery remains sealed;
- `FINALIZE_BOOTSTRAP=false/0` cannot downgrade a deployment that already entered the sealed lifecycle.

**FACT:** The permissionless future-expansion problem remains separate.

**FACT:** No developer key was restored.

### Proof-integrity correction at 701ba35

Reviewer ahdmesh found that the earlier verifier proved that `owner()==0` at a recorded block but did not prove that the recorded transaction caused finalization.

**FACT:** 701ba35 bound proof to the action itself by checking:

- finalization receipt target == PathwayExpander;
- finalization transaction target == PathwayExpander;
- calldata exactly encodes `finalizeBootstrap()`;
- exactly one `BootstrapFinalized` event is emitted by that PathwayExpander;
- `formerOwner == tx.from`.

**FACT:** The unrelated-successful-transaction false-proof case is now rejected.

Relevant comments:

- ahdmesh finding: issue comment `5986754799`
- Xubu-Trad response: issue comment `5987884505`

---

## 3. PR #276 — current design and history

### Current head

`d32727842fa242411068fa1ed0d8d8b495a7d0f0`

### Main behavior

**FACT:** #276 removes reliance on a mutable LayerZero endpoint default by explicitly pinning selected send and receive message libraries through PathwayExpander.

**FACT:** The PR adds owner-gated `pinSendLibrary` and `pinReceiveLibrary` paths and integrates pin reconciliation into `solidity/scripts/lz-dvn-config.js`.

**FACT:** The verifier rejects:

- a pathway still relying on the default, even when the default equals the expected library;
- a wrong explicit send library;
- a wrong explicit receive library.

**FACT:** LayerZero configuration and explicit library pinning are consecutive transactions, not atomic.

**FACT:** Once #276 pinning is combined with #221 finalization, the selected library cannot later be changed through the sealed PathwayExpander.

**INFERENCE:** future library replacement therefore requires reviewed redeployment/migration or a future permissionless mechanism.

Relevant comments:

- nyaromesama review: issue comment `6032625377`
- Xubu-Trad response: issue comment `6035053040`

---

## 4. Combined #221 + #276 integration V1

### Parents

#221:

`f0815a8e0ced5beb4cf195798518f21f8344d613`

#276:

`d32727842fa242411068fa1ed0d8d8b495a7d0f0`

### Exact combined artifact

SHA256:

`c93ec642a94045734d0151c659afb9848d3d3082a6104729068ffc7f1e8a82d3`

Size:

`19368`

### Conflict reproduction

**FACT:** textual conflicts reproduced only in:

- `solidity/contracts/PathwayExpander.sol`
- `solidity/scripts/verify-deploy-wiring.js`

**FACT:** `solidity/scripts/lz-dvn-config.js` merged cleanly.

**FACT:** The reconciliation kept #221 as the semantic base for conflicted files, inserted #276 pinning surfaces/events, merged the #276 library verifier into the #221 verifier, and retained the #221 finalization verifier.

### Production identities in the validated combined worktree

`PathwayExpander.sol`

`5531c2b98b2c371310d356840553ea477d44f67b49468e1b5d1ed380a62062cf`

`deploy.js`

`259597fc77a6a8b010c12fda0921636c6b8d5df7e752c69c7785af111eaed670`

`lz-dvn-config.js`

`24a12b021663af40261956c0fa5db86f17f9e1a6ade8cba9b234a16301351903`

`verify-deploy-wiring.js`

`35aba0bb5593238f0282960ee5bff419c708a8b23e3836a03f73860008e5d944`

`package-lock.json`

`2ed4876f494ed4e02703b825fdd84475781fdd974c4374f71cb53d32fd3f1601`

forge-std exact commit:

`7117c90c8cf6c68e5acce4f09a6b24715cea4de6`

---

## 5. Combined validation that passed before the new failure-boundary finding

These results remain useful historical evidence for the exact `c93ec642...` artifact.

They must **not** be represented as final merge-readiness after the newly reproduced `deploy.js` defect.

### Hardhat compile

**FACT:** 127 Solidity files compiled.

Log SHA256:

`2329d4d6031ace18f82a60650f210333e465780a738d51bb34d65cc6eff8eecf`

### #221 bootstrap-finalization Foundry regression

**FACT:** 5 pass / 0 fail.

Log SHA256:

`2742bf9d8f970f3070b340cd081564d62403fecb2f459aa3e1b3b94e8b9b0ff6`

Tests:

- `test_allPrivilegedSurfacesClosedAfterFinalization()`
- `test_finalizationPreservesPeerStateAndOAppOwner()`
- `test_finalizeBootstrapRenouncesOwner()`
- `test_inheritedRenounceOwnershipAlsoClosesBootstrap()`
- `test_transferOwnershipIsPermanentlyDisabled()`

### #221 pathway-escalation Foundry regression

**FACT:** 11 pass / 0 fail.

Log SHA256:

`b9191fc6d4fc54f037fa281a968a5fba99956d8e0423b800eb11489d3c68594d`

Static/Foundry evidence lane:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/FOUNDRY_DEP_REPAIR_V3`

### Cross-PR pin then finalize

**FACT:** `test_pinThenFinalizeClosesLibraryAuthority()` passed 1/0.

Canonical log:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/PIN_FINALIZE_COMPOSITION_V1/pin_finalize_runtime_v1.log`

SHA256:

`13aeb58bbe628ade89c19fd561ef2c3f70c1306fbad371061b254f2d5d8230f9`

**FACT:** The canonical Forge log contains the actual test PASS and the 1 passed / 0 failed suite result.

**FACT:** The higher-level shell marker `PIN_BEFORE_FINALIZE_AND_POST_FINALIZE_REJECTION_PASS` was printed by the wrapper but was never persisted in the canonical Forge log. Later evidence-seal logic incorrectly required that wrapper marker inside the Forge log. That was an evidence-oracle mistake, not a runtime failure.

### #276 pin runtime

**FACT:** 4 pass / 0 fail.

Canonical log SHA256:

`9f4479ca80bcc3d5f7231203bfe8fced85a78219fd87b0acaa232dfaeb5f9729`

Tests:

- `test_conflictingExplicitPinsFailClosed()`
- `test_expectedRepeatedPinsAreIdempotent()`
- `test_receivePinResistsLaterDefaultMutation()`
- `test_sendPinResistsLaterDefaultMutation()`

### #276 production reconciliation callback

**FACT:** Successful combined reconciliation is V3.

Canonical callback harness, reused from V1:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/PR276_RECONCILE_CALLBACK_COMBINED_V1/reconcile_callback_combined_v1.js`

Harness SHA256:

`87edd03d026170d9f33a5d16574090b68c5619a458f0d0ffe8f3956ec12cd68b`

Successful V3 evidence lane:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/PR276_RECONCILE_CALLBACK_COMBINED_V3`

**FACT:** Four callback cases were exercised:

1. fresh — 4 applied, 0 resumed, 0 skipped;
2. resume — 0 applied, 4 resumed, 0 skipped;
3. matching on-chain / no local guard — reapply through expander to establish guarded state;
4. pin receipt failure — simulated receipt failure propagated.

### Combined #221 action-bound verifier

Canonical log SHA256:

`e51f80e163eac1a7fe7f7926f68d8324863cfdad732012a3ce53950279a2dd1a`

**FACT:** genuine proof:

12 passed / 0 failed / 0 warnings

**FACT:** unrelated successful transaction used as fake finalization proof:

7 passed / 4 failed / 0 warnings

Expected action-binding failures:

- receipt target;
- transaction target;
- calldata;
- `BootstrapFinalized` event count.

Markers included:

- `UNRELATED_old_state_only=true`
- `UNRELATED_action_bound=false`
- `EXACT_CURRENT_VERIFIER_UNRELATED_REJECTED`
- `REVIEWER_FALSE_PROOF_REJECTED`
- `PROOF_BINDING_RUNTIME_OK`
- `CURRENT_VERIFIER_PROOF_BINDING_RUNTIME_PASS`

### Combined #276 four-scenario verifier matrix

Matrix summary SHA256:

`66ea885c806005e60f58754c4e34056356350aae3dcf0e509e307022f6985f04`

Results:

- `explicit_good` — RC 0, 111 passed / 0 failed
- `default_same` — RC 1, 110 passed / 1 failed, `LZ SEND CawProfile L1->L2: explicit`
- `wrong_send` — RC 1, 110 passed / 1 failed, `LZ SEND CawProfile L1->L2: library`
- `wrong_receive` — RC 1, 110 passed / 1 failed, `LZ RECV CawProfile L1->L2: library`

### Canonical Phase 7 lifecycle callback

Canonical harness:

`~/gilg/OUT/PR221_SEALED_LIFECYCLE_FIX_V1/PHASE7_EXACT_CALLBACK_RUNTIME_V3/phase7_exact_callback_runtime_v3.cjs`

SHA256:

`0e25674bd73e0e26603950d9039bf6014515786e03f1a6cf954cdd1f3a9374fb`

Combined Phase 7 runtime log SHA256:

`dc3f0705629b49cfd14ba933c95ec2740eb874c97a11247b30bf1754a23c6339`

**FACT:** combined run reproduced the prior V3 log byte-for-byte.

Required lifecycle markers:

- `UNSEALED_TESTNET_FINALIZER_SKIPPED=OK`
- `SEALED_TESTNET_FINALIZATION=OK`
- `INTERRUPTED_SEAL_RECOVERY=OK`
- `SEALED_LIFECYCLE_DOWNGRADE_REJECTED=OK`
- `FINALIZATION_RUNTIME_FAILURE_FATAL=OK`
- `PHASE7_EXACT_PRODUCTION_CALLBACK_RUNTIME_PASS`

### Remote freshness before the new finding

**FACT:** At `2026-10-07T16:21:05Z`, an authenticated GitHub query recorded both PRs open/unmerged at the exact validated heads and common base, and the combined patch remained byte-identical.

**FACT:** A later GitHub query after the new reviewer discussion still showed the same heads and base, with both PRs open, unmerged, and mergeable.

---

## 6. Evidence-seal attempts — preserve them

No final evidence seal was completed before the newly reproduced failure-boundary defect superseded merge-readiness.

### FINAL_EVIDENCE_SEAL_V1

Stopped because the seal assumed a nonexistent directory named:

`STATIC_COMPILE_AND_FOUNDRY_INTEGRATION_DEPFIX_V3`

**FACT:** real static/Foundry evidence was later resolved to:

- `FOUNDRY_DEP_REPAIR_V3`
- `hardhat_compile_v2.log`

### FINAL_EVIDENCE_SEAL_V2

Stopped because it required the reconciliation harness SHA to exist physically inside the V3 reconciliation directory.

**FACT:** the canonical harness resides in V1 and was reused by V3.

### FINAL_EVIDENCE_SEAL_V3

Stopped because it required a shell wrapper marker to appear inside the canonical pin/finalize Forge log.

**FACT:** the canonical log SHA was correct and the actual Forge test passed 1/0.

### FINAL_EVIDENCE_SEAL_V4

A V4 command was designed to use actual runtime semantics instead of wrapper markers, but it was not completed because the reviewer failure-boundary question became the higher-priority correctness issue.

**RULE:** Preserve every failed seal lane. Do not delete or rewrite them.

---

## 7. New reviewer finding — sealed Phase 7 failure boundary

Reviewer:

`ahdmesh`

Issue comment:

`6040616652`

Date:

2026-10-07

The reviewer observed:

- `deployPhase()` only aborts a chain worker when a linking step throws `FatalDeployError`;
- an ordinary `Error` is logged and execution continues;
- some critical Phase 7 read-backs still have ordinary-error paths, including missing `CawProfileLedger_*` / `CawProfile` handles;
- PathwayExpander finalization steps are appended later in Phase 7.

The reviewer asked whether all critical verification should be an explicit prerequisite for sealed finalization.

### Public Xubu response

Issue comment:

`6043618991`

The response states:

- the concern is applicable;
- critical read-backs can still surface ordinary `Error` values, including missing handles and RPC/read failures;
- `deployPhase()` logs those and continues;
- changing only the two explicit missing-handle throws would not fully close the gap because Phase 7 chain workers run in parallel;
- the safer invariant is an explicit generation-wide barrier;
- deterministic reproduction and regression coverage will be added before updating the PR.

---

## 8. Deterministic reproduction of the failure boundary

### V1 harness — failed before execution

Lane:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/SEALED_FAILURE_BOUNDARY_REPRO_V1`

Harness SHA256:

`1e650f398de267ef7a3ff60d0963eecb0e34c8b5c13544cf05e7f5ccd2d203f3`

Size:

`8087`

Failure:

CommonJS `.cjs` harness used top-level `await`.

Classification:

**harness-only failure**

No production bytes changed.

### V2 harness — corrected wrapper only

Lane:

`~/gilg/OUT/PR221_PR276_INTEGRATION_V1/SEALED_FAILURE_BOUNDARY_REPRO_V2`

Harness SHA256:

`e5d4a1e1ef97932b57751ef5ed17ac80aec9c8cc0af1bbdd20fde885d879a9b7`

Size:

`8186`

V1 -> V2 diff SHA256:

`50a6763897402736f2dd4509a2a2960a278f2a1b8534b57438e9c592e5d5182e`

Runtime log SHA256:

`c2cd2d0687026db7b78bb28e2ff36d707869b57646854cd1b2787be25fff5113`

### Reproduced behaviors

**FACT:** The exact current `deployPhase()` runner reproduced:

`ORDINARY_PHASE7_FAILURE_SAME_CHAIN_FINALIZER_RAN=true`

`FATAL_PHASE7_FAILURE_SAME_CHAIN_FINALIZER_RAN=false`

`CROSS_CHAIN_FATAL_OTHER_CHAIN_FINALIZER_RAN=true`

`ORDINARY_PHASE6_FAILURE_PHASE7_FINALIZER_RAN=true`

Terminal marker:

`CURRENT_DEPLOY_SEALED_FAILURE_BOUNDARY_REPRO_PASS`

### What this proves

**FACT:** An ordinary error from a critical Phase 7 step can be logged and skipped while a later same-chain finalizer remains reachable.

**FACT:** A `FatalDeployError` prevents later finalization on that same chain worker.

**FACT:** A fatal on one Phase 7 chain does not create a generation-wide barrier. Another chain worker can reach its finalizer before `Promise.allSettled()` is inspected and the fatal is propagated.

**FACT:** An ordinary required Phase 6 failure can be swallowed and Phase 7 remains eligible to run.

**INFERENCE:** Changing only the two explicit `throw new Error` missing-handle sites to `FatalDeployError` is insufficient.

---

## 9. Intended corrective design

The intended correction is narrower than making every Phase 7 error fatal.

### Required properties

**IDEA:** Add explicit `sealedRequired` classification for operations that must succeed before a sealed generation may finalize.

**IDEA:** Add `sealedFinalizer` classification for PathwayExpander finalizers.

**IDEA:** When sealing is requested, any ordinary exception from a `sealedRequired` step should be converted into `FatalDeployError`.

**IDEA:** A `sealedRequired` step whose condition is false should fail closed rather than silently skip.

**IDEA:** A `sealedRequired` generic contract step whose runtime contract handle is unavailable should fail closed rather than silently skip.

**IDEA:** Run sealed Phase 7 in two generation-wide passes:

1. all non-finalizer wiring and required verification across all chains;
2. PathwayExpander finalizers only after pass 1 completes successfully across every chain.

**IDEA:** Mark mainnet Phase 6 LayerZero configuration/pinning as `sealedRequired` so an ordinary config/pin error cannot be logged and followed by Phase 7 sealing.

**IDEA:** Preserve permissive behavior for non-required unsealed development steps.

**FACT:** Interrupted-seal recovery must continue to pass.

**IMPORTANT:** `PathwayExpander_L1.addPeer` was intentionally not proposed as blindly `sealedRequired` in the first patch design because interrupted recovery may encounter an already-consumed OnlyOnce peer slot. Required read-backs should establish the actual peer invariant before finalization.

---

## 10. Active corrective worktree — exact current state

Worktree:

`~/gilg/IN/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1`

Branch:

`fix/pr221-sealed-failure-boundary-v1`

Starting HEAD:

`f0815a8e0ced5beb4cf195798518f21f8344d613`

Expected original `deploy.js` SHA256:

`259597fc77a6a8b010c12fda0921636c6b8d5df7e752c69c7785af111eaed670`

Expected original `deploy.js` size:

`148213`

Output lane:

`~/gilg/OUT/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1`

Patcher:

`~/gilg/OUT/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1/patch_sealed_failure_boundary_v1.py`

Patcher SHA256:

`584b9c55f00516cc8a29183ba0313ab548108c87473d9e355ee9e64cb9ae07f2`

Patcher size:

`10187`

### Current stop

The first patcher stopped with:

`STOP: per-L2 OApp ownership transfer: expected one nearby phase:7 field, found 2`

**FACT:** This is a patcher source-anchor ambiguity, not a production regression result.

**INFERENCE:** The patcher writes `deploy.js` only at its final `path.write_text(src)` call, so the stop is expected to have occurred before the production file was written. The next reviewer must verify this directly rather than assume it.

---

## 11. First commands for the next bot

Run before changing anything:

```bash
cd "$HOME/gilg/IN/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1" || exit 1
export LC_ALL=C

git rev-parse HEAD
git branch --show-current
git status --short
sha256sum solidity/scripts/deploy.js
git diff -- solidity/scripts/deploy.js
```

Expected:

- HEAD = `f0815a8e0ced5beb4cf195798518f21f8344d613`
- branch = `fix/pr221-sealed-failure-boundary-v1`
- `deploy.js` SHA256 = `259597fc77a6a8b010c12fda0921636c6b8d5df7e752c69c7785af111eaed670`
- no production diff

If any differ, stop and inspect.

---

## 12. Exact next work sequence

### Step 1 — preserve failed V1 corrective lane

Do not delete or overwrite:

`~/gilg/OUT/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V1`

### Step 2 — create a V2 corrective evidence lane

Suggested:

`~/gilg/OUT/PR221_PHASE7_FAILURE_BOUNDARY_FIX_V2`

Use the same corrective worktree only if production bytes verify unchanged.

### Step 3 — change one variable only

Repair only the patcher's ambiguous insertion logic for the per-L2 ownership-transfer anchor.

Do **not** hand-edit `deploy.js`.

Do **not** redesign the barrier at the same time.

### Step 4 — apply corrected deterministic patcher

Expected production path set:

`solidity/scripts/deploy.js`

Only.

### Step 5 — validate the new barrier

Minimum required regression behaviors:

- sealed-required ordinary Phase 7 failure blocks every finalizer on every chain;
- all required pre-finalization work completes across all chains before any finalizer starts;
- ordinary sealed-required Phase 6 failure is fatal;
- non-required unsealed development error remains permissive.

### Step 6 — rerun canonical Phase 7 lifecycle harness

Harness:

`~/gilg/OUT/PR221_SEALED_LIFECYCLE_FIX_V1/PHASE7_EXACT_CALLBACK_RUNTIME_V3/phase7_exact_callback_runtime_v3.cjs`

Expected SHA256:

`0e25674bd73e0e26603950d9039bf6014515786e03f1a6cf954cdd1f3a9374fb`

Required markers:

- `UNSEALED_TESTNET_FINALIZER_SKIPPED=OK`
- `SEALED_TESTNET_FINALIZATION=OK`
- `INTERRUPTED_SEAL_RECOVERY=OK`
- `SEALED_LIFECYCLE_DOWNGRADE_REJECTED=OK`
- `FINALIZATION_RUNTIME_FAILURE_FATAL=OK`
- `PHASE7_EXACT_PRODUCTION_CALLBACK_RUNTIME_PASS`

### Step 7 — review exact diff before commit

Required production path set:

`solidity/scripts/deploy.js`

Only.

### Step 8 — commit #221 correction only after all local corrective tests pass

Do not push an unvalidated patch.

After a clean corrective commit exists, update the actual #221 PR head branch `docs/pathwayexpander-trust-boundary` with a lease-aware workflow.

Do not force-update a moved remote head without rechecking it.

### Step 9 — re-query live #221 and #276 heads

If either moved, invalidate prior assumptions and reconcile against the live heads.

### Step 10 — build fresh combined integration V2

Do not mutate:

`PR221_PR276_INTEGRATION_V1`

Suggested names:

- `IN/PR221_PR276_INTEGRATION_V2`
- `OUT/PR221_PR276_INTEGRATION_V2`

Parents:

- corrected #221 head
- live #276 head

### Step 11 — rerun affected combined gates

At minimum:

- textual conflict reconciliation;
- exact combined patch identity;
- Node syntax;
- Hardhat compile;
- #221 lifecycle regression;
- new sealed-generation barrier regression;
- #276 production reconciliation through `deployPhase` failure semantics;
- cross-PR pin-before-finalize behavior;
- combined verifier interface and action-binding regression;
- #276 four-scenario verifier matrix;
- final Phase 7 callback;
- final live remote-head/base freshness.

Do not inherit the old `c93ec642...` seal.

### Step 12 — only then create a new final evidence seal

Old seal attempts are historical diagnostics.

The corrected artifact needs a new seal lane and a new artifact hash.

---

## 13. Reviewer/comment map

### PR #221

- `5986754799` — ahdmesh proof-integrity finding
- `5987884505` — Xubu-Trad proof-integrity fix response
- `5994300857` — Xubu-Trad architecture note on sealed expansion
- `6032679622` — nyaromesama lifecycle/testnet sealing review
- `6034988614` — Xubu-Trad response; f0815a8 lifecycle correction
- `6040616652` — ahdmesh sealed Phase 7 failure-boundary question
- `6043618991` — Xubu-Trad response confirming applicability and committing to deterministic reproduction

### PR #276

- `6032625377` — nyaromesama combined #221/#276 conflict and permanent-pin tradeoff review
- `6035053040` — Xubu-Trad response acknowledging conflicts and post-seal replacement consequence

---

## 14. Separate unresolved nonce / full E2E lane

**FACT:** Fresh full three-chain end-to-end deployment remains separately blocked before Phase 7 by a nonce-prediction/provider-caching issue.

Lane:

`~/gilg/OUT/NONCE_CACHE_REPRO_V1`

**FACT:** One harness reproduced stale nonce / `NONCE_EXPIRED` behavior under default ethers provider caching.

**FACT:** `cacheTimeout:0` produced 30/30 in that harness.

**FACT:** A paired production-path proof has not yet closed this issue.

**RULE:** Do not use the nonce-cache reproduction as proof that #221 is wrong. It is a separate deployment-path problem.

---

## 15. Architecture boundaries that must remain explicit

**FACT:** #221 solves retained post-deploy PathwayExpander owner authority for a sealed generation.

**FACT:** It does not solve permissionless future topology expansion.

**FACT:** #276 removes dependence on mutable LayerZero default message libraries by explicit pinning.

**FACT:** Explicit config and pin transactions are not atomic.

**FACT:** After pin + sealed finalization, library replacement requires redeployment/migration or a future permissionless mechanism.

**FACT:** No developer/admin key should be restored merely to preserve future expansion.

**FACT:** Full fresh three-chain E2E proof remains separate.

**FACT:** Local validation here is not repository-visible GitHub Actions/status-check proof.

---

## 16. Claims boundary

This engineering record does **not** establish:

- Gilgamesh is the original CAW deployer;
- Gilgamesh has official CAW authority;
- Enkidu and Gilgamesh are the same person;
- fraud;
- deliberate concealment;
- insider enrichment;
- a final mainnet deployment is already broken.

The active finding is narrower:

**FACT:** the current sealed-generation deployment runner does not yet enforce a generation-wide successful-verification barrier before PathwayExpander finalization.

---

## 17. Working rules for continuation

- Evidence first.
- One variable per experiment.
- Preserve failed lanes.
- Never overwrite failed V1/V2/V3 lanes to make history look clean.
- Stop on moved remote heads.
- Stop on checksum mismatch.
- Stop if more than the intended production path changes.
- Treat harness failures as harness failures unless production evidence says otherwise.
- Do not claim merge-readiness from the old `c93ec642...` combined artifact after the new failure-boundary reproduction.
- Do not claim repository-visible CI when only local deterministic evidence exists.
- Do not weaken interrupted-seal recovery while closing the new failure boundary.

---

## 18. Current handoff conclusion

**FACT:** The older combined #221 + #276 artifact reached a high level of local deterministic validation.

**FACT:** A later reviewer question exposed a real deployment-runner boundary not covered by those earlier tests.

**FACT:** That boundary is now deterministically reproduced against the exact current `deployPhase()` implementation.

**FACT:** The current correction attempt stopped in the deterministic patcher before the intended production write because the anchor matcher found two nearby `phase: 7` fields.

**NEXT:** verify the corrective worktree is still byte-identical to f0815a8, preserve the failed patcher lane, repair only the patcher anchor logic in V2, then validate the explicit sealed-generation barrier.

**STOP:** Do not merge the old `c93ec642...` combined artifact as current proof.
