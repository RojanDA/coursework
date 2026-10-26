import numpy as np
from scipy.fftpack import dct, idct
 
# Sample 8x8 block of pixel intensities (grayscale)
block = np.array([
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94],
], dtype=float)
 
# Step 1: Level shift (subtract 128)
shifted = block - 128
 
 
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')
 
 
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')
 
 
# Step 2: Apply 2D DCT
dct_block = dct2(shifted)
 
# Standard JPEG luminance quantization table
quant_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99],
])
 
# Step 3: Quantize (divide and round)
quantized = np.round(dct_block / quant_table)
 
print("Quantized DCT coefficients:")
print(quantized)
 
nonzero = np.count_nonzero(quantized)
print(f"\nNon-zero coefficients: {nonzero} out of 64")
 
# Step 4: Reconstruct (dequantize + inverse DCT) to see the loss
dequantized = quantized * quant_table
reconstructed = idct2(dequantized) + 128
 
print("\nReconstructed block (after compression/decompression):")
print(np.round(reconstructed))
 
mse = np.mean((block - reconstructed) ** 2)
print(f"\nMean Squared Error vs original: {mse:.2f}")
