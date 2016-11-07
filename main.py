from API import digital_job
from DataBase import *
from Database_table_model import db
from GUI import *


def main():
    # Start the main part of the program
    # application must have a wx.App instance, and all creation of UI objects should be delayed until after the wx.App o
    db.connect()
    db.create_table(job_table_model, safe=True)
    app = wx.App(False)  # bootstrap the wxPython system and initialize the underlying gui toolkit
    # set and get application-wide properties
    frame = Data_Gov_Gui(None)  # This defines frame as our GUI
    frame.Show()  # Show the GUI
    # Execute the main GUI event loop-start
    # the application's MainLoop whose role is to handle the events.
    app.MainLoop()

main()
