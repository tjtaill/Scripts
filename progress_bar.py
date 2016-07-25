def progress_bar(minutes):
    from time import sleep
    from tqdm import tqdm
    
    seconds = minutes * 60
    for s in tqdm(range(seconds)):
        sleep(1)
    
def vm_progress_bar():
    progress_bar(3)
    
def group_progress_bar():
    progress_bar(7)
    
def restart_progress_bar():
    progress_bar(2)

if __name__ == "__main__":
    progress_bar(1)
