def running_groups():
    import virtualbox
    import sys
    from running_vms import is_running
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    groups = set()
    for vm in vbox.machines:
        if is_running(vm):
            groups.update(vm.groups)            
    return groups


if __name__ == "__main__":
    for group in running_groups():
        print(group)
    