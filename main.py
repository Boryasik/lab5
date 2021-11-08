def medians(nums1, nums2):
    numbers = nums1 + nums2
    numbers.sort()
    print(numbers)
    if len(numbers) % 2 == 0:
        return float((numbers[:((int(len(numbers) / 2)) + 1)][-1] + numbers[:(int(len(numbers) / 2))][-1]) / 2)
    else:
        return float(numbers[:((int(len(numbers) / 2)) + 1)][-1])
