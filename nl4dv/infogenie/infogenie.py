from nl4dv.utils import constants, helpers
import copy



class InfoGenie:
    def __init__(self, nl4dv_instance):
        self.nl4dv_instance = nl4dv_instance
        self.info_hub = {}
        self.print_info = True

    def push_info(self, info, type = 'undefined'):
        self.info_hub[type] = {"type":type, "info":info} 
        if self.print_info:
            if type == 'user_error':
                print("\033[0;31;47m"+type+": "+info+"\033[0m")  
            else:
                print("\033[0;30;47m"+type+": "+info+"\033[0m")  
        
