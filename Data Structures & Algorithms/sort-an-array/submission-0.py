class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,m, r):
            left, right = nums[l: m+1], nums[m+1: r+1]
            i, j, k= l, 0, 0
            while j < len(left) and k < len(right):
                if left[j] >= right[k]:
                    nums[i] = right[k]
                    k+=1
                else:
                    nums[i] = left[j]
                    j+=1
                i+=1
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1
            while k < len(right):
                nums[i] = right[k]
                k+=1
                i+=1

        def sort(l, r):
            print(l, r)
            if r <= l:
                return
            m = (l +r)//2
            sort(l, m)
            sort(m+1, r)
            merge(l,m, r)

        sort(0, len(nums)-1)
        return nums
            
            


