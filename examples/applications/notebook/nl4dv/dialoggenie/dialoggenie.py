from nl4dv.utils import constants, helpers
import re
import nltk
from nltk import word_tokenize
from si_prefix import si_parse
from nltk.corpus import stopwords
import copy



class DialogGenie:
    def __init__(self, nl4dv_instance):
        self.nl4dv_instance = nl4dv_instance
        self.previous_response = None

    def renew_fillter(self, current_response, mode = 'replace filter which has the same field'):
        previous_transform = copy.deepcopy(self.previous_response['visList'][0]['vlSpec']['transform'])
        current_transform = copy.deepcopy(current_response['visList'][0]['vlSpec']['transform'])
        if mode == 'just add filter':
            self.previous_response['visList'][0]['vlSpec']['transform'].extend(current_transform)
            return 

        elif mode == 'replace filter which has the same field':
            ft_pre = dict() # ft: field map to filter
            ft_cur = dict()
            for trans_pre in previous_transform:
                ft_pre[trans_pre['filter']['field']] = trans_pre
            for trans_cur in current_transform:
                if list(trans_cur.keys())[0] == 'filter':
                    ft_cur[trans_cur['filter']['field']] = trans_cur

            for field_cur in ft_cur:
                ft_pre[field_cur] = ft_cur[field_cur]
            self.previous_response['visList'][0]['vlSpec']['transform'] = list(ft_pre.values())
            return 

        elif mode == 'OR with fillter which has the same field':
            ft_pre = dict() # ft: field map to filter
            ft_cur = dict()
            for trans_pre in previous_transform:
                ft_pre[trans_pre['filter']['field']] = trans_pre
            for trans_cur in current_transform:
                if list(trans_cur.keys())[0] == 'filter':
                    ft_cur[trans_cur['filter']['field']] = trans_cur

            p_newed_by_c = copy.deepcopy(ft_pre)
            c_newed_by_p = copy.deepcopy(ft_cur)
            for field_cur in ft_cur:
                p_newed_by_c[field_cur] = ft_cur[field_cur]
            for field_pre in ft_pre:
                c_newed_by_p[field_pre] = ft_pre[field_pre]     

            for field in p_newed_by_c:
                  if(p_newed_by_c[field]['filter']['oneOf']!=c_newed_by_p[field]['filter']['oneOf']):
                      p_newed_by_c[field]['filter']['oneOf'].extend(c_newed_by_p[field]['filter']['oneOf'])
            self.previous_response['visList'][0]['vlSpec']['transform'] = list(p_newed_by_c.values())
            return            

        else:
            raise ValueError("bad mode")
