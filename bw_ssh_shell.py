import paramiko
import sys
import re


_r = re.compile("\033\[[0-9;?]*[mhl]")


def strip_console_control_chars(s1):
    s2 = _r.sub('', s1)
    return s2


def encoded_print(s1):
    enc = sys.stdout.encoding
    s2 = s1.encode(enc, errors='backslashreplace').decode(enc)
    print(strip_console_control_chars(s2))


class BwSshShell(object):
    def __init__(self, ip_address, prompt='> [0m'):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip_address = ip_address
        self.prompt = prompt

    def _wait_for_prompt(self):
        buffer = ''
        while not buffer.endswith(self.prompt):
            try:
                b = self.channel.recv(9999)
                resp = str(b, encoding='ISO-8859-1')
                buffer += resp
            except UnicodeEncodeError as uee:
                continue
            encoded_print(resp)

    def change_prompt(self, prompt):
        self.prompt = prompt

    def send_cmd(self, cmd):
        self.channel.send(cmd + '\n')
        self._wait_for_prompt()

    def __lshift__(self, cmd):
        self.send_cmd(cmd)

    def __enter__(self):
        self.ssh.connect(self.ip_address, username='bwadmin', password='bwadmin')
        self.channel = self.ssh.invoke_shell()
        self.ssh.get_transport().set_keepalive(1)
        return self

    def __exit__(self, exception_type, exception_val, exception_trace):
        self.ssh.close()
        return False

if __name__ == '__main__':
    with BwSshShell('10.9.55.21') as ssh:
        ssh << 'ls'
