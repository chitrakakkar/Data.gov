import os, wx
from API import digital_job as ap
# Define the GUI as a window/frame


class Data_Gov_Gui(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)  # Bring everything from __init__ for Frame into this class
        # GUI APPEARANCE (LAYOUT AND DESIGN)
        self.panel = wx.Panel(self, size=(1800, 1000))
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
        self.model_name = wx.TextCtrl(self.panel, pos=(200, 300), size=(200, -1), style=wx.ALIGN_LEFT, value='')
        self.search_button = wx.Button(self.panel, pos=(400, 300), size =(20,-1),label="Search")
        self.search_button.Bind(wx.EVT_BUTTON, self.OnSearchcButton())
        self.search_button.SetBackgroundColour((141, 221, 247))
        self.search_button.SetFont(bold_font)
        # self.clear_button = wx.Button(self.panel, label="Clear All")
        # self.clear_button.Bind(wx.EVT_BUTTON, self.OnClearButton)
        # self.clear_button.SetBackgroundColour((255, 126, 71))  # orange
        # self.clear_button.SetFont(bold_font)
        # -------------- Define the layouts of the widgets ----------------
        # b = 5
        # w = 150
        # model_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # # model_sizer.Add(self.model_lblname, 0, wx.ALL, b)
        # model_sizer.Add(self.model_name, 0, wx.ALL, b)
        # # model_sizer.SetItemMinSize(self.model_lblname, (w, -1))

    def OnSearchcButton(self):
        jobs = ap.all_job()
        return jobs

    def OnClearButton(self):
        pass

    def OnSaveButton(self):
        pass

    def OnRefreshButton(self):
        pass
    def OnQuitButton(self):
        exit(0)



# Start the main part of the program
# application must have a wx.App instance, and all creation of UI objects should be delayed until after the wx.App o
app = wx.App(False)   # bootstrap the wxPython system and initialize the underlying gui toolkit
# set and get application-wide properties
frame = Data_Gov_Gui(None)  # This defines frame as our GUI
frame.Show()         # Show the GUI
app.MainLoop()       # Execute the main GUI event loop-start the application's MainLoop whose role is to handle the events.
