# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging

import mcpi.entity
from mcpi.connection import RequestError

from mcthings.scene import Scene
from ._version import __version__

from mcthings.world import World


class Entity:
    entity = mcpi.entity.BAT

    def __init__(self, position=None):
        """
        Create a entity
        :param position: spawn position
        """

        self._position = None
        if position:
            self._position = mcpi.vec3.Vec3(position.x, position.y, position.z)

        # McThing Extras version which created this Thing
        self._version = __version__

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    def spawn(self):
        try:
            World.server.spawnEntity(self.position.x, self.position.y,
                                     self.position.z, self.entity)
        except RequestError:
            logging.debug("Server can not spawn entities")

    def build(self):
        """ Share this API with Thing so Scene can recreate more easily the scenes """
        self.spawn()

    def unbuild(self):
        """ An entity can not be unbuilt """
        pass
