from API import digital_job as ap
import wx
import wx.grid
from DataBase import *
import os

# Define the GUI as a window/frame
class Data_Gov_Gui(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(1100, 700))  # Bring everything from __init__ for Frame into this class
        # --------GUI APPEARANCE (LAYOUT AND DESIGN)---------
        self.panel = wx.Panel(self, size=(500, 500))
        # self.SetBackgroundColour('pink')
        self.SetBackgroundColour((198, 235, 242))
        self.SetTitle('Data Gov JOBS')
        # self.CreateStatusBar()
        # --------MEnu Designed----------------
        self.menu = wx.Menu()
        self.menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        self.menu.AppendSeparator()
        self.menu.Append(wx.ID_EXIT, "Exit", " Exit the GUI")
        self.menuBar = wx.MenuBar()
        # Give the MenuBar a Title
        self.menuBar.Append(self.menu, "File")
        # Connect the MenuBar to the frame
        self.SetMenuBar(self.menuBar)
        # Set the fonts to be used
        self.menuBar.Bind(wx.EVT_MENU, self.OnQuitButton, self.menuBar)
        self.Show(True)
        bold_font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        # ----------------Database Mode check-Box---------------
        self.offline_mode = wx.CheckBox(self.panel, 10, 'Offline-search', pos=(600, 10))
        self.offline_mode.SetValue(False)
        # ------------Search text Box -------------------------
        self.search_Txt = wx.TextCtrl(self.panel, pos=(400, 100), size=(400, 25), style=wx.ALIGN_LEFT, value='Enter the keyword')
        # ----------Search button------------------
        self.Search_button = wx.Button(self.panel, pos=(800, 100), size=(30, 25), label="S")
        self.Search_button.SetForegroundColour('orange')
        # ---------------All jobs check box---------------
        self.All_Jobs = wx.CheckBox(self.panel, 10, 'All Jobs', pos=(50, 200))
        self.All_Jobs.SetValue(False)
        # ----------------Locations based check box ----------------------
        self.Location_Based = wx.CheckBox(self.panel, 10, 'Location-Based', pos=(250, 200))
        self.Location_Based.SetValue(False)
        # ----------------Part-Time check box ----------------------
        self.Part_Time = wx.CheckBox(self.panel, 10, 'Part-Time', pos=(500, 200))
        self.Part_Time .SetValue(False)
        # ----------------Full-Time check box ----------------------
        self.Full_Time = wx.CheckBox(self.panel, 10, 'Full-Time', pos=(750, 200))
        self.Full_Time.SetValue(False)
        # ----------------Specific-jobs check box ----------------------
        self.Specific_Job = wx.CheckBox(self.panel, 10, 'Specific-Jobs', pos=(975, 200))
        self.Specific_Job.SetValue(False)
        # -----------------Grid Display ----------------
        self.display_Txt = wx.grid.Grid(self.panel, pos=(10, 300), id=1, name="Search-result", size=(1080, 170))
        color = (255, 255, 255)
        color2 = 206, 133, 226
        self.display_Txt.SetDefaultCellBackgroundColour(color)
        self.display_Txt.SetForegroundColour(color2)
        # ---------------Search-button -----------------
        self.Search_button.SetBackgroundColour((141, 221, 247))
        self.Search_button.SetFont(bold_font)
        self.Search_button.Bind(wx.EVT_BUTTON, self.OnSearchcButton)
        # ---------------Quit-button -----------------
        self.Quit_Button = wx.Button(self.panel, pos=(30, 600), size=(100, -1), label="Quit")
        self.Quit_Button.Bind(wx.EVT_BUTTON, self.OnQuitButton)
        self.Quit_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Quit_Button.SetFont(bold_font)
        # ---------------Clear-button -----------------
        self.Clear_Button = wx.Button(self.panel, pos=(300, 600), size=(100, -1), label="Clear")
        self.Clear_Button.Bind(wx.EVT_BUTTON, self.OnClearButton)
        self.Clear_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Clear_Button.SetFont(bold_font)
        # ---------------Refresh-button -----------------
        self.Refresh_Button = wx.Button(self.panel, pos=(600, 600), size=(175, -1), label="Refresh Display")
        self.Refresh_Button.Bind(wx.EVT_BUTTON, self.OnRefreshButton)
        self.Refresh_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Refresh_Button.SetFont(bold_font)
        # ---------------Save-button -----------------
        self.Save_Button = wx.Button(self.panel, pos=(900, 600), size=(100, -1), label="Save")
        self.Save_Button.Bind(wx.EVT_BUTTON, self.OnSaveButton)
        self.Save_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Save_Button.SetFont(bold_font)
        if not self.offline_mode.IsChecked():
            self.Jobs = ap.all_job()
        else:
            self.Jobs = job_table_model.select()
    # This calls the API to fetch all the jobs data.
        # -------------Grid-Creation----------------------

        headers = ["JOB_ID", "Job_Title", "Company_name", "Salary", "Last_Date", "Location", "Link"]
        headers.sort()
        print("Length of Jobs", len(self.Jobs))
        self.display_Txt.CreateGrid(len(self.Jobs), len(headers))
        # self.display_Txt.CreateGrid(len(self.Jobs), len(headers))

        for Counter in range(0, len(headers)):
            column_Header = headers[Counter]
            self.display_Txt.SetColLabelValue(Counter, column_Header)

    def OnSearchcButton(self, e):
        if not self.offline_mode.IsChecked():
            # displays the jobs which is a list of dictionaries
            jobs = self.Jobs
            print(jobs)
            self.grid_Creation(jobs)
        else:
            jobs = get_all_data_from_the_table()
            print("total Jobs from db", len(jobs))
            # count the number of dictionaries inside jobs which is a list of dictionaries
            self.grid_Creation(jobs)

    def OnClearButton(self,e):
        self.display_Txt.ClearGrid()
        self.search_Txt.Clear()
        self.All_Jobs.SetValue(False)
        self.Location_Based.SetValue(False)
        self.Part_Time.SetValue(False)
        self.Full_Time.SetValue(False)
        self.Specific_Job.SetValue(False)

    def OnSaveButton(self, e):
        jobs = self.check_checkBoxes()
        insert_all_job_to_table(jobs)
        self.display_Txt.ClearGrid()

    def OnRefreshButton(self, e):
        if not self.offline_mode.IsChecked():
            self.display_Txt.ClearGrid()
            jobs = self.check_checkBoxes()
            self.grid_Creation(jobs)
        else:
            jobs = get_all_data_from_the_table()




        # else:
        #     if self.Location_Based.IsChecked():
        #         jobs = get_parametrized_data(self.search_Txt.GetValue())
        #         self.grid_Creation(jobs)
        #     if self.Specific_Job.IsChecked():
        #         jobs = get_parametrized_data(self.search_Txt.GetValue())
        #         self.grid_Creation(jobs)
        #     if self.Part_Time.IsChecked():
        #         jobs = get_parametrized_data(self.search_Txt.GetValue())
        #         self.grid_Creation(jobs)
        #     if self.Full_Time.IsChecked():
        #         jobs = get_parametrized_data(self.search_Txt.GetValue())
        #         self.grid_Creation(jobs)

    def OnQuitButton(self, e):
        # for subdir, dirs, files in os.walk('./'):
        #     if "CK.db" in files:
        #       os.remove("CK.db")

        exit(0)



    def grid_Creation(self, jobs):
        grid_row = len(jobs)
        print(grid_row)

        if grid_row != 0:
            dict = {}
            # telling complier that job[0] is a dictionary
            dict = jobs[0]
            # dict.keys() returns a class(array) of keys inside a dictionary
            grid_col_Label = []  # an empty array to merge column headers from job
            grid_col_Label.extend(dict.keys())  # merges all the keys as header into grid_co_label array
            grid_col_Label.sort()
            print("grid_col_Label = ",grid_col_Label)
            # displays the table inside the grid_view
            # to set column labels in grid
            for Counter in range(0, grid_row):
                temp_dict = {}
                temp_dict = jobs[Counter]
                for keys in grid_col_Label:
                    Values = temp_dict[keys]
                    # print("Values = "+str(Values)+"Counter = "+ str(Counter) + "keys = " +str(keys) + "grid col lab"+str(grid_col_Label.index(keys)))
                    try:
                        self.display_Txt.SetCellValue(Counter, grid_col_Label.index(keys), str(Values))
                    except : #OperationalError as e:
                        # print("error", e)
                        pass
                    self.display_Txt.AutoSizeColumns(True)

    def check_checkBoxes(self):
        all_job, location, part_time, full_time, specific_job = False, False, False, False, False
        if not self.offline_mode.IsChecked():
            if self.All_Jobs.IsChecked():
                all_job = True
            if self.Location_Based.IsChecked():
                location = True
            if self.Specific_Job.IsChecked():
                specific_job = True
            if self.Part_Time.IsChecked():
                part_time = True
            if self.Full_Time.IsChecked():
                full_time = True
            jobs = ap.jobs_with_combination(all_job, location, part_time, full_time, specific_job)
            if len(jobs) == 0:
                jobs = [{"JOB_ID": "-", "Job_Title": "-", "Company_name": "-", "Salary": "-", "Last_Date": "-",
                         "Location": "-",
                         "Link": "-"}]
        return jobs