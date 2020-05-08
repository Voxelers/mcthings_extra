import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server

from mcthings_extra.schematic import Schematic
from mcthings_extra.stairs_snail import StairsSnail

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 9711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building from a schematic file")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 10

        schematic = Schematic(pos)
        # 2012: https://www.minecraft-schematics.com/schematic/68/
        schematic.file_path = "pirate-boat.schematic"
        # 2014
        # schematic.file_path = "viking-boat.schematic"
        # 2016
        # schematic.file_path = "us-navy-pbr-naval.schematic"
        # 2018
        # schematic.file_path = "trawler-fishing.schematic"
        # 2020
        # schematic.file_path = "one-chunk-drakkar.schematic"
        schematic.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
