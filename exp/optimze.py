import sys

sys.path.append(".")

from exp.data import *
import heapq


def calculate_price_time(function_list):
    # calculate single exectuion price and time
    # function should be a dict like this [{"duration":2660,"mem":133,"IO":0.21863797480360336},...]
    mem_list = [func["mem"] for func in function_list]
    mem = max(mem_list)
    assert mem <= 256
    if mem <= 128:
        executed_memory = 128
    else:
        executed_memory = 256
    all_time = 0
    for func in function_list:
        T = func["duration"]
        IO_time = (
            func["IO"] * T
            - min((executed_memory - func["mem"]) / func["mem"], 1 / 10)
            * func["IO"]
            * T
        )
        cpu_time = T * (1 - func["IO"]) * func["duration"] / executed_memory
        executed_time = cpu_time + IO_time
        all_time += executed_time
    return all_time, all_time * single_price * executed_memory / 1024


def calculate_target(time, price, lada=1e-7):
    # print(lada*time,price)
    return lada * time + price


def calculate_merge_distance(function_list, lada=1e-7):
    time, price = calculate_price_time(function_list)
    return calculate_target(time, price, lada=lada)


def dijkstra(graph, start):
    shortest_path = {vertex: float("infinity") for vertex in graph}
    shortest_path[start] = 0
    priority_queue = [(0, start)]
    # 添加前驱字典来保存路径
    predecessors = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_path[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                # 当我们找到一个更短的路径时，更新前驱
                predecessors[neighbor] = current_vertex

    return shortest_path, predecessors


def get_shortest_path(predecessors, start, end):
    path = []
    while end:
        path.append(end)
        end = predecessors[end]
    path.reverse()  # 从起点到终点
    return path


# 示例图


# calculate the result for DAG1
def calculate_merge_function_DAG1(fc_dict_x, lada=1e-7):
    graph_237 = {
        "f2": {
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f3"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance([fc_dict_x["f3"], fc_dict_x["f7"]], lada=lada),
        },
        "f3": {
            "f7": transition_price
            + calculate_merge_distance([fc_dict_x["f7"]], lada=lada)
        },
        "f7": {},
    }
    shortest_distances_237, predecessors_237 = dijkstra(graph_237, "f2")
    shortest_distances_237 = shortest_distances_237["f7"]
    # print(get_shortest_path(predecessors_237, "f2", "f7"))
    graph_247 = {
        "f2": {
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance([fc_dict_x["f4"], fc_dict_x["f7"]], lada=lada),
        },
        "f4": {
            "f7": transition_price
            + calculate_merge_distance([fc_dict_x["f7"]], lada=lada)
        },
        "f7": {},
    }
    shortest_distances_247, predecessors_247 = dijkstra(graph_247, "f2")
    print("get_247", get_shortest_path(predecessors_247, "f2", "f7"))

    shortest_distances_247 = shortest_distances_247["f7"]

    graph_248 = {
        "f2": {
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f8": transition_price
            + calculate_merge_distance([fc_dict_x["f4"], fc_dict_x["f8"]], lada=lada),
        },
        "f4": {
            "f8": transition_price
            + calculate_merge_distance([fc_dict_x["f8"]], lada=lada)
        },
        "f8": {},
    }
    shortest_distances_248, predecessors_248 = dijkstra(graph_248, "f2")
    print("get_248", get_shortest_path(predecessors_248, "f2", "f8"))
    shortest_distances_248 = shortest_distances_248["f8"]

    graph_258 = {
        "f2": {
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f8": transition_price
            + calculate_merge_distance([fc_dict_x["f5"], fc_dict_x["f8"]], lada=lada),
        },
        "f5": {
            "f8": transition_price
            + calculate_merge_distance([fc_dict_x["f8"]], lada=lada)
        },
        "f8": {},
    }
    shortest_distances_258, predecessors_258 = dijkstra(graph_258, "f2")
    print("get_258", get_shortest_path(predecessors_258, "f2", "f8"))
    shortest_distances_258 = shortest_distances_258["f8"]

    graph_259 = {
        "f2": {
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f9": transition_price
            + calculate_merge_distance([fc_dict_x["f5"], fc_dict_x["f9"]], lada=lada),
        },
        "f5": {
            "f9": transition_price
            + calculate_merge_distance([fc_dict_x["f9"]], lada=lada)
        },
        "f9": {},
    }
    shortest_distances_259, predecessors_259 = dijkstra(graph_259, "f2")
    print("get_259", get_shortest_path(predecessors_259, "f2", "f9"))
    shortest_distances_259 = shortest_distances_259["f9"]
    graph_269 = {
        "f2": {
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f6"]], lada=lada),
            "f9": transition_price
            + calculate_merge_distance([fc_dict_x["f6"], fc_dict_x["f9"]], lada=lada),
        },
        "f6": {
            "f9": transition_price
            + calculate_merge_distance([fc_dict_x["f9"]], lada=lada)
        },
        "f9": {},
    }
    shortest_distances_269, predecessors_269 = dijkstra(graph_269, "f2")
    print("get_269", get_shortest_path(predecessors_269, "f2", "f9"))
    shortest_distances_269 = shortest_distances_269["f9"]
    graph = {
        "start": {
            "f1": transition_price
            + calculate_merge_distance([fc_dict_x["f1"]], lada=lada),
            "f2": transition_price
            + calculate_merge_distance([fc_dict_x["f1"], fc_dict_x["f2"]], lada=lada),
            "f3": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f3"]], lada=lada
            ),
            "f4": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f4"]], lada=lada
            ),
            "f5": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f5"]], lada=lada
            ),
            "f6": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f1"], fc_dict_x["f2"], fc_dict_x["f6"]], lada=lada
            ),
            "f7": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f1"],
                    fc_dict_x["f2"],
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f7"],
                ],
                lada=lada,
            ),
            "f8": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f1"],
                    fc_dict_x["f2"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f8"],
                ],
                lada=lada,
            ),
            "f9": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f1"],
                    fc_dict_x["f2"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f9"],
                ],
                lada=lada,
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f1"],
                    fc_dict_x["f2"],
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f1"],
                    fc_dict_x["f2"],
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f1": {
            "f2": transition_price
            + calculate_merge_distance([fc_dict_x["f2"]], lada=lada),
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f2"], fc_dict_x["f3"]], lada=lada),
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f2"], fc_dict_x["f4"]], lada=lada),
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f2"], fc_dict_x["f5"]], lada=lada),
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f2"], fc_dict_x["f6"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f2"], fc_dict_x["f3"], fc_dict_x["f4"], fc_dict_x["f7"]],
                lada=lada,
            ),
            "f8": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f2"], fc_dict_x["f5"], fc_dict_x["f4"], fc_dict_x["f8"]],
                lada=lada,
            ),
            "f9": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f2"], fc_dict_x["f5"], fc_dict_x["f6"], fc_dict_x["f9"]],
                lada=lada,
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f2"],
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f2"],
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f2": {
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f3"]], lada=lada),
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f6"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f3"], fc_dict_x["f4"], fc_dict_x["f7"]], lada=lada
            ),
            "f8": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f5"], fc_dict_x["f4"], fc_dict_x["f8"]], lada=lada
            ),
            "f9": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f5"], fc_dict_x["f6"], fc_dict_x["f9"]], lada=lada
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f3": {
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f6"]], lada=lada),
            "f7": transition_price + shortest_distances_247,
            "f8": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f4"], fc_dict_x["f5"], fc_dict_x["f8"]], lada=lada
            ),
            "f9": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f5"], fc_dict_x["f6"], fc_dict_x["f9"]], lada=lada
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f4": {
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f3"]], lada=lada),
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f6"]], lada=lada),
            "f7": transition_price + shortest_distances_237,
            "f8": transition_price + shortest_distances_258,
            "f9": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f5"], fc_dict_x["f6"], fc_dict_x["f9"]], lada=lada
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f5": {
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f3"]], lada=lada),
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f6": transition_price
            + calculate_merge_distance([fc_dict_x["f6"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f3"], fc_dict_x["f4"], fc_dict_x["f7"]], lada=lada
            ),
            "f8": transition_price + shortest_distances_248,
            "f9": transition_price + shortest_distances_269,
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f6": {
            "f3": transition_price
            + calculate_merge_distance([fc_dict_x["f3"]], lada=lada),
            "f4": transition_price
            + calculate_merge_distance([fc_dict_x["f4"]], lada=lada),
            "f5": transition_price
            + calculate_merge_distance([fc_dict_x["f5"]], lada=lada),
            "f7": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f3"], fc_dict_x["f4"], fc_dict_x["f7"]], lada=lada
            ),
            "f8": transition_price
            + calculate_merge_distance(
                [fc_dict_x["f5"], fc_dict_x["f4"], fc_dict_x["f8"]], lada=lada
            ),
            "f9": transition_price + shortest_distances_259,
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f5"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f7": {
            "f8": transition_price + shortest_distances_258,
            "f9": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f9"],
                ],
                lada=lada,
            ),
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f5"],
                    fc_dict_x["f6"],
                    fc_dict_x["f8"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f8": {
            "f7": transition_price + shortest_distances_237,
            "f9": transition_price + shortest_distances_269,
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f6"],
                    fc_dict_x["f7"],
                    fc_dict_x["f9"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f9": {
            "f7": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f7"],
                ],
                lada=lada,
            ),
            "f8": transition_price + shortest_distances_248,
            "f10": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_x["f3"],
                    fc_dict_x["f4"],
                    fc_dict_x["f7"],
                    fc_dict_x["f8"],
                    fc_dict_x["f10"],
                ],
                lada=lada,
            ),
        },
        "f10": {"end": transition_price},
        "end": {},
    }
    shortest_distances, predecessors = dijkstra(graph, "start")
    print(shortest_distances)
    print(get_shortest_path(predecessors, "start", "end"))


