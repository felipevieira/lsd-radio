import os
import vote_queue, scratch_queue
import time
from radio_config import ICES_PIPE

def ices_get_next():
    
    while (True) :
        file_path = vote_queue.get_next()
        if (not file_path) :
            file_path = scratch_queue.get_next()
        
        pipe = open(ICES_PIPE, 'w')
        pipe.write('1')
        pipe.close()
        
        if (file_path is not None) :
            return file_path
        
        time.sleep(5)