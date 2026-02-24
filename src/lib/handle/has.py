import re
import src.lib.handle.math

def has(dict, key, default):
    key_n = dict.get(key, default)
    return key_n

def has_num_e(dict, key, default):
    key_n = int(dict.get(key, default))
    return key_n

def has_num(dict, key, default, num):
    pattern_random = r'random_\[(-?\d+),(-?\d+)\]'
    pattern_recursion = r'recursion_\[(-?\d+),(-?\d+),(-?\d+)\]'
    pattern_recursion_d = r'recursion_d_\[(-?\d+),(-?\d+),(-?\d+)\]'
    key_n = dict.get(key, default)
    key_n_str = str(key_n)
    match_random = re.search(pattern_random,key_n_str)
    match_recursion = re.search(pattern_recursion,key_n_str)
    match_recursion_d = re.search(pattern_recursion_d, key_n_str)
    if match_random:
        key_n = src.lib.handle.math.random_n(
            int(match_random.group(1)),
            int(match_random.group(2))
        )
    elif match_recursion:
        key_n = src.lib.handle.math.recursion(
            int(match_recursion.group(1)),
            int(match_recursion.group(2)),
            int(match_recursion.group(3)),
            num
        )
    elif match_recursion_d:
        key_n = src.lib.handle.math.recursion_d(
            int(match_recursion.group(1)),
            int(match_recursion.group(2)),
            int(match_recursion.group(3)),
            num
        )

    return key_n

def has_str(dict, key, default, num):
    pattern_random = r'^(.+)_random_\[(-?\d+),(-?\d+)\]$'
    pattern_recursion = r'^(.+)_recursion_\[(-?\d+),(-?\d+),(-?\d+)\]$'
    pattern_recursion_d = r'^(.+)_recursion_d_\[(-?\d+),(-?\d+),(-?\d+)\]$'

    key_n = dict.get(key, default)
    key_n_str = str(key_n).strip()

    result = key_n_str

    match_random = re.search(pattern_random, key_n_str)
    if match_random:
        prefix = match_random.group(1)
        min_val = int(match_random.group(2))
        max_val = int(match_random.group(3))
        num_result = src.lib.handle.math.random_n(min_val, max_val)
        result = f"{prefix}_{num_result}"

    elif re.search(pattern_recursion, key_n_str):
        match_recursion = re.search(pattern_recursion, key_n_str)
        prefix = match_recursion.group(1)
        a = int(match_recursion.group(2))
        b = int(match_recursion.group(3))
        c = int(match_recursion.group(4))
        num_result = src.lib.handle.math.recursion(a, b, c, num)
        result = f"{prefix}_{num_result}"

    # 匹配recursion_d模式
    elif re.search(pattern_recursion_d, key_n_str):
        match_recursion_d = re.search(pattern_recursion_d, key_n_str)
        prefix = match_recursion_d.group(1)
        a = int(match_recursion_d.group(2))
        b = int(match_recursion_d.group(3))
        c = int(match_recursion_d.group(4))
        num_result = src.lib.handle.math.recursion_d(a, b, c, num)
        result = f"{prefix}_{num_result}"

    return result