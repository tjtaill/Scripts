from xsp_logs import BwSftpSession
import os


class NsLogSftpSession(BwSftpSession):

    def __init__(self, ip_address, local_dir=os.getcwd()):
        super().__init__(ip_address, '/var/broadworks/logs/routingserver', local_dir)
        self.file_pattern = r'.*\.(?:log|txt)'
        self.nlogs = 5


if __name__ == '__main__':
    with NsLogSftpSession('10.9.55.25') as ns_sftp:
        ns_sftp.get_logs()
