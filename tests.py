import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    """Black-box test suite for the Boggle solver."""

    def setUp(self):
        """Common dictionary for reuse."""
        self.dictionary = [
            "ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT",
            "PRAT", "PRY", "QUA", "QUART", "QUARTZ", "RAT",
            "TAR", "TARP", "TEN", "WENT", "WET", "ARTY", "NOT", "QUAR"
        ]

    # --- 1. Normal case: medium grid, typical dictionary ---
    def test_normal_case(self):
        grid = [
            ["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]
        ]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertIn("TEN", result)
        self.assertIn("RAT", result)
        self.assertIn("TAR", result)

    # --- 2. Empty grid ---
    def test_empty_grid(self):
        grid = []
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])

    # --- 3. Empty dictionary ---
    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, [])
        result = game.getSolution()
        self.assertEqual(result, [])

    # --- 4. 1x1 grid (too small to form 3-letter words) ---
    def test_single_cell_grid(self):
        grid = [["T"]]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])

    # --- 5. Non-square (rectangular) grid ---
    def test_rectangular_grid(self):
        grid = [["T", "E", "N", "T"], ["A", "R", "T", "Y"]]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertIn("TEN", result)
        self.assertIn("ART", result)

    # --- 6. Grid with repeating letters ---
    def test_repeating_letters(self):
        grid = [["T", "T"], ["T", "T"]]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        # Should not error, but probably no valid words
        self.assertIsInstance(result, list)

    # --- 7. Complex pattern: test Qu tile ---
    def test_qu_tile(self):
        grid = [["Qu", "A", "R", "T"]]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertIn("QUART", result)

    # --- 8. Small dictionary with unreachable words ---
    def test_unreachable_words(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["XYZ", "QWERTY", "LONGWORD"]
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertEqual(result, [])

    # --- 9. Large grid ---
    def test_large_grid(self):
        grid = [
            ["C", "A", "T", "S"],
            ["D", "O", "G", "S"],
            ["B", "I", "R", "D"],
            ["F", "I", "S", "H"]
        ]
        dictionary = ["CAT", "DOG", "BIRD", "FISH", "CATS"]
        game = Boggle(grid, dictionary)
        result = game.getSolution()
        self.assertIn("CAT", result)
        self.assertIn("DOG", result)

    # --- 10. Words with overlapping paths ---
    def test_overlapping_paths(self):
        grid = [
            ["A", "R", "T"],
            ["T", "A", "R"],
            ["R", "T", "A"]
        ]
        game = Boggle(grid, self.dictionary)
        result = game.getSolution()
        self.assertIn("ART", result)
        self.assertIn("TAR", result)


if __name__ == "__main__":
    unittest.main()
