from django.test import TestCase
from django.contrib.gis.geos import Point
from models import Node, Edge
from astar import bidirectional_astar

class TestAStar(TestCase):	
	def setUp(self):
		self.new_york = Node(coordinates=Point(40, 73))
		self.austin = Node(coordinates=Point(30, 97))
		self.san_fran = Node(coordinates=Point(37, 122))
		self.chicago = Node(coordinates=Point(41, 87))
		
		self.new_york.save()
		self.austin.save()
		self.san_fran.save()
		self.chicago.save()

		Edge(node_src=self.new_york, node_sink=self.chicago).save()
		Edge(node_src=self.chicago, node_sink=self.san_fran).save()

		Edge(node_src=self.new_york, node_sink=self.austin).save()
		Edge(node_src=self.austin, node_sink=self.san_fran).save()

		Edge(node_src=self.san_fran, node_sink=self.new_york).save()
		
	def test_find_path(self):
		start = self.new_york;
		goal = self.san_fran;

		path = bidirectional_astar(start, goal)
		self.assertEqual(path[0].id, self.new_york.id)
		self.assertEqual(path[1].id, self.chicago.id)
		self.assertEqual(path[2].id, self.san_fran.id)

