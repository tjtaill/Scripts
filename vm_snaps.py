def vm_snaps(vm, snaps_tree, root):
    from collections import deque   
    
    snaps = deque()
    snaps.append(vm.find_snapshot(""))
    snaps_tree.add_node(vm.name, root)
    last_parent = vm.name
    while snaps:
        s = snaps.popleft()
        snaps_tree.add_node(s.name, last_parent)
        last_parent = s.name
        snaps.extend(s.children)

if __name__ == "__main__":
    import sys
    import virtualbox    
    from tree import Tree
    
    sys.coinit_flags = 0   
    vbox = virtualbox.VirtualBox()    
    snaps_tree = Tree()
    vm = vbox.find_machine(sys.argv[1])
    vm_snaps(vm, snaps_tree, None)
    snaps_tree.display(vm.name)

    