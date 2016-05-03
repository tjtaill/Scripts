from bw_ssh_shell import BwSshShell
import sys

def bw_bash(cmd):
    hosts = [ '10.9.55.21',
        '10.9.55.27',
        '10.9.55.22',
        '10.9.55.42',
        '10.9.55.25' ]
    for host in hosts:
        with BwSshShell(host) as bw:
            bw << cmd


if __name__ == "__main__":
    cmd = sys.argv[1]
    bw_bash(cmd)