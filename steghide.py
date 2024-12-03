import cv2  
import numpy as np 
import os 

# Function to hide a secret image inside a cover image

def hide_image(cover_image_path, secret_image_path, output_path):
    # Check if the output path includes a file name with an extension
    if not os.path.splitext(output_path)[1]:
        print("Error: Output path must include a file name with a valid extension (e.g., .png, .jpg).")
        return 

    # Load the cover and secret images in grayscale (black and white)
    cover_image = cv2.imread(cover_image_path, cv2.IMREAD_GRAYSCALE)
    secret_image = cv2.imread(secret_image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the images were successfully loaded
    if cover_image is None or secret_image is None:
        print("Error: One or both images could not be loaded. Check the paths.")
        return 

    # Resize the secret image to match the size of the cover image
    if cover_image.shape != secret_image.shape:
        print("Resizing images to match dimensions...")
        # Resize the secret image to the same width and height as the cover image
        secret_image = cv2.resize(
            secret_image, (cover_image.shape[1], cover_image.shape[0]))

    # Embed the secret image into the cover image
    # - The cover image is masked to keep the upper 4 bits (using & 0xF0)
    # - The secret image is shifted to take the lower 4 bits (using >> 4)
    stego_image = (cover_image & 0xF0) | (secret_image >> 4)

    # Save the combined image (stego image) to the specified output path
    cv2.imwrite(output_path, stego_image)
    print(f"Stego image saved as {output_path}")

# Function to extract the hidden secret image from the stego image


def extract_image(stego_image_path, output_path):
    # Load the stego image in grayscale
    stego_image = cv2.imread(stego_image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the stego image was successfully loaded
    if stego_image is None:
        print("Error: The stego image could not be loaded. Check the path.")
        return 

    # Extract the hidden secret image
    # - Extract the lower 4 bits of the stego image (using & 0x0F)
    # - Shift those bits back to their original position (using << 4)
    secret_image = (stego_image & 0x0F) << 4

    # Save the extracted secret image to the specified output path
    cv2.imwrite(output_path, secret_image)
    print(f"Extracted secret image saved as {output_path}")

# Main function to provide the menu and handle user choices

def main():
    while True:  # Loop until the user decides to exit
        print("\nOptions:")
        print("1. Hide an Image") 
        print("2. Extract an Image")
        print("3. Exit") 

        # Ask the user for their choice
        choice = input("Enter your choice: ")

        # If the user wants to hide an image
        if choice == "1":
            # Get the file paths for the cover image, secret image, and output stego image
            cover_image_path = input("Enter the path of the cover image: ")
            secret_image_path = input("Enter the path of the secret image: ")
            output_path = input("Enter the output path for the stego image: ")

            # Check if the cover and secret image paths are valid
            if not os.path.exists(cover_image_path) or not os.path.exists(secret_image_path):
                print("Error: One or both of the image paths are invalid.")
                continue  # Go back to the menu if the paths are invalid

            # Call the function to hide the secret image
            hide_image(cover_image_path, secret_image_path, output_path)

        # If the user wants to extract a hidden image
        elif choice == "2":
            # Get the file paths for the stego image and the output secret image
            stego_image_path = input("Enter the path of the stego image: ")
            output_path = input(
                "Enter the output path for the extracted secret image: ")

            # Check if the stego image path is valid
            if not os.path.exists(stego_image_path):
                print("Error: The stego image path is invalid.")
                continue  # Go back to the menu if the path is invalid

            # Call the function to extract the hidden secret image
            extract_image(stego_image_path, output_path)

        # If the user wants to exit
        elif choice == "3":
            print("Exiting...")  # Print a message and exit the program
            break  # Exit the loop

        # If the user enters an invalid option
        else:
            # Ask for a valid option
            print("Invalid choice. Please try again.")


# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main() 
