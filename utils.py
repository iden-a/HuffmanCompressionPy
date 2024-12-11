# binary files handle data in 8 bits
def write_binary_file(output_path, encoded_text):
    # make sure the encoded text length is a multiple of 8
    padding = 8 - len(encoded_text) % 8

    encoded_text = '0' * padding + encoded_text # add padding to the encoded text
    with open(output_path, 'wb') as file:
        # processing by slicing it into 8 bit segments & converting each 8-bit segement into an int
        byte_array = bytearray(int(encoded_text[i:i + 8], 2) for i in range(0, len(encoded_text), 8))
        file.write(byte_array)

def read_binary_file(input_path):
    with open(input_path, 'rb') as file:
        byte_data = file.read()
        # creating a binary string and formatting into it's binary form
        binary_string = ''.join(format(byte, '08b') for byte in byte_data)

    # remove padding (the first `padding` bits are artificial)
    padding = binary_string.find('1')  # find first '1' after padding
    if padding != -1:
        binary_string = binary_string[padding:] # creating the binary string by looking at the values after the padding
    return binary_string

def write_text_file(output_path, text):
    # writing the text into the output path
    with open(output_path, 'w') as file:
        file.write(text)

def read_text_file(input_path):
    # reading the text from the input path
    with open(input_path, 'r') as file:
        return file.read()

def compression_ratio(original_size, compressed_size):
    # calculating the compression ratio by dividing the compressed size by the original file size
    compression_ratio = (1 - (compressed_size / original_size)) * 100
    return compression_ratio
