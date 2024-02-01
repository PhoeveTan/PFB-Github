# import required modules  
from pathlib import Path  
import csv  
  
# setup filepaths for reading profit and loss:  
fp_read = Path.cwd() / "csv_reports" / "profit-and-loss-sgd.csv"    
  
## actual body to read and print rows from csv file:  
## mode = "r" => denotes read mode  
## mode = "w" => denotes write (and overwrite) mode  
  
# create list  
pnl_list = []    
  
def pnl():  
    """  
    This function calculates the difference in the  
    net profit column from a CSV file, then analyses the trend,  
    printing messages indicating whether there is a surplus,  
    a deficit, or specific days with net profit deficits.  
    Parameters:  
    None  
    """  
    # open csv file to read   
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:    
        reader = csv.reader(file)   # create csv reader object using csv  
        next(reader)  # to skip reading header  
        for row in reader:  # iterate each row with loop  
            pnl_list.append(float(row[4]))    
  
    # calculate the differences for each day   
    differencespnl = [pnl_list[pnl + 1] - pnl_list[pnl] for pnl in range(len(pnl_list) - 1)]    
  
    # analyze the overall trend (diff in pnl)  
    all_increasing = sum(1 for diffp in differencespnl if diffp > 0)  
    all_decreasing = sum(1 for diffp in differencespnl if diffp < 0)  
 
    pnl_deficits = [] 

    summary_report_path = Path.cwd() / "summary_report.txt"
    with summary_report_path.open(mode="a", encoding="UTF8") as output:
        if all_increasing == len(differencespnl):  
            output.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")  
            output.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {len(pnl_list)}, AMOUNT: SGD {pnl_list[-1]:.2f}\n") 
        elif all_decreasing == len(differencespnl):  
            output.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")  
            output.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {len(pnl_list)}, AMOUNT: SGD {pnl_list[-1]:.2f}\n") 
        else:  
            for day, diffp in enumerate(differencespnl, start=12):  
                if diffp < 0:  
                    deficitp_amount = abs(diffp)  
                    output.write(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {deficitp_amount:.2f}\n")  
                    pnl_deficits.append((diffp, day)) 

            # print 3 top highest cash deficits and list out in descending order 
            pnl_deficits.sort() # sort in descending order 
            output.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {pnl_deficits[0][1]}, AMOUNT: SGD{abs(pnl_deficits[0][0])}\n") 
            output.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {pnl_deficits[1][1]}, AMOUNT: SGD{abs(pnl_deficits[1][0])}\n") 
            output.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {pnl_deficits[2][1]}, AMOUNT: SGD{abs(pnl_deficits[2][0])}\n") 
  
  
    return differencespnl 