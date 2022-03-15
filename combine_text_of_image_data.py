def drop_spaces_from_text(items):
    items_to_check = []
    combined_text = []

    for item in items:
        if item != "":
            combined_text.append(item)
        elif len(combined_text) != 0:
            concatenated_text = " ".join(combined_text)
            items_to_check.append(concatenated_text)
            combined_text.clear()
        else:
            continue
    if len(combined_text) != 0:
        concatenated_text = " ".join(combined_text)
        items_to_check.append(concatenated_text)

    return items_to_check