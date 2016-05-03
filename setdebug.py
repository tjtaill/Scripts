if __name__ == "__main__":
    import subprocess as sp
    import sys
    
    set_debug_cmds = [ 
        'set-debug-ps',
        'set-debug-xs',
        'set-debug-xsp',        
    ]
    if len(sys.argv) > 1:
        set_debug_cmds = []
        for server in sys.argv[1:]:
            set_debug_cmds.append('set-debug-' + server)
            
    cmds = ['cd C:\\svn\\trunk\\BUILD\\ant\\custom\\XS']    
    for set_debug_cmd in set_debug_cmds:
        cmds.append('ant %s' % set_debug_cmd)
    
    cmd = ' & '.join(cmds)            
    sp.Popen(["start", "cmd", "/k", cmd], shell = True)
