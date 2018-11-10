import sys
import os
from . import handler as acb


def main():
    if len(sys.argv) is 1:
        message("Please specify file.\nUsage: acbpy target_file [target dir]")
    elif 2 <= len(sys.argv) <= 3:
        message("Starting extract.")
        if len(sys.argv) is 3:
            if not os.path.exists(sys.argv[2]):
                message(f"Target directory did not exist: {sys.argv[2]}")
                return False
            save_dir = sys.argv[2]
            message(f"Target directory: {save_dir}")
        else:
            save_dir = ""
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "rb") as r:
                for j in acb.parse_binary(r):
                    with open(os.path.join(save_dir, f"{j.track.name}.{j.extension}"), "wb") as w:
                        w.write(j.binary.read())
                        message(f"cue_id: {j.track.cue_id} / {j.track.name}.{j.extension}")
        else:
            message(f"Target file did not exist: {sys.argv[1]}")


def message(msg: str):
    print(f"[acbpy] {msg}")
