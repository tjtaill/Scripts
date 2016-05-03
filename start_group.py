import sys

def start_group(group_name):
    import virtualbox
    from start_vm import start_vm
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    
    for vm in vbox.machines:
        groups = {str(group) for group in vm.groups}
        if group_name in groups:
            start_vm(vm)


if __name__ == "__main__":
    from progress_bar import group_progress_bar
    start_group(sys.argv[1])
    group_progress_bar()
