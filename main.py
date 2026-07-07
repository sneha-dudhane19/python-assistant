from utils import validate_file_name

def main():
    """
    Main function to demonstrate the usage of the validate_file_name function.
    """
    test_files = ["data.csv", "dataset.CSV", "data", ""]
    
    for file in test_files:
        is_valid = validate_file_name(file)
        print(f"Validating '{file}': {is_valid}")

if __name__ == "__main__":
    main()