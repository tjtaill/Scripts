def stop_group():
    import virtualbox
    import sys
    from stop_vm import stop_vm
    from running_groups import running_groups
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    
    rg = running_groups() 
    
    for vm in vbox.machines:
        groups = {group for group in vm.groups}
        intersection = rg & groups
        if  intersection:
            stop_vm(vm)

if __name__ == "__main__":
    """
    stop the currently running group
    """
    stop_group()