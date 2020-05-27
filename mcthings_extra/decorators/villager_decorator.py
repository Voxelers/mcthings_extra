# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import math

import mcpi.block
import mcpi.entity
from mcpi.vec3 import Vec3

from mcthings.decorators.decorator import Decorator
from mcthings_extra.entity import Entity


class VillagerDecorator(Decorator):
    """
    An Entity Decorator to populate the Thing.

    Add a villager to Thing
    """

    @classmethod
    def decorate(cls, thing):
        """
        Add a villager in the center of the Thing

        :return:
        """

        thing_end = thing.end_position
        thing_start = thing.position

        center_pos_x = thing_start.x + math.floor((thing_end.x - thing_start.x) / 2)
        center_pos_y = thing_start.y + math.floor((thing_end.y - thing_start.y) / 2)
        center_pos_z = thing_start.z + math.floor((thing_end.z - thing_start.z) / 2)

        entity = Entity(Vec3(center_pos_x, center_pos_y, center_pos_z))
        entity.entity = mcpi.entity.VILLAGER
        entity.spawn()

