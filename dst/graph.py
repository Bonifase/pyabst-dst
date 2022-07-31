# Copyright (C) Bonifase Orwa - All Rights Reserved.


class Point:

    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_neighbor(self, nbr, cost=0):
        self.connections[nbr] = cost

    def get_connections(self):
        return self.connections.keys()

    def connection_cost(self, nbr):
        return self.connections.get(nbr)

    def __str__(self):
        return f"{str(self.key)} connected to: {str([x.key for x in self.connections])}"



class Network:

    def __init__(self):
        self._points = {}
        self.size = 0

    def new_point(self, key):
        """
            Add a point to the Graph network with the id of key
            Time complexity is O(1) as we are only adding a single
            new point which does not affect any other points.
        """
        #add 1 to the number of size attribute
        self.size += 1
        #instantiate a new Point class
        point = Point(key)
        #add the point with the key to the points dictionary
        self._points[key] = point
        #return the point created
        return point

    def get_point(self, key):
        """
            If a point with key is in Graph then return the point
            Time complexity is O(1) as we are simply checking whether
            the key exists or not in a dictionary and returning it
        """
        #use the get method to return the Point if it exists
        #otherwise it will return None
        return self._points.get(key)

    def __contains__(self, key):
        """
            Check whether point with key is in the Graph
            Time complexity is O(1) as we are simply checking whether
            the key is in in the dictionary or not
        """
        #returns True or False depending if in list
        return key in self._points

    def add_connection(self, start_point, destination, weight=0):
        """
            Add an edge to connect two points of destination and start_point with weight
            assuming directed graph
            Time complexity of O(1) as adding vertices if they don't
            exist and then add neighbor
        """
        #add points if they do not exist
        if destination not in self._points:
            self.new_point(destination)
        if start_point not in self._points:
            self.new_point(start_point)
        #then add Neighbor from f start_point destination with weight
        self._points[start_point].add_neighbor(self._points[destination], weight)

    def connection_points(self):
        """
            Return all the connection points in the graph
            Time complexity is O(1) as we simply return all the keys
            in the points dictionary
        """

        return self._points.keys()


if __name__ == '__main__':
    network = Network()
    network.new_point('A')
    network.add_connection('A', 'B', 1)
    network.add_connection('A', 'D', 5)
    network.add_connection('B', 'C', 2)
    network.add_connection('B', 'D', 7)
    network.add_connection('C', 'F', 1)
    network.add_connection('D', 'E', 3)
    network.add_connection('E', 'F', 8)
    network.add_connection('F', 'D', 1)

    print(network.connection_points())
    print(network.size)