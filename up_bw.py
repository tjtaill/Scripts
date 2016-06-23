if __name__ == "__main__":
    import subprocess as sp
    import sys
    
    
    if len(sys.argv) > 1:
        vms = sys.argv[1:] 
    else:
        vms = ['ns', 'nds', 'ps', 'xsp', 'xs']
             
    
    for vm in vms:
        cmd = ' '.join(['cd C:\\svn\\trunk\\BUILD\\dev\\VM', '&', 'vm.bat vm.%s.properties up-bw' % vm])        
        sp.Popen(["start", "cmd", "/k", cmd], shell = True)
   