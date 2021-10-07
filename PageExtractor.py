from UrlParsing import UrlError


def dataExtraction(url: str):
    # Parsing
    parsed_obj = UrlError(url)
    parsed_data = parsed_obj.parser()
    # Extracting TITLE
    job_title = parsed_data.find(
        'h1', attrs={'class': 'jobsearch-JobInfoHeader-title'}).text.strip()
    # Extracting INSTITUTION NAME
    institution_name = parsed_data.find('div', attrs={
                                        'class': 'jobsearch-InlineCompanyRating'}).find('div').find('a').text.strip()
    # Extracting LOCATION
    job_location = parsed_data.find(
        'div', attrs={'class': 'jobsearch-JobInfoHeader-subtitle'}).find_all('div')
    job_location = job_location[-1].text.strip()
    # Extracting TYPE
    try:
        job_type_div = parsed_data.find(
            'div', attrs={'id': 'jobDetailsSection'}).find_all('div')
        for x in range(len(job_type_div)):
            if job_type_div[x].text == "Job Type":
                job_type = job_type_div[x+1].text.strip()
                break
    except:
        job_type = "Not Mentioned"
    # Extracting SALARY
    try:
        job_salary = parsed_data.find(
            'div', attrs={'id': 'jobDetailsSection'}).find('span')
        if job_salary != None:
            job_salary = job_salary.text.strip()
        else:
            job_salary = "NaN"
    except:
        job_salary = "NaN"
    # Extracting SUMMARY
    job_summary = parsed_data.find(
        'div', attrs={'id': 'jobDescriptionText'}).text
    # Extracting DAYS
    job_days = parsed_data.find(
        'div', attrs={'class': 'jobsearch-JobMetadataFooter'}).find_all('div')
    job_days = job_days[1].text.strip()

    return job_title, institution_name, job_location, job_type, job_salary, job_summary, job_days
