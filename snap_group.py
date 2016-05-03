import sys

def snap_group(snap_name):
    """
    takes a snap shot of the running group
    """
    import virtualbox
    from running_groups import running_groups
    from snap_vm import snap_vm
    
    vbox = virtualbox.VirtualBox()
    
    sys.coinit_flags = 0
    
    rg = running_groups()
    for vm in vbox.machines:        
        groups = {group for group in vm.groups}
        intersection = rg & groups
        if  intersection:
            snap_vm(vm, snap_name)
    
if __name__ == "__main__":
    snap_group(sys.argv[1])
        