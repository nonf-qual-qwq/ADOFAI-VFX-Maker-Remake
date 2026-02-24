import src.lib.handle.has as has
import src.lib.handle.lib as lib

def get_AddDecoration(dict):
    result_all = []
    if "num" not in dict:
        print("没有num")
        return None
    num = int(dict["num"])

    i = 1
    while i <= num:
        fl = has.has_num(dict, "fl", 0, num)
        di = has.has_str(dict, "di", "", num)
        tag_t = dict.get("tag_t", "")
        tag_s = has.has_str(dict, "tag_s", "sampleTag", i) if "tag_s" in dict else ""
        tag_parts = []
        if tag_t:
            tag_parts.append(tag_t)
        if tag_s:
            tag_parts.append(tag_s)

        pox = has.has_num(dict, "pox", 0, num) if "pox" in dict else 0
        poy = has.has_num(dict, "poy", 0, num) if "poy" in dict else 0

        result = {
            "floor": fl,
            "eventType": "AddDecoration",
            "decorationImage": di,
            "tag": " ".join(tag_parts) if tag_parts else "",
            "positionOffset" : [pox, poy]
                  }

        rt = has.has_str(dict, "rt", "Global", num)
        if rt not in lib.relative_to_list:
            print("所写的rt没有在ADOFAI库里")
            return None
        else:
            result["relativeTo"] = rt

        stf = bool(has.has(dict, "stf", "false"))
        result["stickToFloor"] = stf

        pix = has.has_num(dict, "pix", 0, num)
        piy = has.has_num(dict, "piy", 0, num)
        result["pivotOffset"] = [pix, piy]

        ro = has.has_num(dict, "ro", 0, num)
        result["rotationOffset"] = ro

        lr = bool(has.has(dict, "lr", "false"))
        result["lockRotation"] = lr

        sx = has.has_num(dict, "sx", 100, num)
        sy = has.has_num(dict, "sy", 100, num)
        result["scale"] = [sx, sy]

        ls = bool(has.has(dict, "ls", "false"))
        result["lockScale"] = ls

        tx = has.has_num(dict, "tx", 1, num)
        ty = has.has_num(dict, "ty", 1, num)
        result["tile"] = [tx, ty]

        c = has.has(dict, "c", "ffffffff")
        result["color"] = c

        op = has.has_num(dict, "op", 100, num)
        result["opacity"] = op

        d = has.has_num(dict, "d", -1, num)
        result["depth"] = d

        sfd = bool(has.has(dict, "sfd", "false"))
        result["syncFloorDepth"] = sfd

        px = has.has_num(dict, "px", 0, num)
        py = has.has_num(dict, "py", 0, num)
        result["parallax"] = [px, py]

        pax = has.has_num(dict, "pax", 0, num)
        pay = has.has_num(dict, "pay", 0, num)
        result["parallaxOffset"] = [pax, pay]

        ims = bool(has.has(dict, "ims", "false"))
        result["imageSmoothing"] = ims

        bm = has.has_str(dict, "bm", "None", num)
        if bm not in lib.blend_mode_list:
            print("所写的bm没有在ADOFAI库里")
            return None
        else:
            result["blendMode"] = bm

        mt = has.has_str(dict, "mt", "None", num)
        if mt not in lib.masking_type_list:
            print("所写的mt没有在ADOFAI库里")
            return None
        else:
            result["maskingType"] = mt

        umd = bool(has.has(dict, "umd", "false"))
        result["useMaskingDepth"] = umd

        mfd = has.has_num(dict, "mfd", -1, num)
        result["maskingFrontDepth"] = mfd

        mbd = has.has_num(dict, "mbd", -1, num)
        result["maskingBackDepth"] = mbd

        hb = has.has_str(dict, "hb", "None", num)
        if hb not in lib.hit_box_list:
            print("所写的hb没有在ADOFAI库里")
            return None
        else:
            result["hitbox"] = hb

        hbt = has.has_str(dict, "hbt", "Once", num)
        if hbt not in lib.hit_box_trigger_type_list:
            print("所写的hbt没有在ADOFAI库里")
            return None
        else:
            result["hitboxTriggerType"] = hbt

        hbr = has.has_num(dict, "hbr", 1000, num)
        result["hitboxRepeatInterval"] = hbr

        hbe = has.has_str(dict, "hbe", "", num)
        result["hitboxEventTag"] = hbe

        hbd = has.has_str(dict, "hbd", "Planet", num)
        if hbd not in lib.hit_box_detect_target_list:
            print("所写的hbd没有在ADOFAI库里")
            return None
        else:
            result["hitboxDetectTarget"] = hbd

        hbtp = has.has_str(dict, "hbtp", "Any", num)
        if hbtp not in lib.hit_box_target_planet_list:
            print("所写的hbtp没有在ADOFAI库里")
            return None
        else:
            result["hitboxTargetPlanet"] = hbtp

        hbdt = has.has_str(dict, "hbdt", "", num)
        result["hitboxDecoTag"] = hbdt

        fht = has.has_str(dict, "fht", "Box", num)
        if fht not in lib.fail_hit_box_type_list:
            print("所写的fht没有在ADOFAI库里")
            return None
        else:
            result["failHitboxType"] = fht

        fhx = has.has_num(dict, "fhx", 100, num)
        fhy = has.has_num(dict, "fhy", 100, num)
        result["failHitboxScale"] = [fhx, fhy]

        fox = has.has_num(dict, "fox", 0, num)
        foy = has.has_num(dict, "foy", 0, num)
        result["failHitboxOffset"] = [fox, foy]

        fhr = has.has_num(dict, "fhr", 0, num)
        result["failHitboxRotation"] = fhr

        result_all.append(result)
        i += 1

    return result_all