import math


class SearchTree:
    """
    a full binary tree is given where the values are in AP
    root node is always 1 and we need to find out a given value in better than O(n)

    Calculate the level and count of total elements till that level
    Now, if count is greater than or equal to our node, then
    it exists. Otherwise it does not

    here we are using a simplified case and using tree as a list
    """
    def searchTree(self,nodes:list[int],x:int)->bool:
        if x<1:
            return False
        level = 1
        count = 1

        while count < x:
            level += 1
            count += 2**(level-1)

        return count>=x

    def main(self):
        if (self.searchTree([1,2,3,4,5,6,7,8,9,10,11],10) and
        self.searchTree([1,2,3,4,5,6,7,8,9,10,11],5)):
            print("pass")
        else:
            print("fail")

search  = SearchTree()
search.main()