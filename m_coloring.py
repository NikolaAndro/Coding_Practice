'''
Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors 
such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment 
of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Input:
N = 4
M = 3
E = 5
Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
Output: 1
Explanation: It is possible to colour the
given graph using 3 colours.

Your task is to complete the function graphColoring() which takes the 2d-array graph[], the number of colours and the number of nodes as inputs and returns true if answer exists otherwise false. 1 is printed if the returned value is true, 0 otherwise. The printing is done by the driver's code.
Note: In Example there are Edges not the graph.Graph will be like, if there is an edge between vertex X and vertex Y graph[] will contain 1 at graph[X-1][Y-1], else 0. In 2d-array graph[ ], nodes are 0-based indexed, i.e. from 0 to N-1.Function will be contain 2-D graph not the edges.

Expected Time Complexity: O(MN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 20
1 ≤ E ≤ (N*(N-1))/2
1 ≤ M ≤ N



Approach: The idea is to assign colors one by one to different vertices, starting from the vertex 0. 
Before assigning a color, check for safety by considering already assigned colors to the adjacent vertices 
i.e check if the adjacent vertices have the same color or not. If there is any color assignment that does not violate the conditions, 
mark the color assignment as part of the solution. If no assignment of color is possible then backtrack and return false.

'''

#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
#the 2d-array graph[], the number of colours and the number of nodes 
def graphColoring(graph, k, V):
    # list that represents different colors
    color_list = [x for x in range(5, 5+k)]

    # assign first vertex with first color
    graph[0][0] = color_list[0]

    # check each vertex
    for i in range(1,V):
        copy = [x for x in range(5, 5+k)] # make a copy of the colors list
        for j in range(0, V):
            # scenario when the adjacent vertex has the same color
            if graph[i][j] == 1 and graph[j][j] != 0:
                #check if already removed
                if graph[j][j] in copy:
                    copy.remove(int(graph[j][j])) # remove the used color by the adjacent vertex from the list of colors

            if len(copy) == 0:
                for z in graph:
                    print(z) 
                return 0
            #assign color to the vertex
            graph[i][i] = copy[0]
            
    for z in graph:
        print(z)       
    return 1

#  Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    
    V = int(input()) # number of vertices
    k = int(input()) # number of colors
    m = int(input()) # number of edges
    list = [int(x) for x in input().strip().split()]
    graph = [[0 for i in range(V)] for j in range(V)]
    cnt = 0
    for i in range(m):
        graph[list[cnt]-1][list[cnt+1]-1]=1
        graph[list[cnt+1]-1][list[cnt]-1]=1
        cnt+=2
    if(graphColoring(graph, k, V)==True):
        print("It is possible!")
    else:
        print("It is not possible!")
