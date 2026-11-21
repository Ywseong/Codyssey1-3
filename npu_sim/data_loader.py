
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