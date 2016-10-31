import os
from API import digital_job as ap
import wx

import wx.grid


# Define the GUI as a window/frame
class Data_Gov_Gui(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(1100, 700))  # Bring everything from __init__ for Frame into this class
        # GUI APPEARANCE (LAYOUT AND DESIGN)
        self.panel = wx.Panel(self, size=(500, 500))
        # self.SetBackgroundColour('pink')
        self.SetBackgroundColour((198, 235, 242))
        self.SetTitle('Data Gov JOBS')
        self.CreateStatusBar()
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
        self.Database_Select = wx.CheckBox(self.panel, 10, 'Database_Mode', pos=(600, 10))
        self.Database_Select.SetValue(False)
        self.search_Txt = wx.TextCtrl(self.panel, pos=(400, 100), size=(400, 25), style=wx.ALIGN_LEFT, value='Enter the keyword')
        self.Search_button = wx.Button(self.panel, pos=(800, 100), size=(30, 25), label="S")
        self.Search_button.SetForegroundColour('orange')
        self.All_Jobs = wx.CheckBox(self.panel, 10, 'All Jobs', pos=(50, 200))
        self.All_Jobs.SetValue(False)
        self.Location_Based = wx.CheckBox(self.panel, 10, 'Location-Based', pos=(250, 200))
        self.Location_Based.SetValue(False)
        self.Part_Time = wx.CheckBox(self.panel, 10, 'Part-Time', pos=(500, 200))
        self.Part_Time .SetValue(False)
        self.Full_Time = wx.CheckBox(self.panel, 10, 'Full-Time', pos=(750, 200))
        self.Full_Time.SetValue(False)
        self.Specific_Job = wx.CheckBox(self.panel, 10, 'Specific-Jobs', pos=(975, 200))
        self.Specific_Job.SetValue(False)
        self.display_Txt = wx.grid.Grid(self.panel, pos=(10, 300), id=1, name="Search-result", size=(1080, 170))
        color = (255, 255, 255)
        color2 = 206, 133, 226
        self.display_Txt.SetDefaultCellBackgroundColour(color)
        self.display_Txt.SetForegroundColour(color2)
        self.Search_button.SetBackgroundColour((141, 221, 247))
        self.Search_button.SetFont(bold_font)
        self.Search_button.Bind(wx.EVT_BUTTON, self.OnSearchcButton)
        self.Quit_Button = wx.Button(self.panel, pos=(30, 600), size=(100, -1), label="Quit")
        self.Quit_Button.Bind(wx.EVT_BUTTON, self.OnQuitButton)
        self.Quit_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Quit_Button.SetFont(bold_font)
        self.Clear_Button = wx.Button(self.panel, pos=(300, 600), size=(100, -1), label="Clear")
        self.Clear_Button.Bind(wx.EVT_BUTTON, self.OnClearButton)
        self.Clear_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Clear_Button.SetFont(bold_font)
        self.Refresh_Button = wx.Button(self.panel, pos=(600, 600), size=(100, -1), label="Refresh")
        self.Refresh_Button.Bind(wx.EVT_BUTTON, self.OnRefreshButton)
        self.Refresh_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Refresh_Button.SetFont(bold_font)
        self.Save_Button = wx.Button(self.panel, pos=(900, 600), size=(100, -1), label="Save")
        self.Save_Button.Bind(wx.EVT_BUTTON, self.OnSaveButton)
        self.Save_Button.SetBackgroundColour((206, 133, 226))  # orange
        self.Save_Button.SetFont(bold_font)

    # @staticmethod
    def OnSearchcButton(self, e):
        # displays the jobs which is a list of dictionaries
        jobs = ap.all_job()
        # count the number of dictionaries inside jobs which is a list of dictionaries
        grid_row = len(jobs)
        if grid_row != 0:
            dict = {}
            # telling complier that job[0] is a dictionary
            dict = jobs[0]
            # dict.keys() returns a class(array) of keys inside a dictionary
            grid_col_Label = []  # an empty array to merge column headers from job
            grid_col_Label.extend(dict.keys())  # merges all the keys as header into grid_co_label array
            grid_col_Label.sort()
            # displays the table inside the grid_view
            self.display_Txt.CreateGrid(grid_row, len(grid_col_Label))
            # to set column labels in grid
            for Counter in range(0, len(grid_col_Label)):
                column_name = grid_col_Label[Counter]
                self.display_Txt.SetColLabelValue(Counter, column_name)
            for Counter in range(0, grid_row):
                temp_dict= {}
                temp_dict = jobs[Counter]
                for keys in grid_col_Label:
                    Values = temp_dict[keys]
                    self.display_Txt.SetCellValue(Counter, grid_col_Label.index(keys), str(Values))
                    self.display_Txt.AutoSizeColumns(True)
    def OnClearButton(self,e):
        # self.display_Txt.SetColLabelValue = " "
        self.display_Txt.ClearGrid()
       


    def OnSaveButton(self,e):
        pass

    def OnRefreshButton(self,e):
        pass

    def OnQuitButton(self, e):
        exit(0)

# Start the main part of the program
# application must have a wx.App instance, and all creation of UI objects should be delayed until after the wx.App o
app = wx.App(False)   # bootstrap the wxPython system and initialize the underlying gui toolkit
# set and get application-wide properties
frame = Data_Gov_Gui(None)  # This defines frame as our GUI
frame.Show()         # Show the GUI
app.MainLoop()       # Execute the main GUI event loop-start the application's MainLoop whose role is to handle the events.


