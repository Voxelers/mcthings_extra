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

        World.server.postToChat("Building a scene from a file")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        pos.z -= 50

        # Let's load the scene and build it
        scene = Scene()
        scene.load("scene_rainbow.mct")
        # Move the scene to the player position
        scene.move(pos)
        scene.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
