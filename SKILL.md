---
name: screenshot-refresh-plan
description: Identify App Store or Google Play screenshots that need updating after an app release. Compare existing store images with current app captures and confirmed changes, then report affected languages, devices, and image positions with evidence. Use for outdated store screenshots, screenshot refresh planning, or “这次改版哪些商店图要重拍”.
---

# Screenshot Refresh Plan

Produce an actionable refresh list for existing store screenshots. Write the report in the user's language and preserve original UI labels when citing evidence. The first run can work with two folders of images. Python 3 is optional for inventory fingerprints. Image viewing is required for visual verdicts.

## Establish the comparison

Find the existing store images, current app captures, and the intended app/build from the request and project. Use supplied release notes or a scoped code diff as additional context. Distinguish the published store set from draft artwork, and current captures from design proposals. If the current build's identity is unknown, state that the result compares the supplied images only.

Inspect inputs already available before asking for missing material. Continue with the images that can be compared. If there are no store images, request their location and the intended current version. If there are no current captures, confirmed user-provided changes can support a content update, but visual checks remain incomplete.

Use an existing manifest when available. Otherwise identify each store image by its relative filename, locale, device class, and position. Match it to a current screen using visible headings, navigation, content, and supplied mappings. Filename clues are provisional until corroborated. Record unknown dimensions as `unknown`, retaining the filename as the identity. Preserve duplicate-looking images in different slots. For a composite showing several screens, check each relevant panel.

For local folders, optionally inventory each side with the bundled helper, resolving its path from this skill folder.

```sh
python3 /path/to/screenshot-refresh-plan/scripts/inventory.py /path/to/store-images
python3 /path/to/screenshot-refresh-plan/scripts/inventory.py /path/to/current-captures
```

The helper reads PNG, JPG, JPEG, and WebP files recursively and prints paths and SHA-256 hashes. It reports skipped symlinks and read failures. Account for these in coverage. A hash proves file identity only. Different hashes do not establish stale content.

## Compare visible facts

Open both images for every pair that receives a visual verdict. Contact sheets can help match screens, but inspect readable full-size images before quoting labels or judging a small detail. Use the host's image-viewing tools. If an image is unreadable or image tools are unavailable, mark that portion unverified.

Check these separately so the update action stays specific.

- The UI inside the device frame, including navigation, meaningful controls, displayed feature names, and available actions.
- The marketing caption, including functionality or availability claims, and its relationship to the current product.
- The locale and device context, including translated labels, truncation, and the supplied screen size.

Treat variable sample names, dates, counts, progress, and status-bar details as content variation unless they change the claim being made. A different account, subscription state, feature flag, onboarding state, or experiment can explain an apparent discrepancy. Resolve that context before asserting the store image is outdated.

Compare matching locale/device/state captures where available. A capture in one language cannot establish that another language's UI copy is correct. A shared layout change may identify other assets to inspect, but each uninspected asset remains unverified. Code changes identify candidate screens, not visual proof or deployment status. Missing code or an absent button alone does not prove a feature was removed.

Use three verdicts.

| Verdict | Required evidence | Typical action |
| --- | --- | --- |
| `update` | A material contradiction visible in a matched current capture, or a visible old claim contradicted by an explicit confirmed product change | Replace the embedded capture, revise a caption, or replace a specific panel |
| `keep` | All meaningful UI panels and claims for this asset have adequate current evidence and no material discrepancy | Reuse for the stated build and checked scope |
| `check` | Missing, ambiguous, unreadable, mismatched, or unconfirmed evidence prevents a verdict | Name the exact missing capture or product fact |

A known contradiction can justify `update` even when other parts remain unverified. Include the remaining uncertainty. For an asset otherwise marked `keep`, any unverified meaningful panel or claim makes the overall verdict `check`.

For each `update`, cite what the store image shows, what the current evidence shows, and where each can be found. Identify the region in plain words such as “bottom navigation, second tab”. Quote text only when legible. Use bounding coordinates only when measured. Distinguish a confirmed release change from a visual observation. Assign priority from user impact, with unavailable features and materially wrong purchase claims ahead of minor copy changes.

## Deliver the plan

Report the app/build, evidence scope, and coverage counts first. The review scope is the union of discovered store files and expected entries in supplied manifests or prior audit mappings. Include each asset exactly once. Counts for `update`, `keep`, and `check` must sum to that scope; list skipped symlinks and unreadable inputs separately and mark expected inaccessible assets `check`. A missing expected entry stays in scope even when the file is absent. Report current screens without store counterparts separately as optional additions.

Use a compact table with asset, locale/device/slot, verdict, evidence, and action. Sort `update` first, then `check`, then `keep`. Link to the exact supplied or local files using paths supported by the host. Show a short example pair inline when it helps the user see the most important issue. End with the smallest concrete list of assets to recapture or captions to revise, and unresolved inputs that could change that list.

Save a report and reusable mappings in the current project when file output is supported and consistent with the request. Read [references/state.md](references/state.md) when persisting a result or reusing prior mappings. Keep app identities separate. An audit records observations and suggested changes. A published or approved baseline changes only when the user identifies a replacement set as published or approved. Store images and their source captures are inputs to this workflow.
