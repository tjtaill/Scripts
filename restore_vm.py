from stop_vm import stop_vm
from start_vm import start_vm
    

def restore_vm(vm, snap):
    stop_vm(vm)
    
    session = vm.create_session()
    m = session.machine
    
    progress = m.restore_snapshot(snap)
    progress.wait_for_completion(-1)
    session.unlock_machine()
    
    start_vm(vm)


if __name__ == "__main__":
    import sys
    import virtualbox as vb
    from progress_bar import vm_progress_bar
    
    sys.coinit_flags = 0
    
    vbox = vb.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])
    snap = vm.find_snapshot(sys.argv[2])
    
    restore_vm(vm, snap)
    vm_progress_bar()

        
    