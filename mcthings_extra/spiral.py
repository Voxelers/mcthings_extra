# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Familia de Lorenzo

from mcpi.vec3 import Vec3
from mcthings.thing import Thing


class Spiral(Thing):

    size = 10
    height = 10

    def create(self):

        size = 10
        height = 3

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        for i in range(1, size, 2):
            self.set_blocks(Vec3(init_x + i, init_y, init_z + i - 1),
                            Vec3(init_x + i, init_y + height, init_z - i),
                            self.block.id)

            self.set_blocks(Vec3(init_x + i, init_y, init_z - i),
                            Vec3(init_x - i, init_y + height, init_z - i),
                            self.block.id)

            self.set_blocks(Vec3(init_x - i, init_y, init_z - i),
                            Vec3(init_x - i, init_y + height, init_z + i + 1),
                            self.block.id)

            self.set_blocks(Vec3(init_x - i, init_y, init_z + i + 1),
                            Vec3(init_x + i + 2, init_y + height, init_z + i + 1),
                            self.block.id)

            self._end_position = Vec3(init_x + i + 2, init_y + height, init_z + i + 1)
