import pandas as pd
import numpy as np
import os
import sys

sys.path.append(".")
from exp.data import *
from exp.optimze import calculate_price_time


def calculate_price_time_whole_process(function_list_list):
    single_execution_time = 0
    single_exeuction_price = 0
    num_function_list = len(function_list_list)
    single_exeuction_price += (num_function_list + 1) * transition_price
    for function_list in function_list_list:
        time, price = calculate_price_time(function_list)
        single_execution_time += time
        single_exeuction_price += price
    price_all = (single_exeuction_price) * execution_time
    single_execution_time = single_execution_time * 1e-3
    return price_all, single_execution_time


DAG1_graph_237_word = {
    "f2": {
        "f3": ["f3"],
        "f7": ["f3", "f7"],
    },
    "f3": {"f7": ["f7"]},
    "f7": {},
}


DAG1_graph_247_word = {
    "f2": {
        "f4": ["f4"],
        "f7": ["f4", "f7"],
    },
    "f4": {"f7": ["f7"]},
    "f7": {},
}


DAG1_graph_248_word = {
    "f2": {
        "f4": ["f4"],
        "f8": ["f4", "f8"],
    },
    "f4": {"f8": ["f8"]},
    "f8": {},
}

DAG1_graph_258_word = {
    "f2": {
        "f5": ["f5"],
        "f8": ["f5", "f8"],
    },
    "f5": {"f8": ["f8"]},
    "f8": {},
}

DAG1_graph_259_word = {
    "f2": {
        "f5": ["f5"],
        "f8": ["f5", "f9"],
    },
    "f5": {"f9": ["f9"]},
    "f9": {},
}

DAG1_graph_269_word = {
    "f2": {
        "f6": ["f6"],
        "f8": ["f6", "f9"],
    },
    "f6": {"f9": ["f9"]},
    "f9": {},
}


