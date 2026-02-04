def rot47(text):
    """
    Encodes or decodes a string using ROT47.
    """
    result = []
    for char in text:
        # Check if character is within the visible ASCII range (33-126)
        if 33 <= ord(char) <= 126:
            # Apply the ROT47 shift
            result.append(chr(33 + ((ord(char) - 33 + 47) % 94)))
        else:
            # Keep character unchanged if it's outside the range (e.g., space)
            result.append(char)
            
    return "".join(result)

# --- Example Usage ---
if __name__ == "__main__":
    original_text = "Hello World!"
    encoded_text = rot47(original_text)
    decoded_text = rot47(encoded_text)

    print(f"Original: {original_text}")
    print(f"Encoded:  {encoded_text}")
    print(f"Decoded:  {decoded_text}")