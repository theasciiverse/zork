> **Play it with Asciiverse.** With [av](https://asciiverse.sh), the Asciiverse
> client:
>
> Each game installs on its own:
>
> | Game | With av | From a release archive |
> |---|---|---|
> | Zork I: The Great Underground Empire | `av install zork1` | `./zork1` |
> | Zork II: The Wizard of Frobozz | `av install zork2` | `./zork2` |
> | Zork III: The Dungeon Master | `av install zork3` | `./zork3` |
>
> Start one with `av play <name>`, or download its archive for your system from
> this repository's Releases and run it from there.
>
> The original README follows.

# Zork I, II and III for Asciiverse

Infocom's Zork trilogy, packaged to play in a terminal: each story file
with [Frotz](https://gitlab.com/DavidGriffith/frotz) 2.55, the Z-machine
interpreter, built for Linux and macOS.

- **Zork I: The Great Underground Empire** (1980)
- **Zork II: The Wizard of Frobozz** (1981)
- **Zork III: The Dungeon Master** (1982)

All three by Marc Blank, Dave Lebling, Bruce Daniels and Tim Anderson,
published by Infocom (as each story's README credits them).

## Where the files come from

The story files are Infocom's own compiled releases, unchanged, from the
`COMPILED/` folders of the historicalsource repositories:

| Story | Source | Commit | sha256 |
|---|---|---|---|
| zork1.z3 | github.com/historicalsource/zork1 | 97b7b3d6 | 37084966477dff679282de42974b2077156b1bd68fad92a65d4ea94d8eb64d79 |
| zork2.z3 | github.com/historicalsource/zork2 | 3da96610 | 3ae7d5558943e9721f3e4b273c8a7faec1a03a604e1ae4ee1cde472c21cb24ac |
| zork3.z3 | github.com/historicalsource/zork3 | 3ec9ed41 | b637a242865d059890184164ce8dec28554cc80901dcbf26c740b2d1ed0d4eb8 |

Each story's folder keeps that repository's README.md and LICENSE.

## License

Microsoft, with Xbox and Activision, released Zork I, II and III under the
MIT license on 2025-11-20 (`LICENSE`, "Copyright (c) 2025 Microsoft").
Frotz is GPL-2.0-or-later; its license travels with it in each archive
(`lib/COPYING.frotz`).

Zork is a trademark. Following the note that came with the release, this
packaging does not imply any sponsorship by Microsoft, Xbox or Activision.
