from channels.staticfiles import StaticFilesConsumer
from channels.routing import route
from . import consumers


channel_routing = [
    route("http.request", StaticFilesConsumer()),
    route("websocket.connect", consumers.ws_connect, path=r"^/game/[0-9a-fA-F-]+/$"),
    route("websocket.receive", consumers.ws_receive, path=r"^/game/[0-9a-fA-F-]+/$"),
    route("websocket.disconnect", consumers.ws_disconnect, path=r"^/game/[0-9a-fA-F-]+/$"),
]