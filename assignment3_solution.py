import csv
import math


def load_data_into_table(filename):
   with open(filename) as csvfile:
       reader = csv.reader(csvfile, delimiter=",")
       table = []
       for row in reader:
           new_row = []
           for val in row:
               try:
                   val = float(val)
                   new_row.append(val)
               except ValueError:
                   # couldn't convert to float, must be date or name or similar
                   new_row.append(val)
           table.append(new_row)
   return table

def get_column(table, header, col_name):
   col_index = header.index(col_name)
   col = [row[col_index] for row in table]
   return col

def compute_mean(data):
    return sum(data) / len(data)

def compute_std(data):
    n = len(data)
    mean = compute_mean(data)
    devs = []
    for val in data:
        devs.append((val - mean) ** 2)
    stdev = math.sqrt(sum(devs) / n)
    return stdev

def compute_median(data):
    n = len(data)
    data = sorted(data) # or inplace data.sort()
    return data[n // 2]

def compute_stats(col):
   mean = compute_mean(col)
   stdev = compute_std(col)
   median = compute_median(col)
   min_val = min(col)
   max_val = max(col)
   return [mean, stdev, median, min_val, max_val]

def write_stats_to_file(filename, stats_col_names, stats_rows):
   with open(filename, "w") as outfile:
       writer = csv.writer(outfile)
       writer.writerow(["column", "mean", "stdev", "median", "min", "max"])
       for i, col_name in enumerate(stats_col_names):
           writer.writerow([col_name] + stats_rows[i])

def process_numeric_cols(table, header):
   stats_col_names = []
   stats_rows = []
   for i in range(len(header)):
       if isinstance(table[0][i], float):
           col = get_column(table, header, header[i])
           stats = compute_stats(col)
           stats_col_names.append(header[i])
           stats_rows.append(stats)
   return stats_col_names, stats_rows

def main():
   table = load_data_into_table('fitbit_data_3-8_9-16.csv')
   header = table.pop(0)
   print(header)
   print(table[:5])
   stats_col_names, stats_rows = process_numeric_cols(table, header)
   write_stats_to_file("stats.csv", stats_col_names, stats_rows)

if __name__ == "__main__":
   main()