from UrlParsing import UrlError
from datetime import datetime, timedelta
from re import search, IGNORECASE


def dataExtraction(url: str) -> list:
    # Parsing
    parsed_obj = UrlError(url)
    parsed_data = parsed_obj.parser()
    # Extracting TITLE
    job_title = parsed_data.find('h1', attrs={'class': 'jobsearch-JobInfoHeader-title'}).text.strip()
    # Key Data in Title
    data_check = search('data', job_title, flags=IGNORECASE)
    if data_check is not None:
        if data_check.group().lower() == 'data':
            key_data = "Yes"
        else:
            key_data = "No"
    else:
        key_data = "No"
    # Extracting INSTITUTION NAME
    institution_name = parsed_data.find('div', attrs={'class': 'jobsearch-InlineCompanyRating'}).find('div').find('a')
    if institution_name is not None:
        institution_name = parsed_data.find('div', attrs={'class': 'jobsearch-InlineCompanyRating'}).find('div').find('a').text.strip()
    else:
        institution_name = parsed_data.find('div', attrs={'class': 'jobsearch-InlineCompanyRating'}).find('div').text.strip()
    # Extracting LOCATION
    job_location = parsed_data.find('div', attrs={'class': 'jobsearch-JobInfoHeader-subtitle'}).find_all('div')
    job_location = job_location[-1].text.strip()
    # Extracting TYPE
    job_type = "Not Mentioned"
    try:
        job_type_div = parsed_data.find('div', attrs={'id': 'jobDetailsSection'}).find_all('div')
        for x in range(len(job_type_div)):
            if job_type_div[x].text == "Job Type":
                job_type = job_type_div[x+1].text.strip()
                break
    except:
        job_type = "Not Mentioned"
    # Extracting SALARY
    try:
        job_salary = parsed_data.find('div', attrs={'id': 'jobDetailsSection'}).find('span')
        if job_salary is not None:
            job_salary = job_salary.text.strip()
        else:
            job_salary = "NaN"
    except:
        job_salary = "NaN"
    # Extracting SUMMARY
    job_summary = parsed_data.find('div', attrs={'id': 'jobDescriptionText'}).text
    # Extracting DAYS
    job_days_div = parsed_data.find('div', attrs={'class': 'jobsearch-JobMetadataFooter'}).find_all('div')
    job_days = datetime.today().strftime('%d-%m-%Y')
    for x in range(len(job_days_div)):
        if ('days' in job_days_div[x].text.split() or 'day' in job_days_div[x].text.split()) and 'ago' in job_days_div[x].text.split():
            job_days = job_days_div[x].text.strip()
            try:
                past_date = int(job_days.split()[0]) - 1
                job_days = datetime.today() - timedelta(past_date)
                job_days = job_days.strftime('%d-%m-%Y')
            except:
                job_days = "30+ days ago"
            break

    return [job_title, institution_name, job_location, job_type, job_salary, job_summary, job_days, key_data]


def field_entities() -> list:
    return ["Job Title", "Institution Name", "Location", "Job Type", "Salary", "Summary", "Posted On", "Key Term Data"]
