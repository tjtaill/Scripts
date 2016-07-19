import sys
import os
from getpass import getpass



_user = 'ttaillefer'

def svn_copy(source, destination, passwd):    
    os.system('svn copy %s %s --username %s --password %s -m "create branch"' % (source,destination,_user,passwd)) 

def svn_mkdir(path, passwd):
    os.system('svn mkdir %s --username %s --password %s -m "create folder"' % (path, _user, passwd)) 

if __name__ == "__main__":
    """
    create_xs_branch.py trunk ttaillefer/BW-9274/BRANCH2
    create_xs_branch.py patches/Rel_21.sp2.71 ttaillefer/BW-9274/BRANCH2
    create_xs_branch.py patches/Rel_21.sp2.71 mreiher/TIII47014_21sp2_v1
    """

    passwd = getpass()
    
    _svn_base = "https://beach.mtl.broadsoft.com/svn/"

    _svn_working = _svn_base + "working/"
    
    svn_source = _svn_base + sys.argv[1] + '/'
    svn_target = _svn_working + sys.argv[2] + '/'
    
    svn_mkdir(svn_target, passwd)
    svn_copy(svn_source + 'BASE', svn_target + 'BASE', passwd)
    svn_copy(svn_source + 'BUILD', svn_target + 'BUILD', passwd)
    svn_copy(svn_source + 'SHARE', svn_target + 'SHARE', passwd)
    svn_copy(svn_source + 'BWApps', svn_target  + 'BWApps', passwd)
    svn_copy(svn_source + 'WebApps', svn_target + 'WebApps', passwd)
    svn_copy(svn_source + 'BINARIES', svn_target  + 'BINARIES', passwd)
    svn_copy(svn_source + "XSP", svn_target  + "XSP", passwd)
    svn_copy(svn_source + "OCS", svn_target + "OCS", passwd)
    svn_copy(svn_source + "PS", svn_target + "PS", passwd)
    svn_copy(svn_source + 'XS', svn_target + 'XS', passwd)
