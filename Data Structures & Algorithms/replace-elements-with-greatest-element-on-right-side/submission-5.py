class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currentMax = -1 
        for i  in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = currentMax 
            if temp > currentMax:
                currentMax = temp

        return arr

        