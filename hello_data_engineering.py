print("Hello, Data Engineering!")       # Simple print statement to greet the user

msg = "Welcome to the Data Engineering world!"  # Assigning a welcome message to the variable 'msg'
print(msg)

msg = 10
print("Changing variable value to integer", msg)

print(101)  # Printing number
print("This is Python", 101)    # Printing a string and a number together

x, y, z = 10, "Hi", 3.5
print("Multiple variable assignment - ", x, y, z)  # Printing multiple variables assigned in a single line

# Example of a list in Python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # List of months
print(f"Months of the year - {months}")  # Printing the list of months using an f-string for formatting
print("Accessing list elements using loop:")
for val in months:
    print(val)  # Looping through the list of months and printing each month


#Example of a dictionary in Python
user = {
    "name": "Sneha",
    "role": "Senior Data Engineer",
    "team": "Data Operations"
}
print ("User Details - ", user)  # Printing the entire user dictionary
print ("User name - ", user["name"]) # Accessing and printing the 'name' value from the user dictionary


#Python Comments
# This is a single line comment
"""
This is a multi-line comment
that can span multiple lines"""