import sys
import os

if __name__ == "__main__":
    base_dir = sys.argv[1]
    version = sys.argv[2]
    
    # check out code
    
    # create eclipse project
    
    # build xs eclipse project
    
    # update vm's
    # 1. go to vm dir
    vm_dir = os.path.sep.join( [base_dir, "BUILD", "dev", "VM"] )
    os.chdir( vm_dir )
    # 2. fill out and copy template file based on release version
    
    # 3 run vm command on these vm files
    
    # provision vm's
    xs_dir = os.path.sep.join( [base_dir, "BUILD", "dev", "XS", "virtualenv"] )
    os.chdir( xs_dir )
    
    # fill out custom/XS propoerties file
    
    
    