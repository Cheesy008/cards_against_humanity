from enum import IntEnum, unique


@unique
class WebsocketMessageType(IntEnum):
    USER_JOIN = 1
    USER_LEAVE = 2
    MESSAGE = 3
