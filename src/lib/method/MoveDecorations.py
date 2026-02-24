import src.lib.handle.has as has
import src.lib.handle.lib as lib

def get_MoveDecorations(dict):
    result_all = []
    if "num" not in dict:
        print("没有num")
        return None
    if "fl" not in dict:
        print("没有fl")
        return None
    num = int(dict["num"])
    fl = dict["fl"]

    ao = has.has_num_e(dict, "ao", 0)
    ea = has.has(dict, "ea", "Linear")
    ev = has.has(dict, "ev", "")

    i = 1

    while i <= num:
        du = has.has_num(dict, "du", 1, i)
        result = {"floor": fl, "eventType": "MoveDecorations", "duration": du}

        tag_t = dict.get("tag_t", "")
        tag_s = has.has_str(dict, "tag_s", "sampleTag", i) if "tag_s" in dict else ""
        tag_parts = []
        if tag_t:
            tag_parts.append(tag_t)
        if tag_s:
            tag_parts.append(tag_s)
        result["tag"] = " ".join(tag_parts) if tag_parts else "sampleTag"

        if "vis" in dict:
            vis = dict["vis"]
            if vis not in lib.bool_list:
                print("所写的vis没有在ADOFAI库里")
                return None
            else:
                result["visible"] = bool(vis)

        if "rt" in dict:
            rt = dict["rt"]
            if rt not in lib.relative_to_list:
                print("所写的rt没有在ADOFAI库里")
                return None
            else:
                result["relativeTo"] = rt

        if "di" in dict:
            di = dict["di"]
            result["decorationImage"] = di

        if "pox" in dict or "poy" in dict:
            pox = has.has_num(dict, "pox", "null", num) if "pox" in dict else None
            poy = has.has_num(dict, "poy", "null", num) if "poy" in dict else None
            result["positionOffset"] = [pox, poy]

        if "pix" in dict or "piy" in dict:
            pix = has.has_num(dict, "pix", "null", num) if "pix" in dict else None
            piy = has.has_num(dict, "piy", "null", num) if "piy" in dict else None
            result["pivotOffset"] = [pix, piy]

        if "ro" in dict:
            ro = has.has_num(dict, "ro", "null", num)
            result["rotationOffset"] = ro

        if "sx" in dict or "sy" in dict:
            sx = has.has_num(dict, "sx", "null", num) if "sx" in dict else None
            sy = has.has_num(dict, "sy", "null", num) if "sy" in dict else None
            result["scale"] = [sx, sy]

        if "c" in dict:
            c = dict["c"]
            result["color"] = c

        if "op" in dict:
            op = has.has_num(dict, "op", "100", num)
            result["opacity"] = op

        if "d" in dict:
            d = has.has_num(dict, "d", "-1", num)
            result["depth"] = d

        if "px" in dict or "py" in dict:
            px = has.has_num(dict, "px", "null", num) if "px" in dict else None
            py = has.has_num(dict, "py", "null", num) if "py" in dict else None
            result["parallax"] = [px, py]

        if "pax" in dict or "pay" in dict:
            pax = has.has_num(dict, "pax", "null", num) if "pax" in dict else None
            pay = has.has_num(dict, "pay", "null", num) if "pay" in dict else None
            result["parallaxOffset"] = [pax, pay]

        result["angleOffset"] = ao
        result["ease"] = ea
        result["eventTag"] = ev

        if "mt" in dict:
            mt = dict["mt"]
            if mt not in lib.masking_type_list:
                print("所写的mt没有在ADOFAI库里")
                return None
            else:
                result["maskingType"] = mt

        if "umd" in dict:
            umd = dict["umd"]
            if umd not in lib.bool_list:
                print("所写的umd没有在ADOFAI库里")
                return None
            else:
                result["useMaskingDepth"] = bool(umd)

        if "mfd" in dict:
            mfd = has.has_num(dict, "mfd", "-1", num)
            result["maskingFrontDepth"] = mfd

        if "mbd" in dict:
            mbd = has.has_num(dict, "mbd", "-1", num)
            result["maskingBackDepth"] = mbd

        result_all.append(result)
        i += 1

    return result_all