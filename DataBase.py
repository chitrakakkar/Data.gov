from Database_table_model import *
from tabulate import tabulate
import json


def insert_all_job_to_table(job_data):
    try:
        job_new = job_table_model.create(
            Job_ID=job_data['Job_ID'],
            Job_Title=job_data['Job_Title'],
            Company_Name=job_data['Company_Name'],
            Salary=job_data['Salary'],
            Last_Date=job_data['Last_Date'],
            Location=job_data['Location'],
            Link=job_data['Link']
        )
        job_new.save()
    except OperationalError as e:
        print("I am the error", e)


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
    # select
    # Location
    # from job_table_model where
    # Location
    # Like
    # '%NY' [u.username for u in user_q], .where(job_table_model.Location.contains(search_keyword))
    jobs = job_table_model.select()
    # Location = [job.Location for job in jobs]

    # jobs = job_table_model.select().where(job_table_model.Location.contains(search_keyword))
    # print("Location", Location)
    #
    for job in jobs:
        if search_keyword.lower() in str(job.Location).lower():
            all_jobs.append(job)
    return all_jobs
