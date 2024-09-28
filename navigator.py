from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
        
    def isValid(self,x,y,matrix,n,m):
        # checking if (x,y) point is out of bound
        if((x<0)or(x>=n)or(y<0)or(y>=m)):
            return False
        # checking if there is ghost in that cell or if have visited it before
        if((self.navigator_maze[x][y]==1)or(matrix[x][y]==True)):
            return False
        return True
        
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        # if ghost at starting or ending point raising exception
        if(self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1):
            raise PathNotFoundException
        # creating a bool matrix for knowing visited nodes
        bool_matrix = []
        n = len(self.navigator_maze)
        m = len(self.navigator_maze[0])
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(False)
            bool_matrix.append(temp)
        # stack used here to know then last visited node in case we get stuck at some node
        # LIFO principle
        # initializing stack for storing the path
        st = Stack()
        st.push((start[0],start[1]))
        bool_matrix[start[0]][start[1]] = True
        # cur stores the current position
        cur = start
        # flag is an indicator for path not found
        flag = 0
        ''' from current position we can go on 4 possible points -> right,left,up,down
         one by one I check for every point I check is it a valid point
         if it's a valid point then push it on stack, mark it visited and update current
         if none of the 4 position is valid, then at current point path is blocked
         and pop it from stack and update cur but if stack become empty, no more path to check'''
        while(cur!=end):
            if(self.isValid(cur[0]+1,cur[1],bool_matrix,n,m)):
                st.push((cur[0]+1,cur[1]))
                bool_matrix[cur[0]+1][cur[1]] = True
                cur = (cur[0]+1,cur[1])
            elif(self.isValid(cur[0],cur[1]+1,bool_matrix,n,m)):
                st.push((cur[0],cur[1]+1))
                bool_matrix[cur[0]][cur[1]+1] = True
                cur = (cur[0],cur[1]+1)
            elif(self.isValid(cur[0]-1,cur[1],bool_matrix,n,m)):
                st.push((cur[0]-1,cur[1]))
                bool_matrix[cur[0]-1][cur[1]] = True
                cur = (cur[0]-1,cur[1])
            elif(self.isValid(cur[0],cur[1]-1,bool_matrix,n,m)):
                st.push((cur[0],cur[1]-1))
                bool_matrix[cur[0]][cur[1]-1] = True
                cur = (cur[0],cur[1]-1)
            else:
                st.pop()
                if(st.isEmpty()):
                    flag = 1
                    break
                cur = st.top()
        # finally if flag is 1 raise exception else return the path
        if(flag==1):
            raise PathNotFoundException
        return st.getList()