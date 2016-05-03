import sys
import os
from getpass import getpass


if __name__ == "__main__":
    """
    coxs.py trunk
    coxs.py working/ttaillefer/CALEA
    coxs.py working/mreiher/TIII47014_21sp2_v1
    """
    
    passwd = getpass()
    user = 'ttaillefer'
    
    _svn_base = "https://beach.mtl.broadsoft.com/svn/"
    svn_url = _svn_base + sys.argv[1]
    
    
    
    os.system("svn co --username %s --password %s --depth empty %s ." % (user,passwd,svn_url))
    os.system("svn up --username %s --password %s --set-depth infinity XS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BASE" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BUILD" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity SHARE" % (user,passwd))
    os.system("svn up --username %s --password %s -N BWApps" % (user,passwd))
    os.system("svn up --username %s --password %s -N WebApps" % (user,passwd))
    os.system("svn up --username %s --password %s -N BINARIES" % (user,passwd))
    os.system("svn up --username %s --password %s -N BINARIES/common" % (user,passwd))
    
    # This is the current ant version for Trunk
    os.system("svn up --username %s --password %s --set-depth infinity BINARIES/common/apache-ant-1.9.6" % (user,passwd))
    
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/ExecutionDataless" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/Provisioning" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity XSP" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity OCS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity PS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/CommPilot-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/DeviceManagementFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/EnhancedCallLogsDBManagement-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/FileRepos" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/FlashPolicy" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/JWSFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/MediaFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/OCIFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/OCIOverSoap" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/OCS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/WebContainer" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/Xsi-Actions-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/Xsi-MMTel-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/Xsi-Events-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity BWApps/Xsi-VTR" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/CommPilot-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/OCIOverSoap" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/MediaFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/JWSFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/DeviceManagementFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/OCIFiles" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/Xsi-Actions-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/Xsi-MMTel-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/Xsi-Events-XS-TAS" % (user,passwd))
    os.system("svn up --username %s --password %s --set-depth infinity WebApps/Xsi-VTR" % (user,passwd))