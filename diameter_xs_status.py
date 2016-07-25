if __name__ == "__main__":
    import sys   
    from bw_ssh_shell import BwSshShell
    from bw_cli_shell import BwCliShell
          
    xs_ip = '10.9.55.21'
    if len(sys.argv) > 1:
        xs_ip = sys.argv[1]        
       
    with BwCliShell(xs_ip) as xscli:
        xscli << "XSDiagnostic;Diameter;Peers;"
        xscli << "get"

    