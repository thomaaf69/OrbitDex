# test_orbitdex.py
"""
Tests for OrbitDex module.
"""

import unittest
from orbitdex import OrbitDex

class TestOrbitDex(unittest.TestCase):
    """Test cases for OrbitDex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrbitDex()
        self.assertIsInstance(instance, OrbitDex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrbitDex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
