def mergeTwoLists(list1, list2):
        result_list = list1
        for i in range(len(list2)):
            result_list.append(list2[i])
        return sorted(result_list)