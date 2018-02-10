import unittest
from main import getRepos, getNumCommits

class TestGithub(unittest.TestCase):
    def testRepo(self):
        repos = getRepos('johnmottole')
        self.assertIn('AgileMethodsProject',repos)
        self.assertIn('finalProj',repos)
        self.assertIn('iOSBluetoothCommunication',repos)
        self.assertIn('JointTech',repos)
        self.assertIn('ssw322-group1',repos)
        self.assertIn('Travel-Time',repos)
    def testRepo2(self):
        repos = getRepos('stevenssec')
        self.assertIn('Alexa',repos)
    def testNumCommits(self):
        self.assertGreaterEqual(getNumCommits('johnmottole','AgileMethodsProject'),30)
        self.assertGreaterEqual(getNumCommits('johnmottole','finalProj'),5)
        self.assertGreaterEqual(getNumCommits('johnmottole','iOSBluetoothCommunication'),2)
        self.assertGreaterEqual(getNumCommits('johnmottole','ssw322-group1'),18)
        self.assertGreaterEqual(getNumCommits('stevenssec','Alexa'),4)




