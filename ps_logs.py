from bw_sftp_session import BwSftpSession
import os


class PsLogSftpSession(BwSftpSession):

    def __init__(self, ip_address, local_dir=os.getcwd()):
        super().__init__(ip_address, '/var/broadworks/logs/provisioning', local_dir)
        self.file_pattern = r'PS.*\.(?:log|txt)'
        self.nlogs = 2

if __name__ == '__main__':
    with PsLogSftpSession('10.9.55.27') as ps_sftp:
        ps_sftp.get_logs()
