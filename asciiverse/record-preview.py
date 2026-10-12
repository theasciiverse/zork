#!/usr/bin/env python3
"""Records asciiverse/<story>.cast, a story's catalog preview, at 100x30
(hub/RECORDING.md): the opening, then a few moves typed at a human pace,
through the same start script av runs (stage/<story>, see stage.sh), with a
throwaway HOME. Usage: python3 asciiverse/record-preview.py zork1"""
import os, pty, shutil, struct, fcntl, select, sys, tempfile, termios, time

MOVES = {
    "zork1": ["open mailbox", "read leaflet", "south", "east", "open window", "enter house", "take lamp"],
    "zork2": ["look", "take sword", "take lamp", "turn on lamp", "south", "look"],
    "zork3": ["look", "inventory", "turn on lamp", "south", "look"],
}
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
story = sys.argv[1]
home = tempfile.mkdtemp()
env = dict(os.environ, HOME=home, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", f"{root}/stage/{story}/{story}",
        f"{root}/asciiverse/{story}.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))

def pump(t):
    end = time.time() + t
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.03)
        if r:
            try: os.read(fd, 65536)
            except OSError: return

pump(2.5)
for move in MOVES[story]:
    for c in move:
        os.write(fd, c.encode()); pump(0.09)
    os.write(fd, b"\r"); pump(2.2)
for c in "quit":
    os.write(fd, c.encode()); pump(0.09)
os.write(fd, b"\r"); pump(1.0)
os.write(fd, b"y\r"); pump(1.0)
os.write(fd, b" "); pump(0.5)              # Frotz: "[Hit any key to exit.]"
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]: break
    time.sleep(0.2)
shutil.rmtree(home, ignore_errors=True)
