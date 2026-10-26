import heapq
import math
 
 
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
 
    def __lt__(self, other):
        return self.freq < other.freq
 
 
def build_huffman_tree(freq_table):
    heap = [Node(sym, freq) for sym, freq in freq_table.items()]
    heapq.heapify(heap)
 
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
 
    return heap[0]
 
 
def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.symbol is not None:
        codes[node.symbol] = current_code or "0"
        return codes
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes
 
 
# Example usage: symbols with their probabilities
symbols = {
    'A': 0.4,
    'B': 0.2,
    'C': 0.2,
    'D': 0.1,
    'E': 0.1,
}
 
tree = build_huffman_tree(symbols)
codes = generate_codes(tree)
 
print("Symbol : Probability : Huffman Code")
avg_length = 0
for sym in symbols:
    print(f"{sym}      : {symbols[sym]:<10} : {codes[sym]}")
    avg_length += symbols[sym] * len(codes[sym])
 
print(f"\nAverage code length: {avg_length:.3f} bits/symbol")
 
entropy = -sum(p * math.log2(p) for p in symbols.values())
print(f"Entropy: {entropy:.3f} bits/symbol")
 
efficiency = (entropy / avg_length) * 100
print(f"Coding efficiency: {efficiency:.2f}%")
