import unittest

from citrix_netscaler_image_management import __version__


class PackageTest(unittest.TestCase):
    def test_package_version(self):
        self.assertEqual(__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
