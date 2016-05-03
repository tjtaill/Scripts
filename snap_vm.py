
def snap_vm(vm, snap_name):
    session = vm.create_session()
    m = session.machine
    m.take_snapshot(snap_name, '', True)

if __name__ == "__main__":
    import sys
    import virtualbox as vb
    
    sys.coinit_flags = 0
    
    vbox = vb.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])
        
    snap_vm(vm, sys.argv[2])    
    

    
        
    