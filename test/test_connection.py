import unittest
from solr_instance import SolrInstance
from solrcloudpy import Connection
from solrcloudpy import Collection

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.solrprocess = SolrInstance("solr1")
        self.solrprocess.start()
        self.solrprocess.wait_ready()
        self.conn = Connection()

    def tearDown(self):
        self.conn.test2.delete()
        self.solrprocess.terminate()

    def test_list(self):
        colls = self.conn.list()
        self.assertTrue(len(colls)>=1)

    def test_live_nodes(self):
        nodes = self.conn.live_nodes
        self.assertTrue(len(nodes)==1)

    def test_cluster_leader(self):
        leader = self.conn.cluster_leader
        self.assertTrue(leader is not None)

    def test_create_collection(self):
        coll = self.conn.create_collection('test2')
        self.assertTrue(isinstance(coll,Collection))

if __name__ == '__main__':
    unittest.main()
