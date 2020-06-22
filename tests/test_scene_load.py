#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.scene import Scene
from mcthings.world import World

from tests.base import TestBaseThing


class TestLoadScene(TestBaseThing):
    """Test the loading of scenes """

    # TODO: Disable until serialize can be done (remove renderer from Scene and Thing)
    def test_build(self):
        World.renderer.post_to_chat("Building a scene from a file")

        self.pos.z -= 30

        # Let's load the scene and build it
        scene = Scene()
        scene.load("mct/scene_rainbow.mct")
        # Move the scene to the player position
        scene.move(self.pos)
        scene.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')