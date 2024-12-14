import unittest
import tempfile
from utils import write_binary_file, read_binary_file, read_text_file, write_text_file, compression_ratio

class TestHuffanEncoding(unittest.TestCase):
    # testing against invalid file paths
    def test_invalid_path(self):
        input_path = "data/nonexistent.txt"
        with self.assertRaises(FileNotFoundError):
            read_text_file(input_path)

    # testing when user provides a text file that is empty
    def test_empty_text(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file_path = temp_file.name

        try:
            text = read_text_file(temp_file_path)
            self.assertEqual(text, "", "Expected an empty string for an empty text file." )
        finally:
            import os
            os.remove(temp_file_path)

    # making sure the binart data matches what is being written
    def test_write_binary_file(self):
        binary_data = "1010100011110000"
        with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
            temp_file_path = temp_file.name
        
        try:
            write_binary_file(temp_file_path, binary_data)
            with open(temp_file_path, 'rb') as file:
                written_data = file.read()
                written_binary_string = ''.join(format(byte, '08b') for byte in written_data)

            # to account for padding that is being done in the write_binary_file function
            padding = 8 - len(binary_data) % 8
            expected_data = '0' * padding + binary_data

            self.assertEqual(written_binary_string, expected_data, "Binary data mismatch")
        finally:
            import os
            os.remove(temp_file_path)

    def test_read_binary_file(self): #TODO
        pass

    def test_compression_ratio(self): #TODO
        pass


        




    