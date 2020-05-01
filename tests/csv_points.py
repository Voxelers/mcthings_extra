import sys

import mcpi.block
import mcpi.minecraft


from mcthings_extra.csv_points import CsvPoints
from mcthings.server import Server


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building blocks defined in a CSV file")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        pos.z += 1
        csv_points = CsvPoints(pos)
        csv_points.file_path = "alturas-final.csv"
        csv_points.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
