class NumArray:

    def __init__(self, nums):
        self.num_list = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num_list[left: (right + 1)])
