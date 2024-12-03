# Steganography-ImageHiding
Implementation of a Python-based steganography tool for hiding and extracting secret images within cover images using bitwise operations.

---

## Table of Contents
1. [Summary](#summary) 
   1.1 [Purpose of the Assignment](#purpose-of-the-assignment)
   1.2 [Key Objectives](#key-objectives)  
3. [Approach](#approach)  
   2.1 [Overview of the Methodology](#overview-of-the-methodology)  
   2.2 [Steps for Hiding the Image](#steps-for-hiding-the-image)  
   2.3 [Steps for Extracting the Image](#steps-for-extracting-the-image)  
4. [Code](#code)  
   3.1 [Key Operations for Hiding the Image](#key-operations-for-hiding-the-image)  
   3.2 [Key Operations for Extracting the Image](#key-operations-for-extracting-the-image)  
   3.3 [Error Handling and Validation](#error-handling-and-validation)  
5. [Results](#results)  
   4.1 [Test Case 1: Hiding a Secret Image](#test-case-1-hiding-a-secret-image)  
   4.2 [Test Case 2: Extracting the Hidden Image](#test-case-2-extracting-the-hidden-image)  
   4.3 [Observations](#observations)  
6. [Usage](#usage)  
7. [Conclusion](#conclusion)  

---

## Summary

### Purpose of the Assignment
Steganography is the practice of concealing information within non-secret objects or files to securely transmit sensitive data. This assignment focuses on implementing a Python-based steganography tool to hide and retrieve a secret image within a larger cover image.

### Key Objectives
- To implement an embedding process that encodes a secret image into a cover image.
- To enable decoding of the hidden image with minimal distortion of the cover image.
- To ensure usability and robustness of the tool.

---

## Approach

### Overview of the Methodology
The solution leverages **bitwise operations** for embedding and extracting images. The process ensures minimal changes to the cover image while securely hiding the secret image. 

### Steps for Hiding the Image
1. Load the **cover image** and **secret image** in grayscale.
2. Resize the **secret image** to match the dimensions of the **cover image**.
3. Modify the least significant bits (LSBs) of the **cover image** to encode the most significant bits (MSBs) of the **secret image**.
4. Save the resulting stego image.

### Steps for Extracting the Image
1. Load the **stego image** in grayscale.
2. Extract the encoded bits from the LSBs of the **stego image**.
3. Reconstruct the hidden **secret image** from these bits.
4. Save the reconstructed **secret image**.


---

## Key Operations for Hiding the Image

```python
# Hiding the secret image into the cover image
stego_image = (cover_image & 0xF0) | (secret_image >> 4)
cv2.imwrite(output_path, stego_image)
```

- **`cover_image & 0xF0`**: Clears the LSBs of the cover image.
- **`secret_image >> 4`**: Extracts the MSBs of the secret image for embedding.
- **`|`**: Combines these to produce the stego image.

---

## Key Operations for Extracting the Image

```python
# Extracting the secret image from the stego image
secret_image = (stego_image & 0x0F) << 4
cv2.imwrite(output_path, secret_image)
```

- **`stego_image & 0x0F`**: Isolates the hidden bits in the stego image.
- **`<< 4`**: Restores these bits to their original position, reconstructing the secret image.

---


## Error Handling and Validation
### Code
```python
if cover_image is None or secret_image is None:
    print("Error: One or both images could not be loaded. Check the paths.")
    return

if cover_image.shape != secret_image.shape:
    secret_image = cv2.resize(secret_image, (cover_image.shape[1], cover_image.shape[0]))
```
- Ensures both images are loaded and resized correctly if dimensions differ.

---

## Results

### Test Case 1: Hiding a Secret Image
**Inputs**:
- Cover Image: `cover_image.png` (grayscale)
- Secret Image: `secret_image.png` (grayscale)
- Output Path: `stego_image.png`

**Output**:
- Stego Image: `stego_image.png` successfully saved.

---

### Test Case 2: Extracting the Hidden Image
**Inputs**:
- Stego Image: `stego_image.png`
- Output Path: `extracted_secret_image.png`

**Output**:
- Extracted Image: `extracted_secret_image.png` successfully saved.

---

### Observations
- The embedding process introduces minimal distortion in the cover image.
- The extracted secret image retains its integrity and is visually accurate.

---

## Usage

### Recreating the Environment
1. Open a terminal and navigate to the project folder.
2. Create a new virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

