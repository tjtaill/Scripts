if __name__ == "__main__":
    import sys
    import virtualbox
    
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])
    
    snap = vm.current_snapshot
    print(snap.name)
    
        
    