DAG1_graph_word = {
    "start": {
        "f1": ["f1"],
        "f2": ["f1", "f2"],
        "f3": ["f1", "f2", "f3"],
        "f4": ["f1", "f2", "f4"],
        "f5": ["f1", "f2", "f5"],
        "f6": ["f1", "f2", "f6"],
        "f7": ["f1", "f2", "f3", "f4", "f7"],
        "f8": ["f1", "f2", "f4", "f5", "f8"],
        "f9": ["f1", "f2", "f5", "f6", "f9"],
        "f10": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
    },
    "f1": {
        "f2": ["f2"],
        "f3": ["f2", "f3"],
        "f4": ["f2", "f4"],
        "f5": ["f2", "f5"],
        "f6": ["f2", "f6"],
        "f7": ["f2", "f3", "f4", "f7"],
        "f8": ["f2", "f5", "f4", "f8"],
        "f9": ["f2", "f5", "f6", "f9"],
        "f10": ["f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
    },
    "f2": {
        "f3": ["f3"],
        "f4": ["f4"],
        "f5": ["f5"],
        "f6": ["f6"],
        "f7": ["f3", "f4", "f7"],
        "f8": [
            "f4",
            "f5",
            "f8",
        ],
        "f9": [
            "f5",
            "f6",
            "f9",
        ],
        "f10": ["f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
    },
    "f3": {
        "f4": ["f4"],
        "f5": ["f5"],
        "f6": ["f6"],
        "f7": ["DAG1_graph_247_word"],
        "f8": [
            "f4",
            "f5",
            "f8",
        ],
        "f9": [
            "f5",
            "f6",
            "f9",
        ],
        "f10": ["f4", "f5", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f4", "f5", "f6", "f7", "f8", "f9", "f10"],
    },
    "f4": {
        "f3": ["f3"],
        "f5": ["f5"],
        "f6": ["f6"],
        "f7": ["DAG1_graph_237_word"],
        "f8": ["DAG1_graph_258_word"],
        "f9": [
            "f5",
            "f6",
            "f9",
        ],
        "f10": ["f3", "f5", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f3", "f5", "f6", "f7", "f8", "f9", "f10"],
    },
    "f5": {
        "f3": ["f3"],
        "f4": ["f4"],
        "f6": ["f6"],
        "f7": ["f3", "f4", "f7"],
        "f8": ["DAG1_graph_248_word"],
        "f9": ["DAG1_graph_269_word"],
        "f10": ["f3", "f4", "f6", "f7", "f8", "f9", "f10"],
        "end": ["f3", "f4", "f6", "f7", "f8", "f9", "f10"],
    },
    "f6": {
        "f3": ["f3"],
        "f4": ["f4"],
        "f5": ["f5"],
        "f7": ["f3", "f4", "f7"],
        "f8": ["f5", "f4", "f8"],
        "f9": ["DAG1_graph_259_word"],
        "f10": ["f3", "f4", "f5", "f7", "f8", "f9", "f10"],
        "end": ["f3", "f4", "f5", "f7", "f8", "f9", "f10"],
    },
    "f7": {
        "f8": ["DAG1_graph_258_word"],
        "f9": ["f5", "f6", "f9"],
        "f10": ["f5", "f6", "f8", "f9", "f10"],
        "end": ["f5", "f6", "f8", "f9", "f10"],
    },
    "f8": {
        "f7": ["DAG1_graph_237_word"],
        "f9": ["DAG1_graph_269_word"],
        "f10": ["f3", "f6", "f7", "f9", "f10"],
        "end": ["f3", "f6", "f7", "f9", "f10"],
    },
    "f9": {
        "f7": ["f3", "f4", "f7"],
        "f8": ["DAG1_graph_248_word"],
        "f10": ["f3", "f4", "f7", "f8", "f10"],
        "end": ["f3", "f4", "f7", "f8", "f10"],
    },
    "f10": {"end": {}},
    "end": {},
}


if __name__ == "__main__":
    # DAG1
    dag1_0 = ["start", "f3", "f7", "f10", "end"]
    dag1_7 = ["start", "f3", "f7", "end"]
    dag1_1 = ["start", "end"]
    # DAG2
    dag2_0 = ["start", "end"]
    dag2_1 = ["start", "end"]
    dag2_100000000 = ["start", "fx6", "end"]

    dag1_0_function = [
        [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f3"]],
        [fc_dict_x["f4"], fc_dict_x["f7"]],
        [
            fc_dict_x["f5"],
            fc_dict_x["f6"],
            fc_dict_x["f8"],
            fc_dict_x["f9"],
            fc_dict_x["f10"],
        ],
    ]

    price, time = calculate_price_time_whole_process(dag1_0_function)
    print("dag1_0_function", "price", price, "time", time)

    dag1_7_function = [
        [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f3"]],
        [fc_dict_x["f4"], fc_dict_x["f7"]],
        [
            fc_dict_x["f5"],
            fc_dict_x["f6"],
            fc_dict_x["f8"],
            fc_dict_x["f9"],
            fc_dict_x["f10"],
        ],
    ]
    price, time = calculate_price_time_whole_process(dag1_7_function)
    print("dag1_7_function", "price", price, "time", time)

    dag1_1_function = [
        [
            fc_dict_x["f1"],
            fc_dict_x["f2"],
            fc_dict_x["f3"],
            fc_dict_x["f4"],
            fc_dict_x["f7"],
            fc_dict_x["f5"],
            fc_dict_x["f6"],
            fc_dict_x["f8"],
            fc_dict_x["f9"],
            fc_dict_x["f10"],
        ]
    ]
    price, time = calculate_price_time_whole_process(dag1_1_function)
    print("dag1_1_function", "price", price, "time", time)

    dag2_0_function = [
        [
            fc_dict_6["fx1"],
            fc_dict_6["fx2"],
            fc_dict_6["fx3"],
            fc_dict_6["fx4"],
            fc_dict_6["fx5"],
            fc_dict_6["fx6"],
        ]
    ]
    price, time = calculate_price_time_whole_process(dag2_0_function)
    print("dag2_0_function", "price", price, "time", time)

    dag2_1_function = [
        [
            fc_dict_6["fx1"],
            fc_dict_6["fx2"],
            fc_dict_6["fx3"],
            fc_dict_6["fx4"],
            fc_dict_6["fx5"],
            fc_dict_6["fx6"],
        ]
    ]
    price, time = calculate_price_time_whole_process(dag2_1_function)
    print("dag2_1_function", "price", price, "time", time)
    dag2_100000000_function = [
        [fc_dict_6["fx1"], fc_dict_6["fx3"]],
        [fc_dict_6["fx2"], fc_dict_6["fx4"], fc_dict_6["fx5"], fc_dict_6["fx6"]],
    ]
    price, time = calculate_price_time_whole_process(dag2_100000000_function)
    print("dag2_100000000_function", "price", price, "time", time)
