#!/usr/env python3
from flask import Flask, render_template
import os
import peer_discovery
from Frame import MyForm
import threading
import wx
from config import Configuration

peers = peer_discovery.peer_handler()
peers.update_peers()

conf = Configuration()

try:
    conf.Set_share_dir(os.getcwd()+'\share')
    if not os.path.exists(share_dir):
        os.makedirs(share_dir)
except:
    print("unable to set share file")
    conf.Set_share_dir('./')

app = Flask(__name__, static_url_path='/static/', static_folder=conf.Get_share_dir())

@app.route("/")
def downloads():
    global peers
    print(peers.peers)
    return render_template('files.html', files = os.listdir(conf.Get_share_dir()), version = "0.0000", peers = peers.peers)

if __name__ == '__main__':
    threading.Thread(target = app.run, args = ("0.0.0.0", 80,)).start()
    wxApp = wx.App(False)
    f = MyForm(conf)
    f.Show()
    wxApp.MainLoop()
    peers.thread_run = False
