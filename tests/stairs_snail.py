import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server

from mcthings_extra.stairs_snail import StairsSnail

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building stairs")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 1

        stairs = StairsSnail(pos)
        stairs.sections = 4
        stairs.steps = 2
        stairs.width = 3
        stairs.block = mcpi.block.IRON_BLOCK
        stairs.build()

        server.mc.entity.setTilePos(server.mc.getPlayerEntityId(BUILDER_NAME),
                                    stairs.end_position)

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
