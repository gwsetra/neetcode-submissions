class KthLargest:
    heap = []
    maxs = 0
    def __init__(self, k: int, nums: List[int]):
        global maxs
        self.heap = []
        print(self.heap)
        maxs = k

        for loop in range(0, len(nums)):
            print("initialise: ",self.heap)
            self.heap.append(nums[loop])
            print("after initial insertion: ",self.heap)

            if len(self.heap) > k:
                if self.heap[loop] > self.heap[0]:
                    # trickledown
                    # swap head with tail
                    self.heap[0] = self.heap[loop]
                    self.heap.pop()
                    print("inside if: ",self.heap)
                    # rebalancing
                    if self.heap[0] > self.heap[1]: # swap new root with left branch
                        print('swap root with left')
                        tmp = self.heap[0]
                        self.heap[0] = self.heap[1]
                        self.heap[1] = tmp
                    else:
                        print('swap root with right')
                        tmp = self.heap[2]
                        self.heap[0] = self.heap[2]
                        self.heap[2] = tmp
                    print("post rebalance: ",self.heap)
                else:
                    # new element is smaller than the most smallest in tree
                    self.heap.pop()
        print("complete", self.heap)

    def add(self, val: int) -> int:
        print('about to add::', val)
        self.heap.append(val)
        print('after addition', self.heap)
        print(len(self.heap))
        print(maxs)
        if len(self.heap) > maxs:
            if self.heap[len(self.heap)-1] > self.heap[0]:
                # trickledown
                # swap head with tail
                self.heap[0] = self.heap.pop()
                print("inside if add: ", self.heap)

                # rebalancing
                if len(self.heap) < 3:
                    print('len self.heap lesser than 3')
                    if self.heap[len(self.heap)-1] > self.heap[0] and self.heap[0] > self.heap[1]:
                        tmp = self.heap[0]
                        self.heap[0] = self.heap[1]
                        self.heap[1] = tmp
                elif self.heap[2] < self.heap[0] and self.heap[2] < self.heap[1]:
                    print('swap root with right')
                    tmp = self.heap[0]
                    self.heap[0] = self.heap[2]
                    self.heap[2] = tmp
                elif self.heap[0] > self.heap[1]: # swap new root with left branch
                    print('swap root with left')
                    tmp = self.heap[0]
                    self.heap[0] = self.heap[1]
                    self.heap[1] = tmp
                else:
                    pass
                print("post rebalance: ",self.heap)
            
            else:
                # new element is smaller than the most smallest in tree
                print('newest element is smaller than head. I"m popping it out')
                self.heap.pop()
        return self.heap[0]