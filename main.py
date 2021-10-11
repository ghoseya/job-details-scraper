import sys
from PageExtractor import dataExtraction,field_entities
import openpyxl
import os.path
import time
import pandas as pd
import pickle


def main():
    file_name = "Data_Librarian.xlsx"
    with open("job_urls.txt", "rb") as fp:
        primary_gen_link = pickle.load(fp)
    if os.path.exists(file_name):
        read_data = pd.read_excel(file_name)
        read_data_jobs = read_data["jobs_url"].tolist()
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
    else:
        read_data_jobs = []
        workbook = openpyxl.Workbook()
        workbook.save(filename=file_name)
        sheet = workbook.active
        temp_list = field_entities() + ["jobs_url"]
        sheet.append(temp_list)
        workbook.save(file_name)
    pd.read_excel(file_name)
    for jobs in primary_gen_link:
        print(jobs)
        if len(primary_gen_link)==len(read_data_jobs):
            sys.exit()
        if (jobs in read_data_jobs):
            print("Data Present")
        else:
            params_data = dataExtraction(jobs)
            sheet.append(params_data + [jobs])
            workbook.save(file_name)
            time.sleep(3)
        workbook.save(file_name)


if __name__ == "__main__":
    main()