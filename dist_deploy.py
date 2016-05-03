if __name__ == "__main__":
    import subprocess as sp
    import sys
    
    dist_deploy_cmds = [ 
        'dist-deploy-ps',
        'dist-deploy-xs',
        'dist-deploy-xsp',        
    ]
    if len(sys.argv) > 1:
        dist_deploy_cmds = []
        for server in sys.argv[1:]:
            dist_deploy_cmds.append('dist-deploy-' + server)
            
    cmds = ['cd C:\\svn\\trunk\\BUILD\\ant\\custom\\XS']    
    for dist_deploy_cmd in dist_deploy_cmds:
        cmds.append('ant %s' % dist_deploy_cmd)
    
    cmd = ' & '.join(cmds)            
    sp.Popen(["start", "cmd", "/k", cmd], shell = True)
