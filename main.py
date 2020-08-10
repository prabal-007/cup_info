import psutil

def cpu_info():
    print('='*20, 'CPU INformation', '='*20)
    print('Physical cores: ', psutil.cpu_count(Logical=False))
    print('Total copres: ', psutil.cpu_count(logical=True))

