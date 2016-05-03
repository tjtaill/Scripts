def restart_vm(vm):
    from stop_vm import stop_vm
    from start_vm import start_vm
    stop_vm(vm)
    start_vm(vm)
    
if __name__ == "__main__":
    import sys
    import virtualbox
    from progress_bar import vm_progress_bar
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])    
    restart_vm(vm)
    vm_progress_bar()