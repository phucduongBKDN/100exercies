#Intersection of Two Arrays

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
def intersection(a,b):
    return (set(a) & set(b))

print(intersection(nums1,nums2))