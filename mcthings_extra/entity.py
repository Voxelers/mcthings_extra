# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.entity

from mcthings.scene import Scene
from ._version import __version__


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

        # Add the entity to the scene
        Scene.add(self)

        # McThing version which created this Thing
        self._version = __version__

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    def spawn(self):
        Scene.server.spawnEntity(self.position.x, self.position.y,
                                 self.position.z, self.entity)

    def build(self):
        """ Share this API with Thing so Scene can recreate more easily the scenes """
        self.spawn()

    def unbuild(self):
        """ An entity can not be unbuilt """
        pass

    def populate(self, thing):
        """
        Populate a thing (Thing) with this entity

        :param thing: Thing to be populated
        :return:
        """

        margin = 3

        p = thing.position
        self._position = p
        Scene.server.spawnEntity(p.x + margin,
                                 p.y,
                                 p.z + margin,
                                 self.entity)
