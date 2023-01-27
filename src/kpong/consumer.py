from kafka import KafkaConsumer

from kpong.serde import ping_pong_deserializer

consumer = KafkaConsumer(
    "pingpong",
    group_id="kpong-1",
    client_id="kpong",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=ping_pong_deserializer
)


def consume_ping_pong():
    print("reading...")
    for msg in consumer:
        print(msg.value)


if __name__ == '__main__':
    consume_ping_pong()
