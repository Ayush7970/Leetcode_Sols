
import heapq
from collections import Counter 


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    
def build_huffman_tree(text):

    # if empty
    if not text:
        return None
    
    freq_map = Counter(text)
    heap = []

    for char, freq in freq_map.items():
        heapq.heappush(heap, Node(char, freq))
    
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merge_node = Node(None, left.freq + right.freq)

        merge_node.left = left
        merge_node.right = right

        heapq.heappush(heap, merge_node)
    
    return heap[0]

def build_codes(root):

    codes = {}

    def dfs(node, code):

        if not node:
            return
    
        if node.char is not None:
            codes[node.char] = code if code else "0" # if nothing is there then we store 0, test it
        
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")

        
    dfs(root, "")
    return codes



def huffman_encodes(text):
    if not text:
        return "", None, {}

    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded_text = "".join(codes[ch] for ch in text)

    return encoded_text, root, codes


def huffman_decodes(encoded_text, root):
    if not root:
        return ""
    
    if root.left is None and root.right is None:
        return root.char * len(encoded_text)
    
    result = []
    curr = root

    for bit in encoded_text:

        if bit == "0":
            curr = curr.left
        else:
            curr = curr.right
        
        if curr.char is not None:
            result.append(curr.char)
            curr = root
    
    return "".join(result)



text = "abbcbcsubvgre9wg9w3bfgb9w4b9u"
encoded_text, root, codes = huffman_encodes(text)

print("Codes:", codes)
print("Encoded:", encoded_text)
print("Decoded:", huffman_decodes(encoded_text, root))






    


