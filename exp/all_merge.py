# all function run sequentially no delay
import sys

sys.path.append(".")
from exp.data import *

# calcualte the transmission for 10 functions
transition_fee = execution_time * transition_price * 2
single_exeuction_price = 0
single_execution_time=0
for func in fc_dict_x:
    assert fc_dict_x[func]["mem"] <= 256
    # if fc_dict_x[func]["mem"] <= 128:
    #     executed_memory = 128
    # else:
    executed_memory = 256
    T = fc_dict_x[func]["duration"]
    IO_time = (
        fc_dict_x[func]["IO"] * T
        - min(
            (executed_memory - fc_dict_x[func]["mem"]) / fc_dict_x[func]["mem"], 1 / 10
        )
        * fc_dict_x[func]["IO"]
        * T
    )
    cpu_time=T*(1-fc_dict_x[func]["IO"])*fc_dict_x[func]["duration"]/executed_memory
    executed_time=cpu_time+IO_time
    single_execution_time+=executed_time
    single_exeuction_price+=executed_time*single_price*executed_memory/1024
exeuction_price=single_exeuction_price*execution_time 
total_execution_time=single_execution_time*execution_time
price_all=exeuction_price+transition_fee
print("for 10 functions")
print("price_all",price_all)
print("single_execution_time",single_execution_time*1e-3)








transition_fee = execution_time * transition_price * 2
single_exeuction_price = 0
single_execution_time=0
for func in fc_dict_6:
    # assert fc_dict_6[func]["mem"] <= 256
    # if fc_dict_6[func]["mem"] <= 128:
    #     executed_memory = 128
    # else:
    executed_memory = 256
    T = fc_dict_6[func]["duration"]
    IO_time = (
        fc_dict_6[func]["IO"] * T
        - min(
            (executed_memory - fc_dict_6[func]["mem"]) / fc_dict_6[func]["mem"], 1 / 10
        )
        * fc_dict_6[func]["IO"]
        * T
    )
    cpu_time=T*(1-fc_dict_6[func]["IO"])*fc_dict_6[func]["duration"]/executed_memory
    executed_time=cpu_time+IO_time
    single_execution_time+=executed_time
    single_exeuction_price+=executed_time*single_price*executed_memory/1024
exeuction_price=single_exeuction_price*execution_time 
total_execution_time=single_execution_time*execution_time
price_all=exeuction_price+transition_fee
print("for 6 functions")
print("price_all",price_all)
print("single_execution_time",single_execution_time*1e-3)