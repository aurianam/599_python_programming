import pandas

#insert file name below
data = x

#is this ^ the best way to do this? so that each user can easily add their file?

# Load 
dataframe = pandas.read_csv(data)

#correct column formatting
numeric_columns = dataframe.select_dtypes(include='number')

#make new list 
statistics = []

# Loop 
for column in numeric_columns.columns:
    series = numeric_columns.loc[numeric_columns[column].notna(), column]
    # i am still working on understanding when to use loc so if this is a mess let me know :)
    statistics.append({
        'Column': column,
        'Mean': round(series.mean(), 3),
        'StdDev': round(series.std(ddof=1), 3),
        'Median': round(series.median(), 3),
        'Min': round(series.min(), 3),
        'Max': round(series.max(), 3)})

# Create a new df that includes the stats
stats_dataframe = pandas.DataFrame(statistics)

# Save to CSV
stats_dataframe.to_csv("stats_output.csv", index=False)

print("Statistics written to stats_output.csv" )

#question: if i wanted to print the file path- how would i do that?
#i know how to print it on my computer but if someone else ran it i want it to print theirs
