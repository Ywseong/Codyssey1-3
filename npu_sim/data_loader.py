from npu_sim.utils import split

LABEL_MAP = {
    "+": "Cross",
    "cross": "Cross",
    "x": "X",
}

def normalize_label(label):
    label = label.replace(" ", "").lower()
    if label in LABEL_MAP:
        return LABEL_MAP[label]
    return None

def get_size(key):
    try:
        split_key = split(key, "_")
        return int(split_key[1])
    except (ValueError, IndexError):
        return None

def normalize_filters(data):

    if "filters" not in data:
        return None
    
    new_filters = {}
    for size_key, filter_group in data["filters"].items():
        new_size = get_size(size_key)
        if new_size is not None:
            new_group = {}
            for label, matrix in filter_group.items():
                new_label = normalize_label(label)
                if new_label is not None:
                    new_group[new_label] = matrix
            new_filters[new_size] = new_group
            labels_text = ", ".join(new_group.keys())
            
            if "Cross" in new_group and "X" in new_group:
                print(f"✓ {size_key} 필터 로드 완료 ({labels_text})")
            else:
                print(f"⚠ {size_key} 필터 일부 누락 ({labels_text})")
    return new_filters
            
   
            