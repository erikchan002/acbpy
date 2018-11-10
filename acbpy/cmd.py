import sys
import os
from . import handler as acb


def main():
    if len(sys.argv) is 1:
        message("ファイルを指定して下さい。\nUsage: acbpy target_file [target dir]")
    elif 2 <= len(sys.argv) <= 3:
        message("展開を開始します。")
        if len(sys.argv) is 3:
            if not os.path.exists(sys.argv[2]):
                message(f"展開対象ディレクトリが存在しませんでした: {sys.argv[2]}")
                return False
            save_dir = sys.argv[2]
            message(f"展開対象ディレクトリ: {save_dir}")
        else:
            save_dir = ""
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], "rb") as r:
                for j in acb.parse_binary(r):
                    with open(os.path.join(save_dir, f"{j.track.name}.{j.extension}"), "wb") as w:
                        w.write(j.binary.read())
                        message(f"cue_id: {j.track.cue_id} / {j.track.name}.{j.extension}")
        else:
            message(f"対象ファイルが存在しませんでした: {sys.argv[1]}")


def message(msg: str):
    print(f"[acbpy] {msg}")
