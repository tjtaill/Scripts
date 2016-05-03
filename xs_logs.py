from bw_sftp_session import BwSftpSession
import os


class XsLogSftpSession(BwSftpSession):

    def __init__(self, ip_address, local_dir=os.getcwd()):
        super().__init__(ip_address, '/var/broadworks/logs/appserver', local_dir)
        self.file_pattern = r'XS.*\.(?:log|txt)'
        self.nlogs = 2

if __name__ == '__main__':
    with XsLogSftpSession('10.9.55.21') as xs_sftp:
        xs_sftp.get_logs()
