# Import Modules
import os
import csv

# Path to collect data from the Resources folder
psybank_csv = os.path.join("Resources", "budget_data.csv")
file_path = "Analysis/analysis.txt"
files_path = "Resources/budget_data.csv"

# Set values and lists
net_total = 0
close = 0
large_inc = []
large_dec = []
prices = []

# Function to find largest increase
def find_inc(lst):
    # Create values
    max_increase = 0
    months_num = 0
    # Loop through list
    for i in range(1, len(lst)):
        # Set increase to be the change from i-1 to i
        increase = int(lst[i])-int(lst[i-1])
        # Check to see if increase is greater than max increase
        if increase > max_increase:
            # If so, max_increase becomes increase and the value for the month it happens in is set as i
            max_increase = increase
            months_num = i
    # Return the max increase and the number cooresponding with the month it happens in
    return [months_num, max_increase]
    

# Function to find largest decrease
def find_dec(lst):
    # Create values
    max_decrease = 0
    month_num = 0
    # Loop through list
    for i in range(1, len(lst)):
        # Set decrease to be the difference between i-1 and i
        decrease = int(lst[i]) - int(lst[i-1])
        # Check to see if decrease is greater than max decrease
        if decrease < max_decrease:
            # If so, max decrease becomes decrease and set month to be the i
            max_decrease = decrease
            month_num = i
    # Return max decrease and number of month it happens in
    return [month_num, max_decrease]

# Function I found online to let me find the value in the csv file that matches the month of the greatest increase and decrease without having to change my functions
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


# Read in CSV file
with open(psybank_csv) as csvfile:
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
# Get header
    csv_header = next(csvreader)
# Loop through the data in the csv file
    for rows in csvreader:
        # Increase net total and add profits/losses to prices list
        net_total += int(rows[1])
        prices.append(rows[1])
    # Set values to equal the correct numbers
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
    # Get month of largest increase or decrease using function
    inc_month = retrieve_csv_element(files_path, (inc_month_num+1), column_index)
    dec_month = retrieve_csv_element(files_path, (dec_month_num+1), column_index)
    # Make change have only 2 numbers after the decimal
    change = round(((int(close) - int(open_price))/(int(months)-1)), 2)

# Create and write text file in analysis folder
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

# Print same info from text file in terminal
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
print("Greatest Decrease in Profits: " + dec_month + " ($" + str(large_dec_val) + ")")