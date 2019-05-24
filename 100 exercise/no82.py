# Intersection of Two Arrays II
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def solution(nums1, nums2):
    list = []
    for k in nums1:
        index = -1
        for j in range(len(nums2)):
            if nums2[j] == k:
                index = j
                break
        if index != -1:
            list.append(k)
            del nums2[index]

    return list


print(solution(nums1,nums2))