def shorten_path(path):
    temp_count = 0
    index_offset = 0
    new_list = []

    for index in range(len(path)):
        if index + index_offset >= len(path):
            break

        item = path[index + index_offset]
        print(item)
        temp_count += 1
        while index + index_offset < len(path) and path[index + index_offset] == item:
            # print(path[index + index_offset])
            temp_count += 1
            index_offset += 1
        new_list.append(f"{path[index]} {temp_count}")
        temp_count = 0

    return new_list


print(shorten_path(["right", "right", "left", "down", "left", "up"]))
