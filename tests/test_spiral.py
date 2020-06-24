#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi.block
import mcpi.minecraft
from mcthings.world import World

from tests.base import TestBaseThing

from mcthings_extra.spiral import Spiral


class TestSpiral(TestBaseThing):
    """Test Spiral Thing"""

    # TODO: Disable until set_blocks restrictions are removed
    def test_build(self):
        World.renderer.post_to_chat("Building a spiral")
        self.pos.z -= 1

        spiral = Spiral(self.pos)
        spiral.block = mcpi.block.WOOD
        spiral.build()

        mc = World.renderer.server.mc
        mc.entity.setTilePos(mc.getPlayerEntityId(self.BUILDER_NAME), spiral.end_position)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')