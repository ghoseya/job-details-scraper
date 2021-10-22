# To merge all xlxs files into a single file
from pandas import DataFrame, read_excel, concat
from os import listdir

data_files = []
my_df = DataFrame()
extensions = (".xlsx")

# os.listdir() returns a list of names of all files and folders inside the current directory
for path in listdir("datasets"):
    if path.endswith(extensions):
        data_files.append(path)

for sheets in data_files:
    temp_sheet_read = read_excel("datasets/"+sheets)
    my_df = concat([my_df,temp_sheet_read])

my_df.drop_duplicates(subset ="jobs_url", inplace=True)
my_df.to_excel("MergedData.xlsx")
summary = my_df["Summary"]
summary.to_excel("summary.xlsx")
