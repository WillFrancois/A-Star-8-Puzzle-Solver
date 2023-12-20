import heapq
import random

#Define nodes in tree for A*
class Node:
    #Desired index of each number is the number -1.
    def find_distance_in_state(self, number : int, current_index : int):
        #x2 - x1 + y2 - y1
        desired_y_position = int((number - 1) / 3)
        desired_x_position = (number - 1) % 3

        current_y_position = int((current_index - 1) / 3)
        current_x_position = (current_index - 1) % 3

        return abs(current_x_position - desired_x_position) + abs(current_y_position - desired_y_position)

    def find_hValue(self):
        for i in range(1, 9):
            self.hValue += self.find_distance_in_state(i, self.state.index(i)+1)
    
    def create_fValue(self):
        self.fValue = self.hValue + self.gValue

    def create_children(self, heap):
        #Creates a tile moving right.
        if (self.state.index(0)+1) % 3 != 1:
            new_list = []
            for i in range(0,9):
                if self.state.index(0)-1 == i:
                    new_list.append(0)
                elif self.state.index(0) == i:
                    new_list.append(self.state[self.state.index(0)-1])
                else:
                    new_list.append(self.state[i])
            new_child = Node(self, new_list, self.gValue+1)
            heapq.heappush(heap, (new_child.fValue, random.random() * 500000, new_child))

        #Creates a tile moving left.
        if (self.state.index(0)+1) % 3 != 0:
            new_list = []
            for i in range(0,9):
                if self.state.index(0)+1 == i:
                    new_list.append(0)
                elif self.state.index(0) == i:
                    new_list.append(self.state[self.state.index(0)+1])
                else:
                    new_list.append(self.state[i])
            new_child = Node(self, new_list, self.gValue+1)
            heapq.heappush(heap, (new_child.fValue, random.random() * 500000, new_child))

        #Creates a tile moving down.
        if (self.state.index(0)+1) > 3:
            new_list = []
            for i in range(0,9):
                if self.state.index(0)-3 == i:
                    new_list.append(0)
                elif self.state.index(0) == i:
                    new_list.append(self.state[self.state.index(0)-3])
                else:
                    new_list.append(self.state[i])
            new_child = Node(self, new_list, self.gValue+1)
            heapq.heappush(heap, (new_child.fValue, random.random() * 500000, new_child))

        #Creates a tile moving up.
        if (self.state.index(0)+1) <= 6:
            new_list = []
            for i in range(0,9):
                if self.state.index(0)+3 == i:
                    new_list.append(0)
                elif self.state.index(0) == i:
                    new_list.append(self.state[self.state.index(0)+3])
                else:
                    new_list.append(self.state[i])
            new_child = Node(self, new_list, self.gValue+1)
            heapq.heappush(heap, (new_child.fValue, random.random() * 500000, new_child))

    def __init__(self, parent, state : list[int], gValue : int):
        self.parent = parent
        self.state = state
        self.gValue = gValue
        self.hValue = 0
        self.find_hValue()
        self.create_fValue()
   
def main():
    #Start solving
    h = []
    start_state = [4, 1, 3, 0, 2, 8, 7, 6, 5]
    start = Node(None, start_state, 0)

    heapq.heappush(h, (start.gValue, -1, start))
    found_hValue = h[0][2].hValue

    cur_node = h[0][-1]

    while found_hValue != 0:
        cur_node = h[0][-1]
        heapq.heappop(h)
        cur_node.create_children(h)
        found_hValue = h[0][-1].hValue
        # print(found_hValue)
        # print(h[0][-1].state)

    while cur_node.parent != None:
        print(cur_node.state[cur_node.parent.state.index(0)])
        cur_node = cur_node.parent   

if __name__ == "__main__":
   main()