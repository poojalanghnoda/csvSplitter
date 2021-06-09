
import pandas as pd
import sys
import os

#csv file name to be read in 
in_csv =sys.argv[1]

output_filename = os.path.basename(in_csv)
#get the number of lines of the csv file to be read
number_lines = sum(1 for row in (open(in_csv)))

#size of rows of data to write to the csv, 
rowsize = int(sys.argv[2])

headers = list(pd.read_csv(in_csv))
count = 1
#start looping through data writing it to a new file for each set
for i in range(1,number_lines,rowsize):
    df = pd.read_csv(in_csv,
          nrows = rowsize,#number of rows to read at each loop
          skiprows = i,
            )#skip rows that have been read
    #csv to write data to a new file with indexed name. input_1.csv etc.
    out_csv = str(output_filename)[:-4] + str(count) + '.csv'
    count+=1
    df.to_csv(out_csv,
          index=False,
          header=headers,
          mode='a',#append data to csv file
          chunksize=rowsize)#size of data to append for each loop

print("Congo, CSV files are splited")
