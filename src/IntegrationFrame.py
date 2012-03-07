import wx


class IntegrationFrame(wx.Frame):
    def __init__(self, parent, id, title, steps):
        wx.Frame.__init__(self, parent, id, title=title, size=wx.DefaultSize)
        panel = wx.Panel(self, size=(1000, 50))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)

        self.processButtons = []
        for this_step in steps:
            print this_step.stepname
            thisbtn = wx.Button(panel, label=this_step.stepname, size=(100, 30))
            this_step.widget = thisbtn
            self.Bind(wx.EVT_BUTTON, this_step.EntryPoint, thisbtn)
            sizer.Add(thisbtn)
            if this_step.PreCondition() != 0:
                thisbtn.Disable()

        self.SetSizerAndFit(sizer)

    def onCloseWindow(self, event):
        #wx.MessageBox("Thank you!")
        self.Destroy()
