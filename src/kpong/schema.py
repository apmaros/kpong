
PING_PONG_SCHEMA = {
    "type": "record",
    "namespace": "com.play",
    "name": "pingpong",
    "doc": "Schema describing ping pong game",
    "fields": [
        {
            "name": "ts",
            "type": "long"
        },
        {
            "name": "userid",
            "type": "string"
        },
        {
            "name": "action",
            "type": "string"
        },
        {
            "name": "status",
            "type": "string"
        }
    ]
}