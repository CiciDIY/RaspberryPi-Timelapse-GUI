
import wx
import pygame, sys
from pygame.locals import *
import pygame.camera
import picamera
import time
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.Show(True)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        #init SetUpPanel class
        self.Panel1 = SetUpPanel(self)
        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        #Adding sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.Panel1,0, wx.EXPAND|wx.ALL,5)
        self.SetSizer(sizer)
        self.Fit()
        self.Centre()
        

class SetUpPanel (wx.Panel):
    def __init__(self, parent):
        """Class Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        
        #Creating visuals
        Settings_label = wx.StaticText(self, wx.ID_ANY, "Settings")
        photo_button = wx.Button(self, wx.ID_ANY, "Photo")
        photo_button.Bind(wx.EVT_BUTTON, self.phototaking)
        stop_button = wx.Button(self, wx.ID_ANY, "Stop")
        stop_button.Bind(wx.EVT_BUTTON, self.phototaking)

        #Adding visuals to sizers
        Overal_sizer = wx.BoxSizer(wx.VERTICAL)
        setting_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        setting_sizer.Add(Settings_label,0, wx.ALL,5)
        button_sizer.Add(photo_button,0, wx.ALL,5)
        button_sizer.Add(stop_button,0, wx.ALL,5)

        Overal_sizer.Add(setting_sizer,0, wx.ALL|wx.CENTRE, 5)
        Overal_sizer.Add(button_sizer,0, wx.ALL|wx.CENTRE, 5)

        self.SetSizer(Overal_sizer)
        Overal_sizer.Fit(self)
        self.Centre()

    def phototaking(self,event):
        camera = picamera.PiCamera()
        camera.resolution = (2592, 1944)
        camera.drc_strength = 'high'
        filename = 'Timelapse.jpg'
        
        npath ="/home/pi/" + str(filename)
        if not os.path.isdir(npath):
            os.makedirs(npath)
        time_of_lapse = 100
        while time_of_lapse > 0:
            camera.capture(npath + "/" + str(time_of_lapse) + filename)
            time_of_lapse = time_of_lapse - 1
        camera.close()
        

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
