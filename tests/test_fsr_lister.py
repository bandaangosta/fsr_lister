import unittest

import fsr_lister


class Fsr_listerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fsr_lister.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to FSR Lister', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
