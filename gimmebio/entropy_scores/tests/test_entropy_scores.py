"""Test suite for kmer."""

from unittest import TestCase
from os.path import dirname, join

from gimmebio.entropy_scores import entropy_score, clump_score


BAM_FILE = join(dirname(__file__), 'test_entropy_scores.bam')


class TestEntropyScores(TestCase):
    """Test suite for entropy scores."""

    def test_entropy_scores(self):
        """Test that entropy score works."""
        val = entropy_score(BAM_FILE)
        self.assertTrue(val >= 0)
        self.assertTrue(val <= 1)

    def test_clump_scores(self):
        """Test that clump score works."""
        val = clump_score(BAM_FILE)
        self.assertTrue(val >= 0)
        self.assertTrue(val <= 1)