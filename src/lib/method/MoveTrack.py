import src.lib.handle.has as has
import src.lib.handle.lib as lib

def get_MoveTrack(dict):
    result_all = []
    if "st" not in dict:
        print("没有st")
        return None
    elif "et" not in dict:
        print("没有et")
        return None
    st = int(dict["st"])
    et = int(dict["et"])

    stg = has.has_num_e(dict, "stg", 0)
    etg = has.has_num_e(dict, "etg", 0)
    stg_t = has.has(dict, "stg_t", "ThisTile")
    etg_t = has.has(dict, "etg_t", "ThisTile")
    gl = has.has_num_e(dict, "gl", 0)
    ao = has.has_num_e(dict, "ao", 0)
    ea = has.has(dict, "ea", "Linear")
    ev = has.has(dict, "ev", "")

    if ea not in lib.ease_list:
        print("所写的ea没有在ADOFAI库里")
        return None

    if stg_t not in lib.tile_list:
        print("所写的stg_t没有在ADOFAI库里")
        return None

    if etg_t not in lib.tile_list:
        print("所写的etg_t没有在ADOFAI库里")
        return None

    floor = st

    while floor <= et:
        num = floor - st + 1
        du = has.has_num(dict, "du", 1, num)
        result = {"floor": floor, "eventType": "MoveTrack", "startTile": [stg, stg_t], "endTile": [etg, etg_t],
                  "gapLength": gl, "duration": du}

        if "pox" in dict or "poy" in dict:
            pox = has.has_num(dict, "pox", "null", num) if "pox" in dict else None
            poy = has.has_num(dict, "poy", "null", num) if "poy" in dict else None
            result["positionOffset"] = [pox, poy]

        if "ro" in dict:
            ro = has.has_num(dict, "ro", "null", num)
            result["rotationOffset"] = ro

        if "sx" in dict or "sy" in dict:
            sx = has.has_num(dict, "sx", "null", num) if "sx" in dict else None
            sy = has.has_num(dict, "sy", "null", num) if "sy" in dict else None
            result["scale"] = [sx, sy]

        if "op" in dict:
            op = has.has_num(dict, "op", "null", num)
            result["opacity"] = op

        result["angleOffset"] = ao
        result["ease"] = ea
        result["eventTag"] = ev

        result_all.append(result)
        floor += 1

    return result_all






