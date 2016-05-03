def is_running(vm):
    off_state = { 'PoweredOff', 'Aborted', 'Saved' }
    return str(vm.state) not in off_state

def running_vms():
    import virtualbox
    import sys
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    vms = []
    for vm in vbox.machines:
        if is_running(vm):
            vms.append(vm)    
    return vms        

if __name__ == "__main__":
    for vm in running_vms():
        snap = vm.current_snapshot
        print(str(vm) + ' ' + snap.name)
