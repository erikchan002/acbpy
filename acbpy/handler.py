import io
from . import acb, models


def parse_binary(acb_file: open):
    utf = acb.UTFTable(acb_file)
    cue = acb.TrackList(utf)
    if not cue.tracks:
        return []
    embedded_awb = io.BytesIO(utf.rows[0]["AwbFile"])
    data_source = acb.AFSArchive(embedded_awb)

    return [
        models.Acb(
            track=track,
            binary=io.BytesIO(data_source.file_data_for_cue_id(track.wav_id)),
            extension=acb.wave_type_ftable.get(
                track.enc_type, track.enc_type)[1:]
        )
        for track in cue.tracks
    ]
