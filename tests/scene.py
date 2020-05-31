import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.pyramid import Pyramid
from mcthings.server import Server
from mcthings.world import World

from mcthings_extra.rainbow import Rainbow

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

# In this scene Things from McThings and McThings-Drawing are mixed


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))

        World.server.postToChat("Building a rainbow")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 20

        pyr = Pyramid(pos)
        pyr.build()

        rainbow = Rainbow(pyr.end_position)
        rainbow.build()

        World.scenes[0].save("scene_rainbow.mct")

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
