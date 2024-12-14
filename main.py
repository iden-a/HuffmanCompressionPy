import os
from huffman import calculate_frequency, build_huffman_tree, generate_codes, encode_text, decode_text
from utils import read_text_file, write_binary_file, read_binary_file, write_text_file, compression_ratio

def main():
    print("\nWelcome to the HuffmanPy Compression System!")
    print("\nFollow These Steps For A Smooth Process ... ")
    print("- Add The Text File You Would Like To Compress Into The `data` Directory")
    print("- Input and Output Files MUST End in .txt ")
    print("- Compressed File MUST End in .bin ")
    print("_____________________________________________________________________________")

    # file paths
    user_input = input("\nEnter the Text File Name (.txt): ")
    user_compressed = input("Enter the Compressed File Name (.bin): ")
    user_decompressed = input("Enter the Decompressed File Name (.txt): ")

    input_path = "data/" + user_input
    compressed_path = "data/" + user_compressed
    decompressed_path = "data/" + user_decompressed

    
    # read the input text file
    try:
        text = read_text_file(input_path)
        if not text.strip():  # check if the text is empty or contains only whitespace
            print("\nThe input text file is empty. Please provide a valid text file.")
            return
    except FileNotFoundError as error:
        print("\nMake Sure The File Exists in the `data` Directory")            
        print(error)
        return
    
    try:
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
        print(f"\nCompression Ratio: {compression_ratio(original_size, compressed_size):.2f}%")

        # decode the text
        binary_string = read_binary_file(compressed_path)
        decoded_text = decode_text(binary_string, huffman_tree)

        # write the decompressed text to a file
        write_text_file(decompressed_path, decoded_text)

        # verifying the results to see if we have successfully decoded the text
        print("Decompression Complete. Files Generated Successfully.")
        print(f"Original Text Matches Decompressed Text: {text == decoded_text}")

        print("\nNavigate to the `data` Directory to View The Results.")
        print("Thanks For Using the HuffmanPy Compression System! ")
        
    except Exception as error:
        print(error)
        print("Error occured during compression or decompression process.")

if __name__ == "__main__":
    main()
