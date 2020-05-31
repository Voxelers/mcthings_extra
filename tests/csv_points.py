import sys

import mcpi.block
import mcpi.minecraft
from mcthings.world import World

from mcthings_extra.csv_points import CsvPoints
from mcthings.server import Server


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))

        World.server.postToChat("Building blocks defined in a CSV file")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))

        pos.z += 1
        csv_points = CsvPoints(pos)
        csv_points.file_path = "alturas-final.csv"
        csv_points.build()
        # csv_points.unbuild()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
