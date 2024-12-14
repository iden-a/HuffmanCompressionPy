#priority queue
import heapq

# Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# storing each character and it's frequency in a dictionary 
def calculate_frequency(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq
    
def build_huffman_tree(frequency_dict):
    if not frequency_dict:  # if the frequency dictionary is empty
        return None

    # adding each element in the dictionary into the heap
    heap = [Node(char, freq) for char, freq in frequency_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq) # merging nodes based on frequencies
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] # return the root 

# generate Huffman codes for each character by traversing the tree.
def generate_codes(node, current_code="", code_table=None):
    if code_table is None:
        code_table = {}

    # If a node is None, it represents an internal node created by merging two child nodes.
    if node is None:
        return 
    if node.char is not None:  # Leaf nodes are unmerged nodes, this is where we assign codes
        code_table[node.char] = current_code
        return code_table

    generate_codes(node.left, current_code + "0", code_table) # the nodes on the lefthand side receive 0
    generate_codes(node.right, current_code + "1", code_table) # nodes on the righthand receive 1

    return code_table

# given the text, we search the code_table to create an encoded binary string
def encode_text(text, code_table):
    return ''.join(code_table[char] for char in text)

# use the Huffman tree to reverse the encoding process and retrieve the original text.
def decode_text(encoded_text, root):
    decoded_text = []
    # start at the root 
    current = root
    for bit in encoded_text:
        if bit == '0': 
            current = current.left
        else:
            current = current.right

        # We have reached a leaf node, this means we have decoded a character
        if current.char:
            decoded_text.append(current.char)
            current = root

    return ''.join(decoded_text)

