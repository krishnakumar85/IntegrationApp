import wx

class IntegrationFrame(wx.Frame):
    def __init__(self, parent, id, title, steps):
        wx.Frame.__init__(self, parent, id, title=title, size=wx.DefaultSize)
        panel = wx.Panel(self, size=(1000,125))
        sizer = wx.GridSizer(rows=len(steps), cols=1, hgap=5, vgap=5)
        
        self.Bind(wx.EVT_CLOSE,self.onCloseWindow)
        
        self.processButtons = []
        for this_step in steps:
            print this_step.stepname
            thisbtn = wx.Button(panel, label=this_step.stepname, size=(100,30))
            self.Bind(wx.EVT_BUTTON, this_step.EntryPoint, thisbtn)
            sizer.Add(thisbtn)
        
        self.SetSizer(sizer)
        self.Fit()
        #panel = wx.Panel(self)
        #self.parseButton = wx.Button(panel, label="Parse", pos=(10,10), size=(50,30))
        #self.fetchButton = wx.Button(panel, label="Fetch", pos=(100,10), size=(50,30))
        #self.Bind(wx.EVT_BUTTON, self.Parse, self.parseButton)
        #self.Bind(wx.EVT_BUTTON, self.Fetch, self.fetchButton)
    
        
    def onCloseWindow(self, event):
        #wx.MessageBox("Thank you!")
        self.Destroy()