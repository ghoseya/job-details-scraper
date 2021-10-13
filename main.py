from PageExtractor import dataExtraction, field_entities
import openpyxl
from os.path import exists
from sys import exit
from time import sleep
from pandas import read_excel
from pickle import load


def main():
    file_name = "Data_Librarian.xlsx"
    with open("job_urls.txt", "rb") as fp:
        primary_gen_link = list(set(load(fp))) # "set" to have unique elements & "list" to have ordered continuous data 
    if exists(file_name):
        read_data = read_excel(file_name)
        read_data_jobs = read_data["jobs_url"].tolist()
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        workbook.save(file_name)
    else:
        read_data_jobs = []
        workbook = openpyxl.Workbook()
        workbook.save(filename=file_name)
        sheet = workbook.active
        temp_list = field_entities() + ["jobs_url"]
        sheet.append(temp_list)
        workbook.save(file_name)


    for jobs in primary_gen_link:
        print(jobs + " - Processing")

        if (jobs in read_data_jobs):
            print("Data Present")
        else:
            params_data = dataExtraction(jobs)
            sheet.append(params_data + [jobs])
            workbook.save(file_name)
            print(jobs + " - Completed")
            sleep(3)

    print("program completed successfully")
    exit()

if __name__ == "__main__":
    while True:
        try:
            main()
        except AttributeError as e:
            sleep(7)
            main()
