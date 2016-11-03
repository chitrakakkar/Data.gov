import requests


class digital_job:
    def __init__(self):
        pass

    @staticmethod
    def all_job():
        url = 'https://api.usa.gov/jobs/search.json?query=jobs'
        # url = 'https://api.usa.gov/jobs/search.json?query=nursing+jobs+in+mn'
        # url = 'https://api.usa.gov/jobs/search.json?query=jobs+at+the+mn&organization_ids=AF'
        response = requests.get(url)
        # it slices the objects up from the big list of json objects
        result = parse_data(response.json())
        return result

    @staticmethod
    def location_based_jobs(parameter):
        url = 'https://api.usa.gov/jobs/search.json?query=jobs+in+'+str(parameter)
        response = requests.get(url)
        result = parse_data(response.json())
        return result

    @staticmethod
    def partTime_jobs(keyword):
        url = 'https://api.usa.gov/jobs/search.json?query=parttime'+str(keyword)
        response = requests.get(url)
        print(response.text)
        result = parse_data(response.json())
        return result

    @staticmethod
    def jobs_with_combination():
        url = 'https://api.usa.gov/jobs/search.json?query= parttime+nursing+jobs+with+veterans+affairs+in+ny'
        response = requests.get(url)
        print(response.text)
        result = parse_data(response.json())
        return result

    @staticmethod
    def specific_jobs(keyword):
        url = 'https://api.usa.gov/jobs/search.json?query=+'+str(keyword)+'jobs'
        response = requests.get(url)
        result = parse_data(response.json())
        return result


def parse_data(response_text):
    job_data_item = []
    for data in response_text:

        try:
            # print(data['id'])
            job = {'Job_ID': data['id'].split(':')[1],
                   'Job_Title': data['position_title'],
                   'Company_Name': data['organization_name'],
                   'Salary': data['maximum'],
                   'Last_Date': data['end_date'],
                   'Location': data['locations'][0],
                   'Link': data['url']}
            job_data_item.append(job)
        except:
            pass
    return job_data_item





