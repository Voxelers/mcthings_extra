#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import unittest

from mcthings.world import World

from tests.base import TestBaseThing

from mcthings_extra.csv_points import CsvPoints


class TestCsvPoints(TestBaseThing):
    """Test CsvPoints Thing"""

    # TODO: Disable until set_blocks restrictions are removed
    def test_build(self):
        World.renderer.post_to_chat("Building blocks defined in a CSV file")

        self.pos.z += 1
        csv_points = CsvPoints(self.pos)
        csv_points.file_path = "data/alturas-final.csv"
        csv_points.build()
        # csv_points.unbuild()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
