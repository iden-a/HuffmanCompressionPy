import os
from huffman import calculate_frequency, build_huffman_tree, generate_codes, encode_text, decode_text
from utils import read_text_file, write_binary_file, read_binary_file, write_text_file, compression_ratio

def main():
    # file paths
    input_path = "data/input.txt"
    compressed_path = "data/compressed.bin"
    decompressed_path = "data/decompressed.txt"

    # read the input text file
    text = read_text_file(input_path)

    # encode the text
    freq = calculate_frequency(text)
    huffman_tree = build_huffman_tree(freq)

    code_table = generate_codes(huffman_tree)
    encoded_text = encode_text(text, code_table)

    # write the encoded text to a binary file
    write_binary_file(compressed_path, encoded_text)

    # measure and display compression ratio
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_path)
    print(f"Compression Ratio: {compression_ratio(original_size, compressed_size):.2f}%")

    # decode the text
    binary_string = read_binary_file(compressed_path)
    decoded_text = decode_text(binary_string, huffman_tree)

    # write the decompressed text to a file
    write_text_file(decompressed_path, decoded_text)

    # verifying the results to ensure that we have successfully decoded the text
    print("Decompression complete. Files generated successfully.")
    print(f"Original text matches decompressed text: {text == decoded_text}")

if __name__ == "__main__":
    main()
