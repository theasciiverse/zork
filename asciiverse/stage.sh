#!/bin/sh
# Lays out one story's av archive in stage/<story>: the start script named
# after the story at the top, Frotz in lib/, the story file, and both
# licenses (the story's MIT, Frotz's GPL).
#   sh asciiverse/stage.sh zork1   (after asciiverse/build-frotz.sh)
set -eu
story=$1
out=stage/$story
rm -rf "$out" && mkdir -p "$out/lib"
cp asciiverse/play "$out/$story"
chmod 755 "$out/$story"
cp build/frotz "$out/lib/frotz"
cp "$story/$story.z3" "$out/"
cp "$story/LICENSE" "$out/LICENSE"
cp build/COPYING "$out/lib/COPYING.frotz"
cp "$story/README.md" "$out/README.md"
