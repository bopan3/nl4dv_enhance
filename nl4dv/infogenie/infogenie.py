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
            elif type == 'attribute info':
                print("\033[0;32;47m"+type+": "+"\033[0m") 
                for keyword in info[1]:
                    print("\033[0;32;47m"+"for keyword "+keyword+", it maps to the following "+str(len(info[1][keyword]))+ " attribute:"+"\033[0m")  
                    for attr in info[1][keyword]:
                        print("\033[1;32;47m  "+attr+"("+self.nl4dv_instance.data_genie_instance.data_attribute_map[attr]['dataType']+")\033[0m\033[0;32;47m: matchScore = "+str(info[0][attr]['matchScore'])+", metric = "+str(info[0][attr]['metric']) + "\033[0m")
            elif type == "task info (explicit 'dependency analysis' task)":
                print("\033[0;32;47m"+type+": "+"\033[0m") 
                for task_type in info:
                    print("\033[0;32;47m"+"for task type "+task_type+", it has the following "+str(len(info[task_type]))+ " task instance:"+"\033[0m")  
                    for task_instance in info[task_type]:
                        print("\033[1;32;47m  "+task_instance['task']+"(queryPhrase == "+str(task_instance['queryPhrase'])+")\033[0m\033[0;32;47m: matchScore = "\
                             +str(task_instance['matchScore'])+", attributes = "+str(task_instance['attributes']) + ", operator = "+\
                             str(task_instance['operator']) + ", values = "+str(task_instance['values'])+"\033[0m")
            elif type == "task info (explicit 'domain_value' task)":
                print("\033[0;32;47m"+type+": "+"\033[0m") 
                for task_instance in info:
                    print("\033[1;32;47m  "+task_instance['task']+"(queryPhrase == "+str(task_instance['queryPhrase'])+")\033[0m\033[0;32;47m: matchScore = "\
                         +str(task_instance['matchScore'])+", attributes = "+str(task_instance['attributes']) + ", operator = "+\
                         str(task_instance['operator']) + ", values = "+str(task_instance['values'])+"\033[0m")            
            elif type == "task info (implicit guess)":
                print("\033[0;32;47m"+type+": "+"\033[0m") 
                print("\033[1;32;47m  "+info['task']+"(queryPhrase == "+str(info['queryPhrase'])+")\033[0m\033[0;32;47m: matchScore = "\
                     +str(info['matchScore'])+", attributes = "+str(info['attributes']) + ", operator = "+\
                     str(info['operator']) + ", values = "+str(info['values'])+"\033[0m")       
            else:
                print("\033[0;30;47m"+type+": "+info+"\033[0m")  
        
