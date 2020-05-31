# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Familia de Lorenzo

from mcpi.vec3 import Vec3
from mcthings.scene import Scene
from mcthings.thing import Thing
from mcthings.world import World


class Spiral(Thing):

    size = 10
    height = 10

    def build(self):
        mc = World.server

        size = 10
        height = 3

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        for i in range(1, size, 2):
            mc.setBlocks(init_x + i, init_y, init_z + i - 1,
                         init_x + i, init_y + height, init_z - i,
                         self.block)

            mc.setBlocks(init_x + i, init_y, init_z - i,
                         init_x - i, init_y + height, init_z - i,
                         self.block)

            mc.setBlocks(init_x - i, init_y, init_z - i,
                         init_x - i, init_y + height, init_z + i + 1,
                         self.block)

            mc.setBlocks(init_x - i, init_y, init_z + i + 1,
                         init_x + i + 2, init_y + height, init_z + i + 1,
                         self.block)

            self._end_position = Vec3(init_x + i + 2, init_y + height, init_z + i + 1)
