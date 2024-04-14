class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # remove the edge that forms cycle

        # making adjacency list again
        self.already_connected = defaultdict(list)
        for a, b in edges :
            self.visited = defaultdict(bool) # basically just a visited set
            if self.is_already_connected(a,b) : # if path already exists
                return [a, b] # the edge 
            self.already_connected[a].append(b) # adding paths to graph/adjacency list
            self.already_connected[b].append(a) 
        
    def is_already_connected(self, a, b) :
        if a == b :
            return True
        for a_adjacent in self.already_connected[a] :
            if not self.visited[a_adjacent] : # if not visited yet check if path exists. if path exists cycle
                self.visited[a_adjacent] = True
                if self.is_already_connected(a_adjacent, b) :
                    return True
        return False
