class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        size = len(gas)
        st, ed, tank = 0, 0, 0   
        arr = [gas[i] - cost[i] for i in range(size)]
        
        while st < size and ed - st < size:
            if tank + arr[ed % size] < 0:
                if st < ed:
                    tank -= arr[st]
                    st += 1
                else:
                    st += 1
                    ed += 1
            else:
                tank += arr[ed % size]
                ed += 1
        
        if tank >= 0 and st < size:
            return st
        else:
            return -1
                
                