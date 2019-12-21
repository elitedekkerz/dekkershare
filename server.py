#!/usr/env python3
from flask import Flask, render_template
import os
import peer_discovery

peers = peer_discovery.peer_handler()
peers.update_peers()

try:
    share_dir = os.getcwd()+'\share'
    if not os.path.exists(share_dir):
        os.makedirs(share_dir)
except:
    print("unable to set share file")
    share_dir = './'

app = Flask(__name__, static_url_path='/static/', static_folder=share_dir)

@app.route("/")
def downloads():
    global peers
    print(peers.peers)
    return render_template('files.html', files = os.listdir(share_dir), version = "0.0000", peers = peers.peers)

if __name__ == '__main__':
    app.run("0.0.0.0", 80, debug=True)
    peers.thread_run = False
