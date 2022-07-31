import unittest
from dst.graph import Point, Network


class TestPoint(unittest.TestCase):

    def test_create_point(self):
        point = Point('A')
        print(point.__dict__)
        self.assertTrue(isinstance(point, Point))


    def test_add_point_neighbors(self):
        pass

    def test_get_point_connections(self):
        pass

    def test_get_connection_cost_to_neighbor(self):
        pass


class TestNetwork(unittest.TestCase):

    def test_create_initial_point_in_network(self):
        pass

    def test_add_more_network_connection_points_in_network(self):
        pass

    def test_get_single_connection_point_in_network(self):
        pass

    def test_get_all_connection_points_in_network(self):
        pass


if __name__ == '__main__':
    unittest.main()