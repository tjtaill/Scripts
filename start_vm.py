import virtualbox


def start_vm(vm):
    session = virtualbox.Session()
    progress = vm.launch_vm_process(session, 'headless', '')    
    progress.wait_for_completion(-1)
    
if __name__ == "__main__":
    import sys
    from progress_bar import vm_progress_bar
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])    
    start_vm(vm)
    vm_progress_bar()