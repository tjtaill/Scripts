def restart_group():
    import virtualbox
    import sys
    from restart_vm import restart_vm
    from running_groups import running_groups
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    
    rg = running_groups() 
    
    for vm in vbox.machines:
        groups = {group for group in vm.groups}
        intersection = rg & groups
        if  intersection:
            restart_vm(vm)

if __name__ == "__main__":
    """
    stop the currently running group
    """
    from progress_bar import group_progress_bar
    restart_group()
    group_progress_bar()