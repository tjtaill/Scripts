from bw_sftp_session import BwSftpSession
import os


class XspLogSftpSession(BwSftpSession):

    def __init__(self, ip_address, local_dir=os.getcwd()):
        super().__init__(ip_address, '/var/broadworks/logs/xsp', local_dir)
        self.file_pattern = r'.*\.(?:log|txt)'
        self.nlogs = 5

if __name__ == '__main__':
    with XspLogSftpSession('10.9.55.22') as xsp_sftp:
        xsp_sftp.get_logs()
