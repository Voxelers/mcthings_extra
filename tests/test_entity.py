#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import sys

import mcpi.block
import mcpi.entity
from mcpi.vec3 import Vec3
from mcthings.decorators.light_decorator import LightDecorator
from mcthings.house import House
from mcthings.server import Server
from mcthings.world import World

from mcthings_extra.decorators.villager_decorator import VillagerDecorator

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))

        World.server.postToChat("Spawning entities in Minecraft")
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))

        # Let's create a Scene and populate it with Entities
        house = House(Vec3(pos.x + 5, pos.y, pos.z))
        house.height = 4
        house.width = 10
        house.length = 10
        house.build()

        house.add_decorator(VillagerDecorator)
        house.add_decorator(LightDecorator)

        house.decorate()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
