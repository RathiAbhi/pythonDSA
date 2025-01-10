import math


class SearchTree:
    """
    a full binary tree is given where the values are in AP
    root node is always 1 and we need to find out a given value in better than O(n)

    Logic: find height using either dfs or property of full binary tree
    number of nodes = 2^h - 1 (where h is height of the tree)
    now using a + (n-1) d = value, here a and d are 1
    so, n = 1 + value --> if n is int and <=number of nodes, then true else false\

    here we are using a simplified case and using tree as a list
    """
    def searchTree(self,nodes:list[int],x:int)->bool:
        n = len(nodes)

        return 1<=x<=n

    def main(self):
        if self.searchTree([1,2,3,4,5,6,7,8,9,10,11],10):
            print("pass")
        else:
            print("fail")

search  = SearchTree()
search.main()