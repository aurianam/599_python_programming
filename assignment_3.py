import csv
import math
import statistics as stats

# Open CSV file
with open("fitbit_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    
    # Read headers
    headers = next(reader)
    print("Headers:", headers)  # Check column names

    # Find the index of the "Calories Burned" column
    col_index = headers.index("Calories Burned")

    table = []  # Store processed rows
    calorie_values = []  # Store extracted calorie values

    for row in reader:
        for i in range(len(row)):
            try:
                row[i] = float(row[i])  # Convert values to float
            except ValueError:
                print(f"Couldn't convert '{row[i]}' to float")

        # Extract Calories Burned for averaging
        calorie_values.append(row[col_index])

        # Add row to table
        table.append(row)

    # Calculate the average calories burned
    average_calories_burned = round(stats.mean(calorie_values), 2)

    # Append the average to each row
    for row in table:
        row.append(average_calories_burned)

# Print final table
print("Updated Table:")
for row in table:
    print(row)


# csvfile = open("fitbit_data.csv")
# reader = csv.reader(csvfile)
# headers = next(reader)

# print(headers)  # Prints column names

# table = [] # matrix
# for row in reader:
    
#     for i in range(len(row)):
#         try:
#             float_val = float(row[i])
#             # successfully converted val to float
#             row[i] = float_val
#         except ValueError:
#             print("couldn't convert", row[i], "to float")
#     # row.append(mean)
#     table.append(row)
#     average_calories_burned = stats.mean('Calories Burned')
#     row.append(average_calories_burned)

# print(table)


#     # Extract calorie values for averaging
# calorie_values.append(row[col_index])

# table.append(row)  # Add row to table

#     # Calculate the average calories burned
# average_calories_burned = statistics.mean(calorie_values)  # Correct: using the list of values

#     # Append the average to each row
# for row in table:
#      row.append(average_calories_burned)

# # Print final table
# print("Updated Table:")
# for row in table:
#     print(row)


# def read_table(fitbit_data):
    # filename is a string represents a path to a file we want to open

    # 1. 
#     infile = open(fitbit_data, "r") # "r" is for reading
#     # 2.
#     lines = infile.readlines()
#     print(lines)
#     # we want to cleanup the newlines and restructure lines into a 2D list (table)
#     table = []
#     for line in lines:
#         line = line.strip()
#         values = line.split(",")
#         print(values)
#         table.append(values)
#     # 3.
#     infile.close()
#     return table 


# def convert_to_numeric(table, header, col_name):
#     # figure out what index col_name corresponds to
#     col_index = header.index(col_name)
#     for row in table:
#         try:
#             row[col_index] = float(row[col_index])
#         except ValueError:
#             print("could not convert:", row[col_index])





