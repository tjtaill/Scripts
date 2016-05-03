from bw_ssh_shell import BwSshShell


class BwCliShell(BwSshShell):
    def __init__(self, ip_address):
        super().__init__(ip_address)

    def __enter__(self):
        super().__enter__()
        self.change_prompt('> ')
        self << 'bwcli'
        return self

if __name__ == '__main__':
    with BwCliShell('10.9.55.21') as bwcli:
        bwcli << 'tree'
        bwcli << 'help'
