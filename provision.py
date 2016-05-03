if __name__ == "__main__":
    import subprocess as sp
    import sys
    from string import Template
    
    rel = '22.0_1'
    if len(sys.argv) > 2:
        build = sys.argv[1]
        rel = sys.argv[2]
    elif len(sys.argv) > 1:
        build = sys.argv[1]
    else:
        print('need build number')
        sys.exit(1)
    
    
    build_properties_template = Template(
"""
# XS setup
deploy.xs.hostname=ttaillefer-XS
deploy.xs.domain=mtlasdev55.net
deploy.xs.ip=10.9.55.21
deploy.xs.username=bwadmin
deploy.xs.password=bwadmin
deploy.xs.buildid=$rel.$build
debug.xs.cli.port=8001
debug.xs.xs.port=8002

# PS setup
deploy.ps.hostname=ttaillefer-PS
deploy.ps.ip=10.9.55.27
deploy.ps.username=bwadmin
deploy.ps.password=bwadmin
deploy.ps.buildid=$rel.$build
debug.ps.cli.port=8001
debug.ps.ps.port=8002
debug.ps.sa.port=8003

# XSP setup
deploy.xsp.hostname=ttaillefer-XSP
deploy.xsp.ip=10.9.55.22
deploy.xsp.username=bwadmin
deploy.xsp.password=bwadmin
deploy.xsp.buildid=$rel.$build
debug.xsp.cli.port=8001
debug.xsp.webcontainer.port=8002

# NS setup
deploy.ns.hostname=ttaillefer-NS
deploy.ns.ip=10.9.55.25
deploy.ns.username=bwadmin
deploy.ns.password=bwadmin
deploy.ns.buildid=$rel.$build
debug.ns.cli.port=8001
debug.ns.webcontainer.port=8002
debug.ns.ps.port=8003

# NDS setup
deploy.nds.hostname=ttaillefer-NDS
deploy.nds.ip=10.9.55.42
deploy.nds.username=bwadmin
deploy.nds.password=bwadmin
deploy.nds.buildid=$rel.$build

# DEVIP setup (Your local machine possibly running S-CSCF & HSS, Web Browser) 
deploy.dev.ip=10.9.55.11
deploy.farmname=xspfarm

""")
        
    build_properties_file_contents = build_properties_template.substitute({'build': build, 'rel' : rel}) 
    with open('C:\\svn\\trunk\\BUILD\\dev\\XS\\virtualenv\\build.properties', 'w') as build_properties_file:
        build_properties_file.write(build_properties_file_contents)
    
    
    cmd = ' '.join(['cd C:\\svn\\trunk\\BUILD\\dev\\XS\\virtualenv', 
            '&', 'C:\\cygwin\\bin\\sh.exe xsGenDF.sh', 
            '&', 'copy /y NSDF-personal.txt staging',
            '&', 'copy /y PSDF-personal.txt staging',
            '&', 'ant config-all'])
    sp.Popen(["start", "cmd", "/k", cmd], shell = True)
    
    
    
                
                