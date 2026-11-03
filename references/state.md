# Local review state

Use `.screenshot-refresh/<app-id>/` in the current project. Derive an app identifier from the request or an existing bundle/package identifier. For an isolated folder with no app identity, use `default` and state that assumption. Ask for the target when several apps would otherwise share state. Honor a user-specified output directory.

Keep image files in their original locations. Store relative paths against explicit roots and observed SHA-256 hashes. Reuse a mapping only after checking that the assets still exist and that their identities and fingerprints still match. Reinspect replacements and changed associations. Even unchanged store files need a fresh comparison when the target build changes.

Write a uniquely named report such as `audit-20261102T153045Z.md` and its matching `.json`. Use the JSON shape below. This is an observation record. Store approval and publication status come from explicit user evidence. Preserve any supplied approved baseline or store manifest as a separate input.

```json
{
  "schema_version": 1,
  "app_id": "com.example.harbor",
  "target_build": "2.3 (42)",
  "build_source": "User identified current/ as captures from build 42",
  "store_root": "../../store",
  "current_root": "../../current",
  "assets": [
    {
      "id": "en-US/iphone/03",
      "locale": "en-US",
      "device": "iphone",
      "slot": "03",
      "store_file": "en-US/iphone/03-home.png",
      "store_sha256": "<observed hash>",
      "screen_id": "home",
      "current_files": [
        {
          "path": "en-US/iphone/home.png",
          "sha256": "<observed hash>"
        }
      ],
      "verdict": "update",
      "evidence": [
        "Store image bottom navigation labels the second tab History",
        "Current matched screen labels the same tab Activity"
      ],
      "action": "Replace the embedded home capture",
      "uncertainty": []
    }
  ],
  "excluded_inputs": [],
  "unmatched_current_files": []
}
```

Resolve roots relative to the JSON file's containing directory. Use `null` for unavailable hashes, `target_build`, or `screen_id`. Use `unknown` for unresolved locale/device/slot values. Use the original relative filename as `id` when the locale/device/slot combination cannot be established or is duplicated. Preserve all asset identities, including missing expected store files. Record other relevant sources, such as a confirmed release note, alongside evidence with a path or direct URL.

A first audit can establish mappings from existing store artwork to current screens. Subsequent audits can load the most recent compatible JSON. Recheck hashes and mappings, reuse the associations, and write a new dated audit. Historical verdicts remain tied to their original target build.

Keep these local reports and image paths out of a public skill package. When preparing a release of the skill itself, include only its reusable instructions and helpers.
