import sys
import wx
#import IntegrationFrame
from IntegrationFrame import *
#TODO: use import instead of from ... import ...


class IntegrationApp(wx.App):
    def __init__(self, process_steps):
        self.process_steps = process_steps
        wx.App.__init__(self, False)

    def OnInit(self):
        self.frame = IntegrationFrame(parent=None, id=-1,
                                      title='Integration Assist',
                                      steps=self.process_steps)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
