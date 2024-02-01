# import required modules  
from pathlib import Path  
import csv  
  
# setup filepaths for reading cash on hand:  
fp_read = Path.cwd() / "csv_reports" / "cash-on-hand-sgd.csv"   
  
# create list  
coh_list = []    
  
## actual body to read and print rows from csv file:  
## mode = "r" => denotes read mode  
## mode = "w" => denotes write (and overwrite) mode  
   
def coh():  
    """  
    This function calculates the difference of  
    cash of hand column from a CSV file, then analyses the trend,  
    printing messages indicating whether there is a surplus,  
    a deficit, or specific days with cash deficit.  
    Parameters:  
    None  
    """  
    # open csv file to read   
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:    
        reader = csv.reader(file)  # create csv reader object using csv  
        next(reader)  # to skip reading header  
        for row in reader:  # iterate each row with loop  
            coh_list.append(float(row[1]))   
  
    # calculate the differences for each day   
    differencescoh = [coh_list[coh + 1] - coh_list[coh] for coh in range(len(coh_list) - 1)]    
  
    # analyze the overall trend (diff in coh)  
    all_increasing = sum(1 for diffc in differencescoh if diffc > 0)  
    all_decreasing = sum(1 for diffc in differencescoh if diffc < 0)  
 
    cash_deficits = [] 
     
    summary_report_path = Path.cwd() / "summary_report.txt"
    with summary_report_path.open(mode="a", encoding="UTF8") as output:
        if all_increasing == len(differencescoh):
            output.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            output.write(f"[HIGHEST CASH SURPLUS] DAY: {len(coh_list)}, AMOUNT: SGD {coh_list[-1]:.2f}\n")
        elif all_decreasing == len(differencescoh):
            output.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
            output.write(f"[HIGHEST CASH DEFICIT] DAY: {len(coh_list)}, AMOUNT: SGD {coh_list[-1]:.2f}\n")
        else:
            for day, diffc in enumerate(differencescoh, start=12):
                if diffc < 0:  
                    deficitc_amount = abs(diffc)  
                    output.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {deficitc_amount:.2f}\n")  
                    cash_deficits.append((diffc, day)) 
 
            # print 3 top highest cash deficits only if there are at least 3 deficits 
            cash_deficits.sort()  # sort in descending order 
            output.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_deficits[0][1]}, AMOUNT: SGD {abs(cash_deficits[0][0]):.2f}\n") 
            output.write(f"[2ND HIGHEST CASH DEFICIT] DAY: {cash_deficits[1][1]}, AMOUNT: SGD {abs(cash_deficits[1][0]):.2f}\n") 
            output.write(f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_deficits[2][1]}, AMOUNT: SGD {abs(cash_deficits[2][0]):.2f}\n") 
  
    return differencescoh