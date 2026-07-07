
source_system = "Postgres Database"
file_name = "dataset.csv"
file_date = "2026-07-05"
row_count = 3456
load_status = "Completed"

print("\n--------------------------- File Inventory Details ---------------------------\n")
print("Source System name :", source_system)
print("File name :", file_name)
print("File date :", file_date)
print("Row count :", row_count)
print("Load status :", load_status)
print("\n-------------------------------------------------------------------------------")


# Working with a list of filenames and checking for CSV files

filenames = ["techstack.CSV", "data.txt", "logs.json", "config.yaml", "dataset.csv", "error_log.txt", "summary.csv", "emp_data.csv"]

for file in filenames:
    if file.lower().endswith(".csv"):
        print(f"{file} is a CSV File")
    else:
        print(f"{file} is not a CSV File")


# Dictionary

dataset = {
    "source": "HR Data",
    "target_table": "employee_data",
    "expected_columns": "[id, name, department, salary]",
    "owner": "Human Resources Team" 
}

print("\n--------------------------- Dataset Details ---------------------------\n")
print("Source : ", dataset["source"])
print("target table : ", dataset["target_table"])
print("Expected columns : ", dataset["expected_columns"])
print("Owner : ", dataset["owner"])
print("\n-------------------------------------------------------------------------------")

