import sys
import wx
#import IntegrationFrame
from IntegrationFrame import *
#TODO: use import instead of from ... import ...
from ProcessStep import *

class IntegrationApp(wx.App):
    def __init__(self, process_steps):
        self.process_steps = process_steps
        wx.App.__init__(self,False)

    def OnInit(self):
        self.frame = IntegrationFrame(parent=None, id=-1, title='Integration Assist', steps=self.process_steps)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    # Adding steps
    process_steps = []
    parsexls = oneParse("Parse","suivi_des_livraisons.xls", "v01-00-00")
    process_steps.append(parsexls)
    fetchdll = twoFetch("Fetch","fetch.xml")
    process_steps.append(fetchdll)
    app = IntegrationApp(process_steps)
    app.MainLoop()

