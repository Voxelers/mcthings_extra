import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server

from mcthings_extra.spiral import Spiral

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a spiral")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 1

        spiral = Spiral(pos)
        spiral.block = mcpi.block.WOOD
        spiral.build()

        server.mc.entity.setTilePos(server.mc.getPlayerEntityId(BUILDER_NAME),
                                    spiral.end_position)

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
