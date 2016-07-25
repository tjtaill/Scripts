from bw_ssh_shell import BwSshShell
from progress_bar import restart_progress_bar

if __name__ == "__main__":    
    with BwSshShell('10.9.55.21') as xs:
        xs << 'restartbw'
    restart_progress_bar()
