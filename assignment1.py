# The information on available cars can be found in a sqlite database (in 'tutorial.db')
# Your goal is to find the 100 most profitable cars

# Income:
# - sale price

# Expenses
# - Transport (where each day costs an amount that varies by country)
# - Tax (this varies by country)


# TWISTS:
# The 'tax' column in the 'countries' table is not fully correct. The person who added it, did not include the base
# value of $300 in every tax amount, as that is the EU minimum. It is your job to add this.


# How to achieve the goal?
# - 3 ways
# First, use only SQL to find the answer. You may modify the database if necessary. You're free to use the
# documentation: https://docs.python.org/3/library/sqlite3.html as well as other online tools.
# For your convenience, a "profitable_cars" table has already been created.

# Second, load the data.xlsx using Polars and use only Polars to find the answer. Your answer should be a Polars
# dataframe only containing the 100 most profitable cars.

# Third, use the data as it is provided by the data_python.py as two arrays with tuples and find the 100 most
# profitable cars using only Python code and no external libraries.
