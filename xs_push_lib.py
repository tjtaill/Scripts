from bw_sftp_session import BwSftpSession
from bw_ssh_shell import BwSshShell
import os
import sys


class XsLibSftpSession(BwSftpSession):

    def __init__(self, ip_address, build_number, local_dir=os.getcwd()):
        super().__init__(ip_address, '/usr/local/broadworks/XS_Rel_22.0_1.%s/lib' % build_number, local_dir)
        self.file_pattern = r'*\.jar'
        self.nlogs = 2

if __name__ == '__main__':
    build_number = sys.argv[1]
    lib_name = sys.argv[2]
    with BwSshShell('10.9.55.21') as xs:
        xs << "stopbw"
        
    with XsLibSftpSession('10.9.55.21', build_number) as xs_sftp:
        xs_sftp << lib_name

    with BwSshShell('10.9.55.21') as xs:
        xs << "startbw"

