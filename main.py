from API import digital_job
from DataBase import *
from Database_table_model import db
from GUI import *


def main():
    # Start the main part of the program
    # application must have a wx.App instance, and all creation of UI objects should be delayed until after the wx.App o
    app = wx.App(False)  # bootstrap the wxPython system and initialize the underlying gui toolkit
    # set and get application-wide properties
    frame = Data_Gov_Gui(None)  # This defines frame as our GUI
    frame.Show()  # Show the GUI
    app.MainLoop()  # Execute the main GUI event loop-start the application's MainLoop whose role is to handle the events.

    # user_input = str(input("Enter the state"))
    # jobs = digital_job.all_job()
    # #print(tabulate(jobs, tablefmt="fancy_grid"))
    # #headers=["ID", "Job_Title", "Company-name", "Salary","Last-date", "Location", "Link"]
    # db.connect()
    # db.create_table(job_table_model)
    # for job in jobs:
    #     insert_all_job_to_table(job)
    # records = get_parametrized_data(user_input)
    # if len(records) != 0:
    #     for record in records:
    #         print("JOB ID is {} with Job title '{}'at {} and pays {} "
    #               "\n Last Date for application is {} \n Location {} \n Link for job is {} ".
    #               format(record.Job_ID, record. Job_Title, record.Company_Name,
    #                      record.Salary, record.Last_Date, record.Location, record.Link))
    # else:
    #     print("No job found at the given location !!!")
    # # get_all_data_from_the_table()


main()
