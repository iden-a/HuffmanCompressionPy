# HuffmanCompressionPy

## Project Overview
The **HuffmanCompressionPy** project is a text file compression and decompression program utilizing the **Huffman Coding Algorithm**. The program reads a text file as input, compresses it using Huffman coding, and writes the compressed data to a binary file. It then provides functionality to decompress the binary file back into its original text form, restoring the file to its original state.

### Key Features:
- **Text File Compression**: Compresses a text file using the Huffman coding algorithm.
- **Huffman Tree Generation**: Builds a Huffman tree to produce a code table for encoding.
- **Binary File Output**: Writes the compressed data to a binary file.
- **Decompression**: Allows users to decompress the binary file and restore the original text.

## How It Works
1. **Text Input**: The program reads an input text file and calculates the frequency of each character.
2. **Huffman Tree Construction**: A Huffman tree is built using a priority queue to generate a minimal encoding.
3. **Encoding**: The input text is encoded based on the generated Huffman tree.
4. **Binary Output**: The encoded text is written to a binary file.
5. **Decompression**: The program can read the binary file, decode the content using the Huffman tree, and restore the original text.

### Compression Ratio
The program calculates and displays the **compression ratio** comparing the size of the original text file and the size of the compressed binary file.

## Project Structure
  - `main.py`: The entry point of the program.
  - `huffman.py`: Contains the implementation for the Huffman tree construction and encoding/decoding logic.
  - `utils.py`: Includes utility functions for file handling and compression ratio calculation.

## Future Enhancements
- **Multithreading**: Implement parallel compression and decompression to handle larger files more efficiently.
- **Graphical User Interface (GUI)**: Develop a simple GUI for easier interaction with the program, allowing drag-and-drop for file compression.

## Run The Program
1. Clone this repository:
   ```bash
   git clone https://github.com/iden-a/HuffmanCompressionPy.git 

2. Navigate to the project directory:
   ```bash
   cd HuffmanPy

3. Run The Program:
   ```bash
   python3 main.py
   


