import os, wx
from API import digital_job as ap
from tabulate import *
import wx
import wx.grid


# Define the GUI as a window/frame
class Data_Gov_Gui(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(1000, 1000))  # Bring everything from __init__ for Frame into this class
        # GUI APPEARANCE (LAYOUT AND DESIGN)
        self.panel = wx.Panel(self, size=(500, 500))
        self.SetTitle('Data Gov JOBS')
        self.SetBackgroundColour('pink')
        self.CreateStatusBar()
        menu = wx.Menu()
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", " Exit the GUI")
        menuBar = wx.MenuBar()
        # Give the MenuBar a Title
        menuBar.Append(menu, "File")
        # Connect the MenuBar to the frame
        self.SetMenuBar(menuBar)
        # Set the fonts to be used
        bold_font = wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        # Input search keyword name widget ----------------------------------------------
        # self.model_lblname = wx.StaticText(self.panel, pos=(500, 500), label="Search", style=wx.ALIGN_RIGHT)
        # self.model_lblname.SetFont(bold_font)
        self.search_Txt = wx.TextCtrl(self.panel, pos=(200, 300), size=(200, -1), style=wx.ALIGN_LEFT, value='Enter the keyword')
        self.search_button = wx.Button(self.panel, pos=(400, 300), size=(20, -1), label="")
        self.search_button.Bind(wx.EVT_BUTTON, self.OnSearchcButton)
        # self.display_Txt = wx.TextCtrl(self.panel, pos=(10, 400), size=(980, 170), style=wx.ALIGN_LEFT| wx.TE_MULTILINE, value="")
        self.display_Txt = wx.grid.Grid(self.panel, pos=(10, 400), id=1, name="Search-result", size=(980, 170))
        self.search_button.SetBackgroundColour((141, 221, 247))
        self.search_button.SetFont(bold_font)
        self.clear_button = wx.Button(self.panel, pos=(50, 700), size=(100, -1), label="Quit")
        self.clear_button.Bind(wx.EVT_BUTTON, self.OnQuitButton)
        self.clear_button.SetBackgroundColour((255, 126, 71))  # orange
        self.clear_button.SetFont(bold_font)
        # -------------- Define the layouts of the widgets ----------------
        # b = 5
        # w = 150
        # model_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # # model_sizer.Add(self.model_lblname, 0, wx.ALL, b)
        # model_sizer.Add(self.model_name, 0, wx.ALL, b)
        # # model_sizer.SetItemMinSize(self.model_lblname, (w, -1))

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
        pass

    def OnSaveButton(self,e):
        pass

    def OnRefreshButton(self,e):
        pass

    def OnQuitButton(self, e):

        exit(1)

# Start the main part of the program
# application must have a wx.App instance, and all creation of UI objects should be delayed until after the wx.App o
app = wx.App(False)   # bootstrap the wxPython system and initialize the underlying gui toolkit
# set and get application-wide properties
frame = Data_Gov_Gui(None)  # This defines frame as our GUI
frame.Show()         # Show the GUI
app.MainLoop()       # Execute the main GUI event loop-start the application's MainLoop whose role is to handle the events.


