if __name__ == "__main__":
    import sys   
    from bw_ssh_shell import BwSshShell
    from bw_cli_shell import BwCliShell
          
    dev_ip = '10.9.55.11'
    xs_ip = '10.9.55.21'
    if len(sys.argv) > 2:
        dev_ip = sys.argv[1]
        xs_ip = sys.argv[2]
       
    with BwCliShell(xs_ip) as xscli:
        xscli << "qa;Interface;Accounting;BroadWorksCDRInterface;"
        xscli << "set enabled true"
        xscli << "set enableLocationChanges true"
        xscli << "Diameter;Online;"
        xscli << "set enabled true"
        xscli << "q;ChargingFunctionElement;"
        xscli << "add %s ECF false" % dev_ip
        xscli << "qa;Interface;Diameter;"
        xscli << "set diameterIdentity xs.client.mtl.broadsoft.com"
        xscli << "set realm TestRealm"
        xscli << "set listeningAddress %s" % xs_ip
        xscli << "set listeningPort 3868"
        xscli << "Peers;"
        xscli << "add rf.server.mtl.broadsoft.com 8000 true ipAddress %s" % dev_ip
        xscli << "qa;Applications;ExecutionDataless;Logging;InputChannels;"
        xscli << "set Diameter enabled true severity debug"
    
    with BwSshShell(xs_ip) as xs:
        xs << "restartbw"
    