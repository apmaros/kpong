from dataclasses import dataclass
from enum import Enum


class PingPongAction(str, Enum):
    PING = 'ping'
    PONG = 'pong'


class PingPongStatus(str, Enum):
    PLAY = 'play'
    LOST = 'lost'
    WON = 'won'
    ERROR = 'error'


@dataclass
class PingPongMessage:
    ts: int
    userid: str
    status: PingPongStatus
    action: PingPongAction

    @classmethod
    def from_dict(cls, d):
        return PingPongMessage(
            ts=d['ts'],
            userid=d['userid'],
            status=PingPongStatus(d['status']),
            action=PingPongAction(d['action']),
        )

