from PageExtractor import dataExtraction
import openpyxl
import os.path
import time
import sys
import pandas as pd
import pickle


def main():
    file_name = input("Enter filename: ")
    with open("job_urls.txt", "rb") as fp:
        primary_gen_link = pickle.load(fp)
    if os.path.exists(file_name):
        read_data = pd.read_excel(file_name)
        read_data_jobs = read_data["url"].tolist()
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active

    else:
        read_data_jobs = []
        workbook = openpyxl.Workbook()
        workbook.save(filename=file_name)
        sheet = workbook.active
        sheet['A1'].value = "job_title"
        sheet['B1'].value = "institution_name"
        sheet['C1'].value = "job_location"
        sheet['D1'].value = "job_type"
        sheet['E1'].value = "job_salary"
        sheet['F1'].value = "job_summary"
        sheet['G1'].value = "job_days"
        sheet['H1'].value = "url"
        workbook.save(file_name)
    pd.read_excel(file_name)
    for jobs in primary_gen_link:
        print(jobs)
        if len(primary_gen_link) == len(read_data_jobs):
            sys.exit()
        if (jobs in read_data_jobs):
            print("Data Present")

        else:
            params_data = dataExtraction(jobs)
            sheet.append(params_data + [jobs])
            workbook.save('Data_Management_Librarian.xlsx')
            time.sleep(2)
    workbook.save('Data_Management_Librarian.xlsx')


if __name__ == "__main__":
    main()
