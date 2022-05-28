"""
Read FTIR peaks from xlsx file and write to new txt file.
"""

import pandas as pd

# path to the data Excel file
path = "peaks.xlsx"

# loading data from Excel file
raw_data = pd.read_excel(path)

# remove empty and unneccesery columns: .filter()
# remove 1st row: .drop(label)
# remove NaN values: .dropna()
data = raw_data.filter(regex="^TM_").drop(0)

# gathering compounds names
names = data.columns


with open("FTIR_data.txt", "w") as file:
    for name in names:
        line = name + ": "
        for peak in data[name]:
            try:
                line += str(round(peak)) + ", "
            except:
                print(line)
                print("Brak kolejnych wartości innych niż NaN")
                break
        # format final line by removing comma and adding new empty line
        fin_line = line[:-2] + ".\n\n"
        # write final line to txt file
        file.write(fin_line)
