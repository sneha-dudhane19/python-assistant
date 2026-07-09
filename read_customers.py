import pandas as pd

try:
    customer_df = pd.read_csv('customers.csv')

except FileNotFoundError:
    print("Error: customers.csv file not found.")

else:
    print("\n=============================================")
    print("\nCustomer dataframe row count :", len(customer_df.index))
    print("\nCustomer DataFrame Column names:\n", customer_df.columns.to_list())
    print("\nPrinting first 3 rows:\n", customer_df.head(3))
    print("\n=============================================")

    row_count = len(customer_df.index)
    if row_count == 0:
        print("\nCustomer dataframe is empty")
    else:
        print("\nCustomer dataframe is not empty")

    col_list = customer_df.columns.to_list()
    expected_cols = {"customer_id", "name", "state"}
    if expected_cols.issubset(set(col_list)):
        print("\nCustomer dataframe has all expected columns")
    else:
        print("\nCustomer dataframe does not have expected columns")



    