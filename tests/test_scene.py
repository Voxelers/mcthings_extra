#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest


from mcthings.pyramid import Pyramid
from mcthings.world import World
from tests.base import TestBaseThing

from mcthings_extra.rainbow import Rainbow

# In this scene Things from McThings and McThings-Drawing are mixed


class TestSpiral(TestBaseThing):
    """Test Spiral Thing"""

    # TODO: Disable until serialize can be done (remove renderer from Scene and Thing)
    def test_build(self):

        World.renderer.post_to_chat("Building a rainbow")
        self.pos.z -= 20

        pyr = Pyramid(self.pos)
        pyr.build()

        rainbow = Rainbow(pyr.end_position)
        rainbow.build()

        World.scenes[0].save("mct/scene_rainbow.mct")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
