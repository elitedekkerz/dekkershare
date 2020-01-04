import wx
import os
import webbrowser

class MyForm(wx.Frame):
    def __init__(self, configuration):
        self.configuration = configuration
        wx.Frame.__init__(self,None,wx.ID_ANY,"Dekkerz SFSOL")
        panel=wx.Panel(self,wx.ID_ANY)
        self.CurrentDir=os.getcwd()
        
        button=wx.Button(panel,wx.ID_ANY,"Select share folder",(10,10))
        button.Bind(wx.EVT_BUTTON,self.OnButton)

        button2=wx.Button(panel,wx.ID_ANY,"Open browser",(10,40))
        button2.Bind(wx.EVT_BUTTON,self.OpenBrowser)

    def OnButton(self,event):
        dlg=wx.DirDialog(self,"Choose a directory",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal()==wx.ID_OK:
            print("you chose %s"%dlg.GetPath())
            self.configuration.Set_share_dir(dlg.GetPath())
            self.configuration.Save_config()

    def OpenBrowser(self,event):
        webbrowser.open("localhost/",new=2)


if __name__ == "__main__":
    app=wx.App(False)
    frame=MyForm()
    frame.Show()
    app.MainLoop()

#frame.Show(True)
#app.MainLoop()

