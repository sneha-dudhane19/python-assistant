
def get_file_extension(file_name):
    """
    Function to get the file extension from a given filename.
    
    Parameters:
    file_name (str): The name of the file.
    
    Returns:
    str: The file extension.
    """
    return file_name.split(".")[-1]

print("Get file extension:", get_file_extension("example.txt"))  # Example usage of the function

def build_table_name(source, entity):
    """
    Function to build a table name based on the source and entity.
    
    Parameters:
    source (str): The source of the data.
    entity (str): The entity name.
    
    Returns:
    str: The constructed table name.
    """
    return f"{source.lower()}_{entity.lower()}".replace(" ", "_")

print("Constructed table name:", build_table_name("HR Data", "Employee"))  # Example usage of the function

def is_csv_file(file_name):
    """
    Function to check if a given filename has a .csv extension.
    
    Parameters:
    file_name (str): The name of the file.
    
    Returns:
    bool: True if the file is a CSV file, False otherwise.
    """
    return file_name.lower().endswith(".csv")

print("Example.csv -> Is CSV file:", is_csv_file("example.csv"))  # Example usage of the function
print("Example.txt -> Is CSV file:", is_csv_file("example.txt"))  # Example usage of the function

def validate_file_name(file_name):
    """
    Function to validate if the given filename is valid (not empty and has an extension).
    
    Parameters:
    file_name (str): The name of the file.
    
    Returns:
    bool: True if the filename is valid, False otherwise.
    """
    if file_name and "." in file_name:
        return True
    return False

"""
print("Validating 'data.csv':", validate_file_name("data.csv"))  # Example usage of the function
print("Validating 'data':", validate_file_name("data"))  # Example usage of the function
print("Validating '':", validate_file_name(""))  # Example usage of the function
"""