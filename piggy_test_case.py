import device
import time
import unittest

class PiggyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.myDevice = device.Device()

    @classmethod
    def tearDownClass(self):
        self.myDevice.close()

    def setUp(self):
        self.myDevice.restart()

    def tearDown(self):
        pass

    def wait(self, sec):
        time.sleep(sec)