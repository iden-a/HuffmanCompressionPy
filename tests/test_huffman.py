import unittest
from huffman import calculate_frequency,build_huffman_tree, generate_codes,encode_text, decode_text

class TestHuffanEncoding(unittest.TestCase):

    # testing that the huffman tree is accurately constructed
    def test_build_huffman_tree(self):
        frequency = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        root = build_huffman_tree(frequency_dict=frequency)

        self.assertEqual(root.freq, sum(frequency.values()), "Root frequency should equal the sum of all frequencies")
        self.assertIsNotNone(root.left, "Root should have a left child")
        self.assertIsNotNone(root.right, "Root should have a right child")

    # testing possible edge cases that may arise
    def test_encode_decode(self):
        test_cases = [
        ("This is a test string", "Normal case with spaces"),
        ("!@#$$%^&*", "String with special characters"),
        ("", "Empty string")
    ]

        for text, case_idx in test_cases:
            with self.subTest(case=case_idx):
                freq = calculate_frequency(text)
                tree = build_huffman_tree(freq)
                codes = generate_codes(tree)
                encoded_text = encode_text(text, codes)
                decoded_text = decode_text(encoded_text, tree)

                self.assertEqual(text, decoded_text, f"Decoded text does not match original text for case: {case_idx}")
        





    


