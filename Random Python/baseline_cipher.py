test1 = "acac"
test2 = "azaz"


def map_list(lst):
    min_lst = min(lst)
    return [x - min_lst for x in lst]


def detect_pattern(s1, s2):
    if len(s1) != len(s2):
        return False

    check_list1 = map_list([ord(x) for x in s1])
    check_list2 = map_list([ord(x) for x in s2])

    print(check_list1)
    print(check_list2)

    return check_list1 == check_list2


print(detect_pattern(test1, test2))
