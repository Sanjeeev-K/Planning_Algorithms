# # importing the required module 
import matplotlib.pyplot as plt 
import numpy as np


def main():

    maze =  np.array(              [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]    )

    
    # res = maze[::-1] 
    # maze = res
    # maze = np.transpose(maze)

    a = len(maze) + 2
    b = len(maze[0]) + 2
    maze2 = np.ones((a,b))
    for i in range (1,a-1):
        for j in range (1,b-1):
            maze2[i][j] = maze[i-1][j-1]


    fig= plt.figure(figsize=(5.6,5.7))
    for i in range (len(maze2)):
        for j in range (len(maze2[0])):
            a1 = maze2[i][j]
            if(a1==0):
                # plt.plot(i, j,'rs', fillstyle='none', markersize=27) 
                plt.plot(j-1, a-i,'rs', fillstyle='none', markersize=27) 
            else:
                # plt.plot(i, j,'bs', fillstyle='full', markersize=25) 
                plt.plot(j-1, a-i,'bs', fillstyle='full', markersize=25) 
    
    start = (0,0)
    # end = (len(maze)-1,len(maze[0])-1)
    # end = (9,8)
    end = (0,len(maze[0])-1)

    # plt.plot(start[0]+1, start[1]+1,'rs', fillstyle='full', markersize=27) 
    # plt.plot(end[0]+1, end[1]+1,'gs', fillstyle='full', markersize=27) 

    plt.plot(start[1]+1-1, a-start[0]-1,'rs', fillstyle='full', markersize=27) 
    plt.plot(end[1]+1-1, a-end[0]-1,'gs', fillstyle='full', markersize=27) 


    start2 = (start[0]+1, start[1]+1)
    end2 = (end[0]+1, end[1]+1)

    # res = maze2[::-1] 
    # maze2 = res
    # maze2 = np.transpose(maze2)
    # print(maze2)
    # print(maze2[end2[0]][end2[1]])
    # input()

    # DONE flag = "initial";
    # DONE Add start to open_list
    # DONE current = [0,start2[0],start2[1]]
    # DONE counter = 1;
    # DONE explored matrix; where obstacles are = -2, rest are -1.
    # DONE While(open!= empty)
    # DONE if(neighbour_up != obstacle && neighbor_up is not explored yet)
    # DONE    Calculate f+g  // f = current[0]+1// g = abs(end2[0]-n_up[0])+ abs(end2[1]-n_up[1])
    # DONE    add n_up to open_list
    # DONE if(neighbour_left != obstacle && neighbor_left is not explored yet)
    # DONE    Calculate f+g  // f = current[0]+1// g = abs(end2[0]-n_up[0])+ abs(end2[1]-n_up[1])
    # DONE    add n_left to open_list
    # DONE if(neighbour_down != obstacle && neighbor_down is not explored yet)
    # DONE    Calculate f+g  // f = current[0]+1// g = abs(end2[0]-n_up[0])+ abs(end2[1]-n_up[1])
    # DONE    add n_down to open_list
    # DONE if(neighbour_right != obstacle && neighbor_right is not explored yet)
    # DONE     Calculate f+g  // f = current[0]+1// g = abs(end2[0]-n_up[0])+ abs(end2[1]-n_up[1])
    # DONE    add n_right to open_list
    # DONE Add current to closed list
    # DONE Remove current from open list
    # DONE Update explored[current] = counter;
    # DONE sort open list.
    # DONE if open_list == empty; set flag = "not found"; break;
    # DONE else assign current as first element of open list.
    # DONE highlight current node.
    # DONE print the current node.
    # DONE if current == end; flag = found; break;
    # DONE print(flag)
    # DONE print(explored_matrix)

    

    flag = "initial"
    open_list = [[0,start2[0],start2[1],0]]
    closed_list = []
    current = open_list[0]
    counter = 1

    a = len(maze2)
    b = len(maze2[0])
    explored_matrix = np.ones((a,b)) # Obstacles as -2, Unexplored at -1, Explored at numbers>=0, If it has been added to the open list, then -3.
    for i in range (len(explored_matrix)):
        for j in range (len(explored_matrix[0])):
            q = maze2[i][j]
            if(q==1):
                explored_matrix[i][j] = -2
            else:
                explored_matrix[i][j] = -1
    
    # print(maze2)
    # print(explored_matrix)
    # input()

    while(len(open_list)!=0):
        #Neighbor Up
        x = current[1]
        y = current[2]+1
        if(explored_matrix[x][y]== -1):                 # Checking if this neighboring node is not obstacle or already explored.
            Heuristic = abs(end2[0]-x)+ abs(end2[1]-y) #Manhattan distance
            Cost = current[3]+1
            g = Cost + Heuristic
            open_list.append([g,x,y,Cost])
            explored_matrix[x][y]=-3
        #Neighbor Right
        x = current[1]+1
        y = current[2]
        if(explored_matrix[x][y]== -1):                 # Checking if this neighboring node is not obstacle or already explored.
            Heuristic = abs(end2[0]-x)+ abs(end2[1]-y) #Manhattan distance
            Cost = current[3]+1
            g = Cost + Heuristic
            open_list.append([g,x,y,Cost])
            explored_matrix[x][y]=-3
        #Neighbor Down
        x = current[1]
        y = current[2]-1
        if(explored_matrix[x][y]== -1):                 # Checking if this neighboring node is not obstacle or already explored.
            Heuristic = abs(end2[0]-x)+ abs(end2[1]-y) #Manhattan distance
            Cost = current[3]+1
            g = Cost + Heuristic
            open_list.append([g,x,y,Cost])
            explored_matrix[x][y]=-3
        #Neighbor Left
        x = current[1]-1
        y = current[2]
        if(explored_matrix[x][y]== -1):                 # Checking if this neighboring node is not obstacle or already explored.
            Heuristic = abs(end2[0]-x)+ abs(end2[1]-y) #Manhattan distance
            Cost = current[3]+1
            g = Cost + Heuristic
            open_list.append([g,x,y,Cost])
            explored_matrix[x][y]=-3
        open_list.remove(current)
        closed_list.append(current)
        x = current[1]
        y = current[2]
        explored_matrix[x][y]=counter
        counter += 1
        
        if ( len(open_list)==0 ):
            flag = "Goal not found"
            break
        else:
            open_list.sort()
            plt.pause(0.1) 
            # plt.plot(x, y,'yo', fillstyle='full', markersize=22)
            plt.plot(y-1, a-x,'yo', fillstyle='full', markersize=22)
            plt.pause(0.1) 
            # print(x," ",y)
            current = open_list[0]
            if current[1]==end2[0] and current[2]==end2[1]:
                plt.plot(current[2]-1, a-current[1],'yo', fillstyle='full', markersize=22)
                flag = "Goal found"
                print(explored_matrix)
                plt.pause(5)
                break
            # print(open_list)
            # print(closed_list)
            # input()
            # print(explored_matrix)
            # print(current)
            # input()

    
    # end of while loop
    print(flag)
    print(explored_matrix)
     
    # # naming the axes 
    # plt.xlabel('x - axis')
    # plt.ylabel('y - axis') 
    
    # # giving a title to my graph 
    # plt.title('My first graph!') 


    # # Setting axes limits
    # plt.ylim(-1,11)
    # plt.xlim(-1,11)

    # # function to show the plot 
    # # plt.show() 

    # for i in range (len(maze2)):
    #     for j in range (len(maze2[0])):
    #         plt.plot(j, i,'ys', fillstyle='full', markersize=27)
    #         plt.pause(0.1)


    # path = astar(maze, start, end)
    # print(path)


if __name__ == '__main__':
    main()

