# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Familia de Lorenzo

from mcpi.vec3 import Vec3
from mcthings.scene import Scene
from mcthings.thing import Thing
from mcthings.world import World


class StairsSnail(Thing):
    """ Create snail stairs with sections including steps of width """

    sections = 3
    steps = 5
    width = 5

    def build(self):
        mc = World.server

        direction = 0

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        for section in range(0, self.sections, 1):
            if direction == 0:
                for eje_y in range(0, self.steps, 1):
                    for eje_x in range(0, self.width, 1):
                        mc.setBlock((init_x + eje_x),
                                    ((self.steps * section) + init_y + eje_y),
                                    (init_z + eje_y) + (direction * self.steps),
                                    self.block)
                direction = 1
            elif direction == 1:
                for eje_y in range(0, self.steps, 1):
                    for eje_x in range(0, self.width, 1):
                        mc.setBlock((init_x + eje_x + self.width),
                                    ((self.steps * section) + init_y + eje_y),
                                    (init_z - eje_y - 1) + (direction * self.steps),
                                    self.block)
                direction = 0

        end_x = init_x + 2 * self.width
        if self.sections == 1:
            end_x = init_x + self.width
        end_y = init_y + self.sections * self.steps + 1
        if self.sections % 2 != 0:
            end_z = init_z + self.steps
        else:
            end_z = init_z

        self._end_position = Vec3(end_x, end_y, end_z)
