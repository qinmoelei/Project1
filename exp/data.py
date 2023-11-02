import pandas as pd
import numpy as np
import os
#from the data, since the DAG is virtually made, we add a IO part indicating the time that IO takes
fc_dict_x={"f1":{"duration":30,"mem":150,"IO":0.6394267984578837},
         "f2":{"duration":30,"mem":92,"IO":0.025010755222666936},
         "f3":{"duration":15,"mem":195,"IO":0.27502931836911926},
         "f4":{"duration":769,"mem":114,"IO":0.22321073814882275},
         "f5":{"duration":26,"mem":117,"IO":0.7364712141640124},
         "f6":{"duration":335,"mem":179,"IO":0.6766994874229113},
         "f7":{"duration":8800,"mem":101,"IO": 0.8921795677048454},
         "f8":{"duration":2408,"mem":172,"IO":0.08693883262941615},
         "f9":{"duration":558,"mem":130,"IO":0.4219218196852704},
         "f10":{"duration":879,"mem":114,"IO": 0.029797219438070344},
         }


fc_dict_6={"fx1":{"duration":2660,"mem":133,"IO":0.21863797480360336},
         "fx2":{"duration":1010,"mem":174,"IO":0.5053552881033624},
         "fx3":{"duration":132,"mem":105,"IO":0.026535969683863625},
         "fx4":{"duration":1589,"mem":163,"IO":0.1988376506866485},
         "fx5":{"duration":3630,"mem":201,"IO": 0.6498844377795232},
         "fx6":{"duration":227,"mem":178,"IO":0.5449414806032167},
         }
#from the paper
execution_time=1e7
configure_memory=[128,256]
single_price=0.00001667
transition_price=0.000025
#assumption
#0.5 IO time 0.5 cpu time
#T=IO*T*selected_memory/memory+(1-IO)T-min((selected_memory-memory)/memory*T,1/10(1-IO)T)
