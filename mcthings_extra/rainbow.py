from mcpi import block
from mcpi.vec3 import Vec3
from mcthings.scene import Scene
from mcthings.thing import Thing

from math import *

# Based on Rainbow code written by zhuowei and retrieved from URL below:
# http://www.minecraftforum.net/topic/1638036-my-first-script-for-minecraft-pi-api-a-rainbow/
from mcthings.world import World

colors = [14, 1, 4, 5, 3, 11, 10]


class Rainbow(Thing):

    height = 20
    """ Height of the rainbow """
    block = block.WOOL.id

    def build(self):
        mc = World.server
        mc.setBlocks(-64, 0, 0, 64, self.height + len(colors), 0, 0)
        for x in range(0, 128):
            for color in range(0, len(colors)):
                y = sin((x / 128.0) * pi) * self.height + color
                mc.setBlock(self.position.x + x - 64, int(y), self.position.z,
                            self.block, colors[len(colors) - 1 - color])
        end_x = self.position.x - 64 + 128
        self._end_position = Vec3(end_x, self.position.y, self.position.z)