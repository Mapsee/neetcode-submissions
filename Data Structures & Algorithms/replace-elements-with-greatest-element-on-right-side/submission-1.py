class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_idx = -1

        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break

            if greatest_idx <= i:
                greatest = 0
                for j in range(i + 1, len(arr)):
                    if arr[j] > greatest:
                        greatest = arr[j]
                        greatest_idx = j

            arr[i] = greatest

        return arr
        