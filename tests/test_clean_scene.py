import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.server import Server
from mcthings.world import World
from minecraftstuff import MinecraftDrawing

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))

        World.server.postToChat("Cleaning a scene")

        # Let's load the scene and build it
        scene = Scene()
        scene.load("scene_rainbow.mct")
        scene.unbuild()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
