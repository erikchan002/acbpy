## acbpy

acbpyはPython3で動作する簡易的なacb展開ライブラリです。<br>
acb形式のファイルをパースするための関数や簡単なコマンドラインツールを内包しています。<br>
このライブラリは[acb.py](https://github.com/summertriangle-dev/acb.py)のラッパーライブラリです。

## install

```bash
pip3 install git+ssh://git@github.com/Cryptomelone/acbpy.git
```

## usage

### command line

``` bash
acbpy target_file [extract dir]
```

### import

```python
import acbpy

with open("target_file.acb", "rb") as f:
    for i in acbpy.parse_binary(f):
        print(i.track.name)
        with open(f"{i.track.name}.{i.extension}", "wb") as s:
            s.write(i.binary.read())
```

## models

- track_t [(from acb.py)](https://github.com/summertriangle-dev/acb.py/blob/master/acb.py#L300)
    - cue_id: int
    - name: str
    - wav_id: int
    - enc_type: int
    - is_stream: int

- Acb (original)
    - track: track_t
    - binary: io.BytesIO
    - extension: str
    
## test

```bash
python3 setup.py test
```

## license
follows: [acb.py](/acbpy/acb.py#L2-L45)