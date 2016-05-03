import paramiko
import os
import re
from sortedcontainers import SortedList


class RemoteFile(object):

    def __init__(self, file_name, mtime):
        self.file_name = file_name
        self.mtime = mtime

    def __lt__(self, other):
        return self.mtime < other.mtime

    def __repr__(self):
        return self.file_name

    def __str__(self):
        return self.file_name


class BwSftpSession(object):
    def __init__(self, ip_address, remote_dir, local_dir=os.getcwd()):
        self.ip_address = ip_address
        self.remote_dir = remote_dir
        self.local_dir = local_dir
        self.ssh = paramiko.SSHClient()
        self.transport = paramiko.Transport((ip_address, 22))
        # self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __enter__(self):
        self.transport.connect(username='bwadmin', password='bwadmin')
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        return self

    def dir(self, file_pattern):
        attrs = self.sftp.listdir_attr(self.remote_dir)
        filtered = SortedList()
        for attr in attrs:
            if hasattr(attr, "filename"):
                filename = attr.filename
                if re.match(file_pattern, filename):
                    remote_file = RemoteFile(filename, attr.st_mtime)
                    filtered.add(remote_file)
        return filtered

    def __rshift__(self, relative_path):
        remote_file = self.remote_dir + '/' + relative_path

        if not os.path.exists( self.local_dir):
            os.makedirs(self.local_dir)

        local_file = self.local_dir + os.sep + relative_path
        self.sftp.get(remote_file, local_file)

    def __exit__(self, exception_type, exception_val, exception_trace):
        self.sftp.close()
        self.transport.close()
        return False

    def get_logs(self):
        logs = self.dir(self.file_pattern)
        most_recent = []
        for _ in range(self.nlogs):
            log = logs.pop()
            most_recent.append(log)
            self >> str(log)
        return most_recent

if __name__ == '__main__':
    ld = os.getcwd() + os.sep + 'xs'
    with BwSftpSession('10.9.55.21', '/var/broadworks/logs/appserver', ld) as xs_sftp:
        fp = r'XS.*\.(?:log|txt)'
        files = xs_sftp.dir(fp)
        xs_sftp >> str(files.pop())
        xs_sftp >> str(files.pop())
