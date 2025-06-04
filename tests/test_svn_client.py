import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from svn_mcp import svn_client

class TestSVNClient(unittest.TestCase):
    @mock.patch('subprocess.run')
    def test_checkout(self, mock_run):
        svn_client.checkout('http://example.com/repo', 'dest')
        mock_run.assert_called_with([
            'svn', 'checkout', 'http://example.com/repo', 'dest'
        ], check=True, capture_output=True, text=True)

    @mock.patch('subprocess.run')
    def test_commit(self, mock_run):
        svn_client.commit('msg')
        mock_run.assert_called_with([
            'svn', 'commit', '-m', 'msg'
        ], check=True, capture_output=True, text=True)


if __name__ == '__main__':
    unittest.main()
