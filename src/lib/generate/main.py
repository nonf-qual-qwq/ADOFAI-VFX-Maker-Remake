import json
import os
import src.lib.method.MoveTrack
import src.lib.method.MoveDecorations
import src.lib.method.AddDecoration

def get_action(json_str):
    data_dict = json.loads(json_str)
    action_results = []

    list_move_track = data_dict.get("MoveTrack", [])
    list_move_decorations = data_dict.get("MoveDecorations", [])


    for idx, single_track in enumerate(list_move_track):
        # 调用已有函数处理单个 MoveTrack
        processed_result = src.lib.method.MoveTrack.get_MoveTrack(single_track)
        # 将处理结果加入合并列表
        for item in processed_result:
            action_results.append(item)

    for idx, single_track in enumerate(list_move_decorations):
        # 调用已有函数处理单个 MoveDecorations
        processed_result = src.lib.method.MoveDecorations.get_MoveDecorations(single_track)
        # 将处理结果加入合并列表
        for item in processed_result:
            action_results.append(item)


    return action_results

def get_decoration(json_str):
    data_dict = json.loads(json_str)
    decoration_results = []

    list_add_decoration = data_dict.get("AddDecoration", [])

    for idx, single_track in enumerate(list_add_decoration):
        # 调用已有函数处理单个 AddDecoration
        processed_result = src.lib.method.AddDecoration.get_AddDecoration(single_track)
        # 将处理结果加入合并列表
        for item in processed_result:
            decoration_results.append(item)

    return decoration_results

def generate(at_file, adofai_file, adofai_file_path):

    adofai_data = json.loads(adofai_file)

    adofai_data["actions"].extend(get_action(at_file))
    adofai_data["decorations"].extend(get_decoration(at_file))


    output_dir = os.path.dirname(adofai_file_path)
    output_path = os.path.join(output_dir, "output.adofai")
    f_o = open(output_path, 'w+', encoding="utf-8")
    json.dump(adofai_data, f_o, ensure_ascii=False, indent=4)
    # f_o.write(str(adofai_data))
