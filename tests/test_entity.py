#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3
from mcthings.decorators.light_decorator import LightDecorator
from mcthings.house import House
from mcthings.world import World
from tests.base import TestBaseThing

from mcthings_extra.decorators.villager_decorator import VillagerDecorator

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


class TestEntity(TestBaseThing):
    """Test Entity Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Spawning entities in Minecraft")

        # Let's create a Scene and populate it with Entities
        house = House(Vec3(self.pos.x + 5, self.pos.y, self.pos.z))
        house.height = 4
        house.width = 10
        house.length = 10
        house.build()

        house.add_decorator(VillagerDecorator)
        house.add_decorator(LightDecorator)

        house.decorate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
