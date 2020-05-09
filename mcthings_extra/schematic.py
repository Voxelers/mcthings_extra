# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo

from nbt import nbt

from mcpi import block
from mcpi.vec3 import Vec3
from mcthings.scene import Scene
from mcthings.thing import Thing


class Schematic(Thing):
    blocks_field = 'Blocks'
    data_field = 'Data'

    def build(self):
        mc = Scene.server

        if not self.file_path:
            RuntimeError("Missing file_path param")

        schematic = nbt.NBTFile(self.file_path, 'rb')

        size_x = schematic["Width"].value
        size_y = schematic["Height"].value
        size_z = schematic["Length"].value

        blocks = schematic[self.blocks_field].value

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        blocks = schematic[self.blocks_field]
        data = schematic[self.data_field]

        for y in range(0, size_y):
            for z in range(0, size_z):
                for x in range(0, size_x):
                    i = x + size_x * z + (size_x * size_z) * y
                    b = blocks[i]
                    if b != 0:
                        d = data[i] & 0b00001111  # lower 4 bits
                        mc.setBlock(init_x + x, init_y + y, init_z + z, b, d)

