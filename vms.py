if __name__ == "__main__":
    import virtualbox
    import sys
    
    sys.coinit_flags = 0
    
    vbox = virtualbox.VirtualBox()
    for vm in vbox.machines:
        print(vm.name)