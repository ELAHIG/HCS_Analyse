from os import listdir
from os import path


# import HCS365 log file with axle and detection data
def find_hcs_logfiles():  
    hcs_logfile_path = './data/HCS'
    hcs_logfiles: list[str] = [path.join(hcs_logfile_path, file) for file in listdir(path=hcs_logfile_path) if file.endswith('.txt')]   
    return hcs_logfiles

def read_hcs_logfiles(file):
    for line in open(file, 'r'):
            
        # @Det: label represents a line with detection information
        start_line_with = ('@Det', '#Ax', '$VEH')
        if line.startswith(start_line_with):
            words = line.split()
            keys = []
            values = []
            for word in words:
                keys = []
                values = []
                    
    return words

hcs_logfiles = find_hcs_logfiles()
for file in hcs_logfiles:
    read_hcs_logfiles(file)