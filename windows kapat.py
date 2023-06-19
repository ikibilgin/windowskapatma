import subprocess

def bilgisayari_kapat():
    subprocess.call(["shutdown", "/s", "/t", "0"])

bilgisayari_kapat()
