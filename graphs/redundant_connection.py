from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges) :
        # remove the edge that forms cycle

        # making adjacency list again
        self.adj_list = defaultdict(list)
        for a, b in edges :
            self.visited = set() # dfs is run on every node so a fresh visited is needed each time
            if self.edge_exists(a,b) : # if path already exists
                return [a, b] # the edge 
            self.adj_list[a].append(b) # adding paths to graph/adjacency list
            self.adj_list[b].append(a) # eventually once this is filled out enough 
        
    def edge_exists(self, a, b) :
        if a == b : # the base case
            return True

        self.visited.add(a)
        for neighbor in self.adj_list[a] :
            if neighbor not in self.visited : # if not visited yet check if path exists. if path exists cycle
                if self.edge_exists(neighbor, b) :
                    return True
        return False

def main() :
    edges = [[1,2],[1,3],[2,3]]
    obj = Solution()
    print(obj.findRedundantConnection(edges))

main()
    