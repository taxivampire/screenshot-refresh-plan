# Screenshot Refresh Plan

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Which store screenshots became outdated after your last app update?

A Codex skill for comparing existing App Store or Google Play screenshots with current app captures. Get a refresh list by language, device, and screenshot position, with the evidence behind each decision.

Useful when a release changes navigation, screen layouts, feature names, or store claims—especially across multiple languages and device sizes.

## Example outcome

Illustrative output for an app with a renamed tab and a changed feature.

| Asset | Verdict | Evidence | Action |
| --- | --- | --- | --- |
| English · iPhone · 03 | Update | Store image shows “History”, current capture shows “Activity” | Replace the embedded capture |
| Japanese · iPhone · 02 | Update | Caption promises a feature confirmed removed from this release | Rewrite the caption |
| German · iPhone · 01 | Check | Current German capture is missing | Capture the matching screen |
| English · iPad · 01 | Keep | UI and claims match the supplied current evidence | Reuse |

## Install

Clone the skill into your Codex skills directory:

```sh
git clone https://github.com/taxivampire/screenshot-refresh-plan.git \
  ~/.codex/skills/screenshot-refresh-plan
```

If that directory already exists, update or inspect your existing installation first. You can also download the repository and copy its contents into that directory.

Open a new Codex chat in your app project. The host needs image-viewing tools. Python 3 enables the optional local inventory helper, which uses the standard library.

## Use it

```text
$screenshot-refresh-plan
Compare store/ with current/ for Harbor 2.3 (42).
Tell me which store images need updating and show the evidence.
```

Chinese requests work too.

```text
$screenshot-refresh-plan
store/ 是现有商店图，current/ 是 2.3 版本的截图。
看看哪些语言、设备和第几张图需要更新，说明具体哪里变了。
```

For the first run, provide the existing store artwork and current captures of the same screens. Release notes and confirmed feature changes can add context. An existing screenshot manifest can provide locale, device, and slot mappings.

A small input layout is enough:

```text
your-app/
  store/en-US/iphone/01.png
  store/en-US/iphone/02.png
  current/en-US/iphone/home.png
  current/en-US/iphone/activity.png
```

You supply the current screenshots and identify the build they came from. A public website or a design proposal without build information supports a preliminary comparison; affected images remain `check` until the evidence is sufficient.

## What you get

- A per-image plan with `update`, `keep`, or `check` verdicts.
- File references and specific visible differences supporting each update.
- Separate actions for recapturing UI, changing captions, and resolving missing evidence.
- Dated reports and reusable mappings under `.screenshot-refresh/<app-id>/` in the app project when file output is available.

An image hash tracks file identity. Visual judgments come from inspecting the actual images. Unconfirmed builds, missing captures, ambiguous screen matches, and unsupported claims remain visible in the report. An audit's recorded observations do not establish a published or approved baseline.

The first version reviews supplied images and confirmed changes. It depends on the host model's visual reading, so small or ambiguous text can require a clearer capture. Current captures for each locale and device improve coverage.

## Local inventory helper

```sh
python3 ~/.codex/skills/screenshot-refresh-plan/scripts/inventory.py ./store
```

This lists image paths, byte sizes, and SHA-256 hashes. It reads local files and makes no network requests. Visual comparison is performed by the host agent using its configured image tools and data settings. Audit reports and mappings stay in your app project.

## 中文说明

用于 App 改版后的商店截图维护：提供旧商店图与当前版本截图，得到按语言、设备、图片位置列出的更新清单。每张图标记为 `update`（需要更新）、`keep`（可复用）或 `check`（证据待补），并写明具体原因与下一步。

适合维护多语言、多尺寸截图的开发者和设计团队。当前版本需要你提供新版截图；缺少当前版本证据时，会保留不确定性。示例是虚构演示，仓库不包含真实 App 的审查资料。

## Feedback

[Open an issue](https://github.com/taxivampire/screenshot-refresh-plan/issues) with the expected result and a small, shareable example. Remove private account information from any screenshots you choose to share.

## License

[MIT](LICENSE) © 2026 taxivampire.
