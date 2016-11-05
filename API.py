import requests


class digital_job:
    def __init__(self):
        pass

    @staticmethod
    def all_job():
        url = 'https://api.usa.gov/jobs/search.json?query=jobs&size=10'
        # url = 'https://api.usa.gov/jobs/search.json?query=nursing+jobs+in+mn'
        # url = 'https://api.usa.gov/jobs/search.json?query=jobs+at+the+mn&organization_ids=AF'
        response = requests.get(url)
        # it slices the objects up from the big list of json objects
        result = parse_data(response.json())
        return result

    @staticmethod
    def jobs_with_combination(all_job, location, part_time, full_time, specific_job):
        url ="https://api.usa.gov/jobs/search.json?query=jobs"
        if location:
            url= url+ " +in+" + "ny"
        if part_time:
            url = url + '+ parttime '
        if full_time:
            url = url + '+ fulltime '
        if specific_job:
            url = url + '+ Computer Engineer '
        if all_job:
            url = url + "&size=40"
        else:
            url = url + "&size=10"
        response = requests.get(url)
        result = parse_data(response.json())
        return result


def parse_data(response_text):
    job_data_item = []
    for data in response_text:

        try:
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





