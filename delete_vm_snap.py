def delete_vm_snap(vm, snap):
    """
    Warning this will delete all children snapshots
    too.
    """
    from collections import deque
    from virtualbox import SessionState
    
    session = vm.create_session()
    m = session.machine
    
    snaps = deque()
    ordered_snaps = deque()
    
    snaps.appendleft(snap)
    while snaps:
        snap = snaps.pop()
        ordered_snaps.appendleft(snap)
        if snap.get_children_count() > 0:
            snaps.extendleft(snap.children)
    
    while ordered_snaps:
        snap = ordered_snaps.popleft()
        progress = m.delete_snapshot(snap.id_p)
        progress.wait_for_completion(-1)
        try:
            session.unlock_machine()
        except:
            pass
    
if __name__ == "__main__":
    import sys
    import virtualbox as vb
    
    import time
    sys.coinit_flags = 0
    
    vbox = vb.VirtualBox()    
    vm = vbox.find_machine(sys.argv[1])
    snap = vm.find_snapshot(sys.argv[2])
    
    delete_vm_snap(vm, snap)
    

        
    