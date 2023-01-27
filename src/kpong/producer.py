from kafka import KafkaProducer

from kpong import PingPongMessage
from kpong.schema import PING_PONG_SCHEMA
from kpong.serde import serializer

USER_ID = 'user-01'

PRODUCER = KafkaProducer(bootstrap_servers='localhost:9092')


def publish_ping_pong(message: PingPongMessage):
    bs = serializer(message, PING_PONG_SCHEMA)
    PRODUCER.send(topic='pingpong', value=bs)
    PRODUCER.flush()

