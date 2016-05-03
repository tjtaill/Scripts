import sys

def restore_group(snap_name):
    """
    restores the running groups to a snapsot
    """
    import virtualbox
    from running_groups import running_groups
    from restore_vm import restore_vm
    
    vbox = virtualbox.VirtualBox()
    
    sys.coinit_flags = 0
    
    rg = running_groups()
    for vm in vbox.machines:        
        groups = {group for group in vm.groups}
        intersection = rg & groups
        if  intersection:
            snap = vm.find_snapshot(snap_name)
            restore_vm(vm, snap)
    
if __name__ == "__main__":
    from progress_bar import group_progress_bar
    restore_group(sys.argv[1])
    group_progress_bar()
        