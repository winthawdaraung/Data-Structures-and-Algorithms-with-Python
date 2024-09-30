nums = list(map(int, input("Enter Your List : ").split()))
res = []
if len(nums) > 2:
    for n in nums:
        for i in nums[n+1:]:
            for j in nums[i+1:]:
                if n+i+j == 0 and [n,i,j] not in res:
                    res.append([n,i,j])

    print(res)
else:
    print("Array Input Length Must More Than 2")