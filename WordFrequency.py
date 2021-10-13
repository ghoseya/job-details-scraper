from nltk.corpus import stopwords
import re
import openpyxl
import pandas


xl_file = pandas.read_excel("Data_Curation_Research.xlsx")
summary = xl_file["job_summary"]
print(summary)
summary = " ".join(summary)


en_stops = set(stopwords.words('english'))
summary = summary.lower()
summary = re.sub(r'[^\w\s]', '', summary)
summary = summary.split()
final = []
all_words = summary
for word in all_words:
    if word not in en_stops:
        final.append(word)

def freq(str):
    workbook = openpyxl.Workbook()
    workbook.save(filename="wordcount.xlsx")
    sheet = workbook.active
    sheet['A1'].value = "words"
    sheet['B1'].value = "count"
    sheet['C1'].value = "pre-word"
    sheet['D1'].value = "post-word"
    str2 = []
    for i in str:
        if i not in str2:
            str2.append(i)
    for i in range(0, len(str2)):
        if(i==0):
            print('Frequency of', str2[i], 'is :', str.count(str2[i]))
            sheet.append([str2[i], str.count(str2[i]), str2[i],str2[i]+" "+str2[i + 1]])
        if(i==len(str2)):
            print('Frequency of', str2[i], 'is :', str.count(str2[i]))
            sheet.append([str2[i], str.count(str2[i]), str2[i-1]+" "+str2[i], str2[i]])
        else:
            print('Frequency of', str2[i], 'is :', str.count(str2[i]))
            sheet.append([str2[i],str.count(str2[i]),str2[i-1]+" "+str[i],str[i]+" "+str[i+1]])
    workbook.save('wordcount.xlsx')

freq(final)