# import required modules 
from pathlib import Path 
import csv 
 
# setup filepaths for reading overheads: 
file_path = 'overheads-day-90.csv'  
fp_read3 = Path.cwd() / "csv_reports" / file_path 
 
## actual body to read and print rows from csv file: 
## mode = "r" => denotes read mode 
## mode = "w" => denotes write (and overwrite) mode 
 
def overhead():
    """ 
    This function analyzes the percentages of expenses
    of all the overheads from a CSV file, and then
    prints a message indicating the name of the overhead
    with the highest percentage, as well as the percentage
    itself. 
    Parameters: 
    None
    """ 
    # initialize variables to store the highest category and percentage 
    highest_category = "" 
    highest_percentage = 0.0

    with fp_read3.open(mode="r", encoding="UTF8", newline="") as file:   
        reader = csv.reader(file)   
        next(reader)  # to skip reading header  
        for row in reader:  # iterate each row with loop 
            category = row[0]  # since 'Category' is the first column 
            percentage = float(row[1])  # since 'Overheads' is the second column 
             
            # if current row has a higher percentage, update highest values 
            if percentage > highest_percentage: 
                highest_category = category 
                highest_percentage = percentage 
    
    summary_report_path = Path.cwd() / "summary_report.txt"
    with summary_report_path.open(mode="a", encoding="UTF8") as output:
        output.write(f"[HIGHEST OVERHEAD] {highest_category} : {highest_percentage:.2f}%\n")
        # return the result as a formatted string directly 
        return f"[HIGHEST OVERHEAD] {highest_category} : {highest_percentage:.2f}%"