# Consecutive folder generator
# Create consecutive folders with the same name
# Asks for the destination path, folder name, and the number of consecutive folders
# Checks if the folder exists before starting from the last number
import os

def create_consecutive_folders():
    destination_path = input("Enter the destination path: ")
    
    # Check if the destination path exists
    if not os.path.isdir(destination_path):
        return
    folder_name = input("Enter the folder name: ")
    num_folders = int(input("Enter the number of consecutive folders: "))
    
    # Initialize the folder number to start from 1
    folder_number = 1

    # Check if the folder already exists and find the last existing folder number
    while os.path.exists(os.path.join(destination_path, f"{folder_name}{folder_number}")):
        folder_number += 1

    # Create consecutive folders
    for i in range(num_folders):
        folder_path = os.path.join(destination_path, f"{folder_name}{folder_number}")
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
        folder_number += 1



if __name__ == "__main__":
    create_consecutive_folders()
