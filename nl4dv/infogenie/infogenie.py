from nl4dv.utils import constants, helpers
import copy



class InfoGenie:
    def __init__(self, nl4dv_instance):
        self.nl4dv_instance = nl4dv_instance
        self.info_hub = {}
        self.user_info_hub = {}
        self.user_info_list = []
        self.print_info = False
        self.print_user_info = True

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

    def user_info(self, info, type = 'undefined'):
        # if not self.user_info_hub[type]:
        #     self.user_info_hub[type] = []
        # self.user_info_hub[type].append({"type":type, "info":info})
        # self.user_info_list[type].apppend({"type":type, "info":info})
        #################ATTRIBUTE#################
        if type == 'Attribue implied by Query':
            for attr in info:
                temp_dict = {}
                temp_dict['type'] = type
                temp_dict['destType'] = 'Attribute'
                temp_dict['destKey'] = info[attr]['name']
                temp_dict['sourceType'] = 'Query'
                temp_dict['sourceKey'] = info[attr]['queryPhrase'][0]
                temp_dict['destOthers'] = None
                temp_dict['reason'] = 'by '+info[attr]['metric'][0]
                temp_dict['reason_score'] = info[attr]['matchScore']
                self.user_info_list.append(temp_dict)
        #################TASK######################
        elif type == 'Task extracted from dependency tree':
            for task_type in info:
                for task_instance in info[task_type]:
                    temp_dict = {}
                    temp_dict['type'] = type
                    temp_dict['destType'] = 'Task'
                    temp_dict['destKey'] = task_instance['task']
                    temp_dict['sourceType'] = 'Query'
                    temp_dict['sourceKey'] = task_instance['queryPhrase']
                    temp_dict['destOthers'] = {'operator':task_instance['operator'], 'values':task_instance['values'], 'attributes':task_instance['attributes']}
                    temp_dict['reason'] = 'by extracting task from dependency tree'
                    temp_dict['reason_score'] = task_instance['matchScore']
                    self.user_info_list.append(temp_dict)
        elif type == 'Task extracted from domain value match':
            for task_instance in info:
                temp_dict = {}
                temp_dict['type'] = type
                temp_dict['destType'] = 'Task'
                temp_dict['destKey'] = task_instance['task']
                temp_dict['sourceType'] = 'Query'
                temp_dict['sourceKey'] = task_instance['queryPhrase']
                temp_dict['destOthers'] = {'operator':task_instance['operator'], 'values':task_instance['values'], 'attributes':task_instance['attributes']}
                temp_dict['reason'] = 'by extracting task from domain value match'
                temp_dict['reason_score'] = task_instance['matchScore']
                self.user_info_list.append(temp_dict)
        elif type == 'Task implicitly inferred from attribute comb':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Task'
            temp_dict['destKey'] = info[0]['task']
            temp_dict['sourceType'] = 'Attribute Combo'
            temp_dict['sourceKey'] = info[1]
            temp_dict['destOthers'] = {'sorted_attr_datatype_combo_str':info[2], 'operator':info[0]['operator'], 'values':info[0]['values'], 'attributes':info[0]['attributes']}
            temp_dict['reason'] = 'because we know this attribute combination usually involved this kind of task'
            temp_dict['reason_score'] = 1
            self.user_info_list.append(temp_dict)
        #################VISUALIZATION#############
        elif type == 'Vis encoded by auto Attribute binding':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = 'channel '+info[0]
            temp_dict['sourceType'] = 'Attribute'
            temp_dict['sourceKey'] = info[1]
            temp_dict['destOthers'] = {'aggregation':info[2]}
            temp_dict['reason'] = 'by auto attribute binding'
            temp_dict['reason_score'] = 0.111222333
            info[3].append(temp_dict)
        elif type == 'Vistype chosen by attribute comb':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[0]
            temp_dict['sourceType'] = 'Attribute Combo'
            temp_dict['sourceKey'] = info[1]
            temp_dict['destOthers'] = None
            temp_dict['reason'] = 'because by design this vistype matches the given attribute combination well'
            temp_dict['reason_score'] = 0.111222333
            info[2].append(temp_dict) 
        elif type == 'Override vistype because of task':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[1]
            temp_dict['sourceType'] = 'Task'
            temp_dict['sourceKey'] = info[0]
            temp_dict['destOthers'] = None
            temp_dict['reason'] = 'becase this vistype can perform this task better'
            temp_dict['reason_score'] = 0.444555666
            info[2].append(temp_dict)
        elif type == 'Override aggregation because of task':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[1] + " axis's aggregation"
            temp_dict['sourceType'] = 'Task'
            temp_dict['sourceKey'] = info[0]
            temp_dict['destOthers'] = info[2]
            temp_dict['reason'] = 'since to perform this task, we should change the original aggregation to this new one'
            temp_dict['reason_score'] = 0.444555666
            info[3].append(temp_dict)
        elif type == 'Sort one dimension because of task':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[1] + " axis sorted"
            temp_dict['sourceType'] = 'Task'
            temp_dict['sourceKey'] = info[0]
            temp_dict['destOthers'] = None
            temp_dict['reason'] = 'since to perform this task, we need to sort this dimension based on the attribute of another dimension'
            temp_dict['reason_score'] = 0.444555666
            info[2].append(temp_dict)            
        elif type == 'Vis mandatory channel encoded by another channel':
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[0]
            temp_dict['sourceType'] = 'Attribute'
            temp_dict['sourceKey'] = info[1]
            temp_dict['destOthers'] = {'aggregation':info[2]}
            temp_dict['reason'] = "since this channel must be encoded but we don't have enough attributes"
            temp_dict['reason_score'] = 0.111222333
            info[3].append(temp_dict)   
        elif type == "Final choice of vistype based on query":
            temp_dict = {}
            temp_dict['type'] = type
            temp_dict['destType'] = 'Visualization'
            temp_dict['destKey'] = info[0]
            temp_dict['sourceType'] = 'Query'
            temp_dict['sourceKey'] = info[1]
            temp_dict['destOthers'] = None
            temp_dict['reason'] = "becase we let the user make the final decision"
            temp_dict['reason_score'] = 0.7778888999
            info[2].append(temp_dict)   
        else:
            print("\033[0;30;47m"+type+": "+info+"\033[0m")   
    def user_info_show(self):
        for u_i in self.user_info_list:
            if u_i['type'][0:5] == "Final":
                print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is decided by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m ("+str(u_i['destOthers'])+")")
            elif u_i['type'][0:8] == "Override":
                print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is used to override the original one due to "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m ("+str(u_i['destOthers'])+")") 
            else:
                print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is implied by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m ("+str(u_i['destOthers'])+")") 
            # if u_i['type'] == 'Attribue implied by Query':
            #     print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is implied by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m") 
            # elif u_i['type'] == 'Task extracted from dependency tree':
            #     print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is implied by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m("+str(u_i['destOthers'])+")") 
            # elif u_i['type'] == 'Vis encoded by auto Attribute binding':
            #     print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is implied by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m("+str(u_i['destOthers'])+")") 
            # elif u_i['type'] == 'Override vistype because of task':
            #     print("\033[0;32;47m"+str(u_i['destType'])+"\033[0m \033[1;32;47m" + str(u_i['destKey']) + "\033[0m is implied by "+"\033[0;32;47m"+str(u_i['sourceType'])+"\033[0m \033[1;32;47m" + str(u_i['sourceKey']) + "\033[0m, "+"\033[1;32;47m"+str(u_i['reason'])+"\033[0m("+str(u_i['destOthers'])+")")                  


        
