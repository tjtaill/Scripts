if __name__ == "__main__":
    from running_vms import running_vms
    from running_groups import running_groups
    from vm_snaps import vm_snaps
    from tree import Tree
    
    rgs = running_groups()
    rg = rgs.pop()
    
    snaps_tree = Tree()
    snaps_tree.add_node(rg, None)
    
    for vm in running_vms():
        vm_snaps(vm, snaps_tree, rg)
    
    snaps_tree.display(rg)
