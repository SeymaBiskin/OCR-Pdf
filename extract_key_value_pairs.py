
def extract_key_value_pair(zipped, key_coordinates, value_coordinates):

    keys = []
    values = []

    for (left, text) in zipped:
        if left >= key_coordinates["lower"] and left <= key_coordinates["upper"]:
            keys.append(text)
        elif left >= value_coordinates["lower"] and left <= value_coordinates["upper"]:
            values.append(text)
        else:
            continue
    return keys, values