import time

from kpong.model.ping_pong_message import PingPongMessage, PingPongAction, PingPongStatus
from kpong.producer import USER_ID, publish_ping_pong


if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        msg = PingPongMessage(
            ts=int(time.time()),
            userid=USER_ID,
            action=PingPongAction.PONG,
            status=PingPongStatus.PLAY
        )

        publish_ping_pong(msg)
    end = time.time()

    print(f"Send messages in {end - start} second")
