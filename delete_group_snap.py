import sys

def delete_group_snap(snap_name):
    """
    restores the running groups to a snapsot
    """
    import virtualbox
    from running_groups import running_groups
    from delete_vm_snap import delete_vm_snap
    
    vbox = virtualbox.VirtualBox()
    
    sys.coinit_flags = 0
    
    rg = running_groups()
    for vm in vbox.machines:        
        groups = {group for group in vm.groups}
        intersection = rg & groups
        if  intersection:
            snap = vm.find_snapshot(snap_name)
            delete_vm_snap(vm, snap)
    
if __name__ == "__main__":
    delete_group_snap(sys.argv[1])
        