#Minimum Index Sum of Two Lists
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]


def findRestaurant(self, list1, list2):
    commons = [word for word in list1 if word in list2]
    answer = []
    smallest = 1000000
    for common in commons:
        index1 = list1.index(common)
        index2 = list2.index(common)
        index = index1 + index2
        if smallest > index:
            smallest = index
            answer = [common]
        elif smallest == index:
            answer.append(common)
    return answer


print(findRestaurant(list1,list2))
