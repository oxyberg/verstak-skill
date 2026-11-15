# Behavioral and cost comparison

Maintainer-only protocol; do not load during ordinary skill execution. No speedup or fidelity result is established until these runs are recorded.

Compare the baseline skill from the parent revision with the candidate in separate clean copies of the same UI repository. Freeze the Figma nodes/revision or replay the same recorded source payloads and assets. Hold model, reasoning setting, tool availability, project dependencies, initial implementation, and capture environment constant. Use fresh sessions; alternate baseline/candidate order and run each case at least three times. Record cold-cache runs separately from follow-ups with existing context. Replay tests do not measure live provider latency.

| Case | Request / starting point | Required outcome |
| --- | --- | --- |
| Local correction | Existing screen; correct one spacing value from a specified node | Correct spacing and unaffected neighbors; focused visual proof |
| Component | Implement a supplied component with disabled/focus states | Original assets, exact type/layout, working keyboard and state behavior |
| Screen | Implement supplied desktop/mobile frames in existing stack | Full composition, supplied sizes and nearby-width behavior, no unintended overflow |
| Large source | Same screen; source payload is truncated | Selective reads recover necessary evidence; no repeated identical oversized request |
| Follow-up | After screen completion, change one supplied variant | Reuse unchanged evidence, refresh affected source, verify integration |
| Blocked source | Target read fails; other project work is available | No repeated unchanged retries or fabricated source values; precise limitation |
| Persistent mismatch | Wrong font causes wrapping differences | Resolve font cause rather than repeatedly tweaking unrelated spacing |

Save the exact request, source IDs/revision, repository commit, skill revision, environment, transcript, final diff, screenshots, and check results per run. Keep artifacts outside the skill package. Use provider-reported token usage; mark unavailable measurements as unavailable, never estimate from word counts.

Record elapsed time to verified result, input/cached-input/output tokens separately, tool calls by type, Figma response sizes when available, repeated reads, comparison/fix cycles, and test results. Calculate cost only with the recorded provider rates and cache treatment. Report median and range per case, not just an aggregate; separate authentication/install/user-wait time.

Have the reviewer compare results without seeing which skill produced them. Evaluate geometry, text wrapping/type, assets, colors/effects, states, responsiveness, and accessibility behavior. Pixel diff is supporting evidence, not a pass threshold. Candidate must complete the same requested scope, pass required checks, and leave no new concrete fidelity or behavior defect relative to the source. Regressions block acceptance regardless of savings. If both versions fail a requirement, record that failure rather than calling parity a quality pass.

Report measured savings only for passing comparable runs; include failures and variance. Do not claim universal improvement from these fixtures. Add real slow-task traces when available to identify the next bottleneck.
