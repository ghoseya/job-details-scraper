from re import sub
from UrlParsing import UrlParseBs
from urllib.parse import urlencode
import pickle


def generateLink():

    # generating our own link for a specific job (first page)
    l1 = "https://www.indeed.com/jobs?"
    job, location = input("job Name: "), input('Job Location(optional): ')
    query = {'q':job,'l':location}
    link_list = []
    jobs_list = []
    start_link = l1 + urlencode(query)
    link_list.append(start_link)

    # creating a object to parse the link
    obj1 = UrlParseBs(start_link)
    read = obj1.parser()
    count = read.find("div", attrs={"id": "searchCountPages"}).text.strip()

    # taking only the number of jobs
    count = sub("Page 1 of ", "", count)
    count = sub(" jobs", "", count)
    count = sub(",", "", count)
    count = int(count)
    page_count = (count // 15) + 1

    # Generating link for all the pages
    for i in range(1, page_count):
        link = start_link + "&start=" + str(i) + "0"
        link_list.append(link)

    # Generating link for every jobs
    n = 1
    for j in link_list:
        page_obj = UrlParseBs(j)
        page_url_data = page_obj.parser()
        print("Page " + str(n) + " scraped")
        n = n + 1

        for tag in page_url_data.find_all(class_="tapItem"):
            job_id = tag.get('id')
            job_id = sub("job_", "", job_id)
            specific_job = "https://www.indeed.com/viewjob?jk="
            specific_job = specific_job + job_id
            jobs_list.append(specific_job)

    with open("job_urls.txt","wb") as fp:
        pickle.dump(jobs_list,fp)  #Save links in a pickle file

generateLink()