def calculate_merge_function_DAG2(fc_dict_6, lada=1e-7):
    print(fc_dict_6)
    graph_1246 = {
        "fx1": {
            "fx2": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"], fc_dict_6["fx4"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance(
                [fc_dict_6["fx2"], fc_dict_6["fx4"], fc_dict_6["fx6"]], lada=lada
            ),
        },
        "fx2": {
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx4"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance([fc_dict_6["fx4"], fc_dict_6["fx6"]], lada=lada),
        },
        "fx4": {
            "fx6": transition_price
            + calculate_merge_distance([fc_dict_6["fx6"]], lada=lada),
        },
        "fx6": {},
    }
    shortest_distances_1246, predecessors_1246 = dijkstra(graph_1246, "fx1")
    shortest_distances_1246 = shortest_distances_1246["fx6"]

    graph_1356 = {
        "fx1": {
            "fx3": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"]], lada=lada),
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"], fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance(
                [fc_dict_6["fx3"], fc_dict_6["fx5"], fc_dict_6["fx6"]], lada=lada
            ),
        },
        "fx3": {
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance([fc_dict_6["fx5"], fc_dict_6["fx6"]], lada=lada),
        },
        "fx5": {
            "fx6": transition_price
            + calculate_merge_distance([fc_dict_6["fx6"]], lada=lada),
        },
        "fx6": {},
    }
    shortest_distances_1356, predecessors_1356 = dijkstra(graph_1356, "fx1")
    shortest_distances_1356 = shortest_distances_1356["fx6"]

    graph = {
        "start": {
            "fx1": transition_price
            + calculate_merge_distance([fc_dict_6["fx1"]], lada=lada),
            "fx2": transition_price
            + calculate_merge_distance([fc_dict_6["fx1"], fc_dict_6["fx2"]], lada=lada),
            "fx3": transition_price
            + calculate_merge_distance([fc_dict_6["fx1"], fc_dict_6["fx3"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance(
                [fc_dict_6["fx1"], fc_dict_6["fx2"], fc_dict_6["fx4"]], lada=lada
            ),
            "fx5": transition_price
            + calculate_merge_distance(
                [fc_dict_6["fx1"], fc_dict_6["fx3"], fc_dict_6["fx5"]], lada=lada
            ),
            "fx6": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx1"],
                    fc_dict_6["fx2"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx1"],
                    fc_dict_6["fx2"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx1": {
            "fx2": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"]], lada=lada),
            "fx3": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"], fc_dict_6["fx4"]], lada=lada),
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"], fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx2"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx2"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx2": {
            "fx3": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx4"]], lada=lada),
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"], fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx4"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx4"],
                    fc_dict_6["fx3"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx4": {
            "fx3": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"]], lada=lada),
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx3"], fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price + shortest_distances_1356,
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx3"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx3": {
            "fx2": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"], fc_dict_6["fx4"]], lada=lada),
            "fx5": transition_price
            + calculate_merge_distance([fc_dict_6["fx5"]], lada=lada),
            "fx6": transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx2"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx2"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx5"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx5": {
            "fx2": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"]], lada=lada),
            "fx4": transition_price
            + calculate_merge_distance([fc_dict_6["fx2"], fc_dict_6["fx4"]], lada=lada),
            "fx6": transition_price + shortest_distances_1246,
            "end": 2 * transition_price
            + calculate_merge_distance(
                [
                    fc_dict_6["fx2"],
                    fc_dict_6["fx4"],
                    fc_dict_6["fx6"],
                ],
                lada=lada,
            ),
        },
        "fx6": {"end": transition_price},
        "end": {},
    }
    shortest_distances, predecessors = dijkstra(graph, "start")
    print(shortest_distances)
    print(get_shortest_path(predecessors, "start", "end"))


if __name__ == "__main__":
    # TODO add different lada to see how the merge result varies
    # graph = {
    #     "A": {"B": 1, "C": 4},
    #     "B": {"C": 2, "D": 5},
    #     "C": {"B": 2, "D": 1},
    #     # "D": {"B": 5, "C": 1},
    #     "D": {},
    # }
    # shortest_distances, predecessors = dijkstra(graph, "A")
    # print(shortest_distances)
    # print(get_shortest_path(predecessors, "A", "D"))

    # graph_237 = {
    #     "f2": {
    #         "f3": transition_price + calculate_merge_distance([fc_dict_x["f3"]]),
    #         "f7": transition_price
    #         + calculate_merge_distance([fc_dict_x["f3"], fc_dict_x["f7"]]),
    #     },
    #     "f3": {"f7": transition_price + calculate_merge_distance([fc_dict_x["f7"]])},
    #     "f7":{}
    # }
    # shortest_distances_237, predecessors_237 = dijkstra(graph_237, "f2")
    # print(shortest_distances_237)
    print("DAG1")
    print("lada=0")
    calculate_merge_function_DAG1(fc_dict_x, lada=0)
    print("lada=1e-7")
    calculate_merge_function_DAG1(fc_dict_x, lada=1e-7)
    print("lada=1")
    calculate_merge_function_DAG1(fc_dict_x, lada=1)

    print("DAG2")
    print("lada=0")
    calculate_merge_function_DAG2(fc_dict_6, lada=0)
    print("lada=1")
    calculate_merge_function_DAG2(fc_dict_6, lada=1)
    print("lada=10")
    calculate_merge_function_DAG2(fc_dict_6, lada=10)
