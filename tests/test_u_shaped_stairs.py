#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import sys
import unittest

import mcpi.block
import mcpi.minecraft
from mcthings.world import World

from tests.base import TestBaseThing

from mcthings_extra.u_shaped_stairs import UShapedStairs


class TestUShapedStairs(TestBaseThing):
    """Test UShapedStairs Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building u shaped stairs")

        self.pos.z -= 1

        stairs = UShapedStairs(self.pos)
        stairs.sections = 4
        stairs.steps = 2
        stairs.width = 3
        stairs.block = mcpi.block.IRON_BLOCK
        stairs.build()

        mc = World.renderer.server.mc
        mc.entity.setTilePos(mc.getPlayerEntityId(self.BUILDER_NAME), stairs.end_position)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
