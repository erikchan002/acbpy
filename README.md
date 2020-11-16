## acbpy

acbpy is simple acb extraction library working on Python3.  
It contains functions and simple command line tool for parse acb format file.  
This library is wrapper library of [acb.py](https://github.com/summertriangle-dev/acb.py).  

## install

```bash
pip3 install git+https://github.com/erikchan002/acbpy.git
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
