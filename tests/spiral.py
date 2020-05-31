import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server
from mcthings.world import World

from mcthings_extra.spiral import Spiral

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))

        World.server.postToChat("Building a spiral")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 1

        spiral = Spiral(pos)
        spiral.block = mcpi.block.WOOD
        spiral.build()

        World.server.entity.setTilePos(World.server.getPlayerEntityId(BUILDER_NAME),
                                       spiral.end_position)

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
