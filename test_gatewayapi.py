# test_gatewayapi.py
"""
Tests for GatewayAPI module.
"""

import unittest
from gatewayapi import GatewayAPI

class TestGatewayAPI(unittest.TestCase):
    """Test cases for GatewayAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GatewayAPI()
        self.assertIsInstance(instance, GatewayAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GatewayAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
