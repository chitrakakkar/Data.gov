from API import digital_job
from DataBase import *
from Database_table_model import db


def main():
    user_input = str(input("Enter the state"))
    jobs = digital_job.all_job()
    # print(tabulate(jobs, tablefmt="fancy_grid"))
    #headers=["ID", "Job_Title", "Company-name", "Salary","Last-date", "Location", "Link"]
    db.connect()
    db.create_table(job_table_model)
    for job in jobs:
        insert_all_job_to_table(job)
    get_parametrized_data(user_input)
    print("I am here")

    # get_all_data_from_the_table()


main()
