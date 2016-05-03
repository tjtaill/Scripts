def stop_vm(vm):
    import time
        
    session = vm.create_session()
    progress = session.console.power_down()
    progress.wait_for_completion(-1)
    m = session.machine
    session.unlock_machine()
    time.sleep(1)

if __name__ == "__main__":
    import sys
    import virtualbox
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])    
    stop_vm(vm)
