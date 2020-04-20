import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.pyramid import Pyramid
from mcthings.server import Server

from mcthings_extra.rainbow import Rainbow

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

# In this scene Things from McThings and McThings-Drawing are mixed


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a rainbow")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 20

        pyr = Pyramid(pos)
        pyr.build()

        rainbow = Rainbow(pyr.end_position)
        rainbow.build()

        Scene.save("scene_rainbow.mct")

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
