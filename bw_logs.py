from ns_logs import NsLogSftpSession
from ps_logs import PsLogSftpSession
from xsp_logs import XspLogSftpSession
from xs_logs import XsLogSftpSession
import os
import shutil
import re


_local_dir = os.getcwd()

_bw_sftp_servers = [
    (NsLogSftpSession, '10.9.55.25', _local_dir + os.sep + 'ns'),
    (PsLogSftpSession, '10.9.55.27', _local_dir + os.sep + 'ps'),
    (XsLogSftpSession, '10.9.55.21', _local_dir + os.sep + 'xs'),
    (XspLogSftpSession, '10.9.55.22', _local_dir + os.sep + 'xsp')
]

if __name__ == '__main__':
    for factory, ip, local_dir in _bw_sftp_servers:
        if os.path.exists(local_dir):
            shutil.rmtree(local_dir)
        with factory(ip, local_dir) as sftp_server:
            logs = sftp_server.get_logs()
            for log in logs:
                with open(local_dir + os.sep + str(log)) as f:
                    for n, line in enumerate(f):
                        # TODO : improve this so it makes different checks per log type
                        if re.match('.*Exception.*', line):
                            print(line + ' in file: ' + str(log) + ' line: ' + str(n + 1))
