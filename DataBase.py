from Database_table_model import *


def insert_all_job_to_table(job_data):
    try:
        if not job_table_model.create_table(True):
            try:
                for job in job_data:
                    job_new = job_table_model.insert(
                        Job_ID=job['Job_ID'],
                        Job_Title=job['Job_Title'],
                        Company_Name=job['Company_Name'],
                        Salary=job['Salary'],
                        Last_Date=job['Last_Date'],
                        Location=job['Location'],
                        Link=job['Link'])
                    job_new.execute()
                print("Done inserting data")
            except OperationalError as e:
                print("I am the error ", e)
            else:
                pass
    except OperationalError as e:
        print("Failed connection to the database", e)


def get_all_data_from_the_table():
    all_data = []
    jobs = job_table_model.select()
    for job in jobs:
        temp = {'Job_ID': job.Job_ID, 'Job_Title': job.Job_Title, 'Company_Name': job.Company_Name,
                'Salary': job.Salary, 'Last_Date': job.Last_Date, 'Location': job.Location, 'Link': job.Link}
        all_data.append(temp)
        print(temp)
    return all_data


def get_parametrized_data():
    all_jobs = []
    jobs = job_table_model.select()
    for job in jobs:
        if 'ny' in str(job.Location).lower():
            all_jobs.append(job)
    return all_jobs


# def jobs_with_combination(all_job, location, part_time, full_time, specific_job):
#     all_jobs = []
#     jobs = job_table_model.select()
#     for job in jobs:
#         if location:
#             if 'ny' in str(job.Location).lower():
#                 all_jobs.append(job)
#         return all_jobs
#
#
#             url= url+ " +in+" + "dc"
#         if part_time:
#             url = url + '+ parttime '
#         if full_time:
#             url = url + '+ fulltime '
#         if specific_job:
#             url = url + '+ Computer Engineer '
#         if all_job:
#             url = url + "&size=40"
#         else:
#             url = url + "&size=10"
#         response = requests.get(url)
#         result = parse_data(response.json())
#         return result
