#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.world import World

from tests.base import TestBaseThing

from mcthings_extra.rainbow import Rainbow


class TestRainbow(TestBaseThing):
    """Test Block Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a rainbow")

        self.pos.z -= 20

        rainbow = Rainbow(self.pos)
        rainbow.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
