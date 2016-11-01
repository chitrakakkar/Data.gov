from Database_table_model import *
from tabulate import tabulate


def insert_all_job_to_table(job_data):
    try:
        db.connect()
        db.create_table(job_table_model)
        if not job_table_model.create_table(True):
            try:
                for job in job_data:
                    job_new = job_table_model.create(
                        Job_ID=job['Job_ID'],
                        Job_Title=job['Job_Title'],
                        Company_Name=job['Company_Name'],
                        Salary=job['Salary'],
                        Last_Date=job['Last_Date'],
                        Location=job['Location'],
                        Link=job['Link'])
                    job_new.save()
                print("Done inserting data")
            except OperationalError as e:
                print("I am the error " , e)
        else:
            print("here")
    except OperationalError as e:
        print("Failed connection to the database", e)


def get_all_data_from_the_table():
    all_data = []
    for job in job_table_model.select():
        small = compile_jobs(job)
        all_data.append(small)
    print(tabulate(all_data, tablefmt="fancy_grid",  headers=["JOB_ID", "Job_Title", "Company_name",
                                                              "Salary", "Last_Date", "Location", "Link"]))


def compile_jobs(record):
    small_list = [record.Job_ID, record. Job_Title, record.Company_Name, record.Salary, record.Last_Date, record.Location, record.Link]
    return small_list


def get_parametrized_data(search_keyword):
    all_jobs = []
    jobs = job_table_model.select()
    for job in jobs:
        if search_keyword.lower() in str(job.Location).lower():
            all_jobs.append(job)
    return all_jobs
