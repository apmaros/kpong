import io
import json
from dataclasses import dataclass

import avro
from avro.io import DatumWriter, DatumReader, BinaryDecoder

from kpong import PingPongMessage
from kpong.schema import PING_PONG_SCHEMA


def ping_pong_deserializer(message):
    return deserializer(message, PING_PONG_SCHEMA, PingPongMessage.from_dict)


def deserializer(datum, schema: str, mapper: callable):
    avro_schema = avro.schema.parse(json.dumps(schema))
    reader = DatumReader(avro_schema)
    message_bytes = io.BytesIO(datum)
    decoder = BinaryDecoder(message_bytes)
    msg = reader.read(decoder)

    return mapper(msg)


def serializer(message: dataclass, schema):
    avro_schema = avro.schema.parse(json.dumps(schema))

    writer = DatumWriter(avro_schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(message.__dict__, encoder)
    bs = bytes_writer.getvalue()

    return bs
