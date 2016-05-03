from bw_ssh_shell import BwSshShell
import sys

if __name__ == "__main__":
    cmd = sys.argv[1]
    with BwSshShell('10.9.55.25') as xs:
        xs << cmd
