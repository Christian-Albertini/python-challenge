import os
import csv


psybank_csv = os.path.join("Resources", "budget_data.csv")
file_path = "Analysis/analysis.txt"
files_path = "Resources/budget_data.csv"


net_total = 0
close = 0
large_inc = []
large_dec = []
prices = []

def find_inc(lst):
    max_increase = 0
    months_num = 0
    for i in range(1, len(lst)):
        increase = int(lst[i])-int(lst[i-1])
        if increase > max_increase:
            max_increase = increase
            months_num = i
    return [months_num, max_increase]
    


def find_dec(lst):
    max_decrease = 0
    month_num = 0
    for i in range(1, len(lst)):
        decrease = int(lst[i-1]) - int(lst[i])
        if decrease > max_decrease:
            max_decrease = decrease
            month_num = i
    return [month_num, max_decrease]

def retrieve_csv_element(csv_file_path, row_index, column_index):
    try:
        # Read the CSV file
        with open(csv_file_path, 'r') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            # Iterate through the rows
            for current_row_index, row in enumerate(csv_reader):
                # Check if the current row matches the desired row index
                if current_row_index == row_index:
                    # Check if the current row has enough columns
                    if column_index < len(row):
                        # Retrieve the specific element and return it
                        return row[column_index]
                    else:
                        raise ValueError(
                            f"Column index {column_index} is out of range for row {row_index}")
            # If the desired row index is not found
            raise ValueError(
                f"Row index {row_index} not found in the CSV file")
    except Exception as e:
        print(f"An error occurred: {e}")



with open(psybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for rows in csvreader:
        net_total += int(rows[1])
        prices.append(rows[1])

    open_price = prices[0]
    close = prices[-1]
    months = len(prices)
    large_inc = find_inc(prices)
    large_inc_val = large_inc[1]
    inc_month_num = large_inc[0]
    large_dec = find_dec(prices)
    large_dec_val = large_dec[1]
    dec_month_num = large_dec[0]
    column_index = 0

    inc_month = retrieve_csv_element(files_path, (inc_month_num+1), column_index)
    dec_month = retrieve_csv_element(files_path, (dec_month_num+1), column_index)

    change = round(((int(close) - int(open_price))/(int(months)-1)), 2)


with open(file_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("\n")
    file.write("--------------------------------------------------\n")
    file.write("\n")
    file.write("Total Months: " + str(months) +"\n")
    file.write("\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("\n")
    file.write("Average Change: $" + str(change) + "\n")
    file.write("\n")
    file.write("Greatest Increase in Profits: " + inc_month + " ($" + str(large_inc_val) + ")\n")
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + dec_month + " ($-" + str(large_dec_val) + ")\n")

print("Financial Analysis")
print("")
print("--------------------------------------------------")
print("")
print("Total Months: " + str(months))
print("")
print("Total: $" + str(net_total))
print("")
print("Average Change: $" + str(change))
print("")
print("Greatest Increase in Profits: " + inc_month + " ($" + str(large_inc_val) + ")")
print("")
print("Greatest Decrease in Profits: " + dec_month + " ($-" + str(large_dec_val) + ")")