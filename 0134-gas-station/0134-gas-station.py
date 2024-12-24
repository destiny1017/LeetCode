class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        i = 0
        st = 0
        ed = 0
        tank = 0
        
        arr = [gas[i] - cost[i] for i in range(len(gas))]
        #print(arr)
        
        while st < len(gas) and ed - st < len(gas):
            #print(st, ed, tank)
            if tank + arr[ed % len(gas)] < 0:
                if st < ed:
                    tank -= arr[st]
                    st += 1
                else:
                    st += 1
                    ed += 1
            else:
                tank += arr[ed % len(gas)]
                ed += 1
        
        if tank >= 0 and st < len(gas):
            return st
        else:
            return -1
                
                