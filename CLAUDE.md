# Zork I, II and III (Asciiverse packaging)

Infocom's Zork trilogy for the Asciiverse Text adventures category: the
original story files (MIT since 2025) packaged with Frotz. Catalog ids
`zork1`, `zork2`, `zork3` (kind `adventure`).

- No code of ours: the story files are unchanged. Provenance and checksums
  are in README.md; never replace a story file without updating them.
- Each av archive: `<story>` (the start script, asciiverse/play), `lib/frotz`,
  `<story>.z3`, LICENSE, README.md. Saved games go to
  ~/.local/share/<story>, outside the install folder.
- Frotz is built from upstream's 2.55 tag at a pinned commit
  (asciiverse/build-frotz.sh), the same build as theasciiverse/frotz.
- Release: tag `v1-av.<n>` and push it.
- Previews: `sh asciiverse/stage.sh zorkN` after building Frotz, then
  `python3 asciiverse/record-preview.py zorkN`.
