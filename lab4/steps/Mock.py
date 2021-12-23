import unittest
from unittest.mock import Mock
from roots import get_roots

class TestQr(unittest.TestCase):
	def test_get_roots(self):
		mockRoot = Mock(return_value = 412)
		get_roots(mockRoot(), 2, 1)


if __name__ == "__main__":
	unittest.main()
