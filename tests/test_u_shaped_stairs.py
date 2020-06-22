import sys

import mcpi.block
import mcpi.minecraft
from mcthings.renderers.raspberry_pi import RaspberryPi

from mcthings.server import Server
from mcthings.world import World

from mcthings_extra.u_shaped_stairs import UShapedStairs

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        renderer = RaspberryPi(MC_SEVER_HOST, MC_SEVER_PORT)

        renderer.server._mc.postToChat("Building stairs")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 1

        stairs = UShapedStairs(pos)
        stairs.sections = 4
        stairs.steps = 2
        stairs.width = 3
        stairs.block = mcpi.block.IRON_BLOCK
        stairs.build()

        World.server.entity.setTilePos(World.server.getPlayerEntityId(BUILDER_NAME),
                                       stairs.end_position)

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
