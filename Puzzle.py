#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:12:34 2022
ENPM 661
Project 1

@author: Pulkit Mehta
UID: 117551693

"""

from collections import deque
from plot_path import *
import numpy as np

def getInitialState():
    flag = False
    while not flag:
        state = [int(item) for item in input("Enter the initial state: ").split()]
        temp = state.copy()
        valid = [0,1,2,3,4,5,6,7,8]
        temp.sort()
        if (temp == valid):
            flag = True
        else:
            print("\n Enter a valid state! \n")
        
    return state

def getGoalState():
    flag = False
    while not flag:
        state = [int(item) for item in input("Enter the goal state: ").split()]
        temp = state.copy()
        valid = [0,1,2,3,4,5,6,7,8]
        temp.sort()
        if (temp == valid):
            flag = True
        else:
            print("\n Enter a valid state! \n")
    return state



def BlankTileLocation(node):
    """
    Finds the index of tile with number 0 in a given state.

    Parameters
    ----------
    node : list
        A given state.

    Returns
    -------
    list
        Location of blank tile (sith row and jth column of state).

    """
    index = node.index(0)               
    i = (index % 3) 
    j = (index // 3)
    return [i,j]

def ActionMoveUp(node):
    """
    Swaps the blank tile with the adjacent tile in the up direction  

    Parameters
    ----------
    node : list
        A given state.

    Returns
    -------
    list
        status : True or False based on validity of move.
        new_node : New state with performed action.

    """

    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if i == 0:
        status = False
    else:
        status = True
        zero_index = (3 * j) + i
        up_index = (3 * j) + (i - 1)
        up_element = node[up_index]
        new_node[up_index] = 0
        new_node[zero_index] = up_element
    return [status,new_node]

def ActionMoveRight(node):
    """
    Swaps the blank tile with the adjacent tile in the right direction  

    Parameters
    ----------
    node : list
        A given state.

    Returns
    -------
    list
        status : True or False based on validity of move.
        new_node : New state with performed action.

    """

    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if j == 2:
        status = False
    else:
        status = True
        zero_index = (3 * j) + i
        right_index = (3 * (j + 1)) + i
        right_element = node[right_index]
        new_node[right_index] = 0
        new_node[zero_index] = right_element
    return [status,new_node]

def ActionMoveDown(node):
    """
    Swaps the blank tile with the adjacent tile in the down direction  

    Parameters
    ----------
    node : list
        A given state.

    Returns
    -------
    list
        status : True or False based on validity of move.
        new_node : New state with performed action.

    """

    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if i == 2:
        status = False
    else:
        status = True
        zero_index = (3 * j) + i
        down_index = (3 * j) + (i + 1)
        down_element = node[down_index]
        new_node[down_index] = 0
        new_node[zero_index] = down_element
    return [status,new_node]

def ActionMoveLeft(node):
    """
    Swaps the blank tile with the adjacent tile in the left direction  

    Parameters
    ----------
    node : list
        A given state.

    Returns
    -------
    list
        status : True or False based on validity of move.
        new_node : New state with performed action.

    """

    [i,j] = BlankTileLocation(node)
    new_node = node.copy()
    if j == 0:
        status = False
    else:
        status = True
        zero_ind = (3 * j) + i
        left_ind = (3 * (j - 1)) + i
        left_element = node[left_ind]
        new_node[left_ind] = 0
        new_node[zero_ind] = left_element
    return [status,new_node]

def AddNode(new_node,nodes,node_set):
    """
    Adds a new node.

    Parameters
    ----------
    new_node : list
        Node to be added in list.
    nodes : list
        List to which node is to be added.
    node_set : set
        Set to which new node is to be added.

    Returns
    -------
    list
        Updated nodes, node_set and a bool specifying if the new node to be added was already in the set or not..

    """
    visited = False
    if tuple(new_node[0:9]) in node_set:
        visited = True
    else:
        nodes.append(new_node)
        node_set.add(tuple(new_node[0:9]))
    return [nodes,node_set, visited]


def generate_path(nodes):
    """
    Path from start state to goal state.

    Parameters
    ----------
    nodes : list
        List of nodes.

    Returns
    -------
    path : list
        List of nodes in path from start state to goal state.

    """
    
    parent = nodes[-1][9]
    path_nodes = [parent]
    while parent != -1:
        parent_node = nodes[path_nodes[-1]]
        parent = parent_node[9]
        path_nodes.append(parent)
    path = [nodes[-1][0:9]]
    for ind in path_nodes:
        if ind == -1:
            break
        else:
            path.insert(0,nodes[ind][0:9])
    return path



def check_neighbors(cur_node,direction):
    """
    Checks the neighbors of a node in given direction and returns a neighbor if valid.  

    Parameters
    ----------
    cur_node : list
        Node for which neighbours are to be checked.
    direction : string
        Specified direction.

    Returns
    -------
    list
        Validity of move and new node in given direction.

    """
    if direction == 'up':
        [status,new_node] = ActionMoveUp(cur_node)
    if direction == 'right':
        [status,new_node] = ActionMoveLeft(cur_node)
    if direction == 'down':
        [status,new_node] = ActionMoveDown(cur_node)
    if direction == 'left':
        [status,new_node] = ActionMoveRight(cur_node)
    
    return [status,new_node]

def BFS(start_node,goal_node):
    """
    Applies Breadth first search, given a start state and goal state.

    Parameters
    ----------
    start_node : list
        Start state.
    goal_node : list
        Goal state.

    Returns
    -------
    list
        Success of opertion and sequence of nodes.

    """
    
    nodes = [[]]

    
    node_set = {tuple(start_node)}

    start_node.append(-1) #set start node to have parent of -1
    nodes[0] = start_node


    queue = deque()
    queue.append(0) #set the start_node as the first node in the queue

    isgoal = False
    success = False

    neighbors = ['left','up','right','down'] #modify order to change the order of search
    while queue:
        # Set the current node as the top of the queue and remove it
        parent = queue.popleft();
        cur_node = nodes[parent]
        for direction in neighbors:
            [status,new_node] = check_neighbors(cur_node,direction)
            if status == True:
                new_node[9] = parent
                [nodes,node_set,exists] = AddNode(new_node,nodes,node_set)
                if not exists:            
                    queue.append(len(nodes)-1)
            if new_node[0:9] == goal_node:
                isgoal = True
                break
        if isgoal:
            success = True
            break

    return [success, nodes]



def Initialize_puzzle():
    """
    Initializes the puzzle with user-defined start and goal state

    Returns
    -------
    start_node : list
        Start state.
    goal_node : list
        Goal state.

    """
    print("\n *************************** \n")
    print(" Welcome to 8 Puzzle Solver")
    print("\n *************************** \n")
    print(" This solver considers inputs to be: \n Nine unique non-negative integers in domain: [0,8] \n")
    print(" Please enter the start state for the puzzle in the format provided below \n")
    print(" For a state like: \n")
    sample = [1,4,7,2,5,8,3,6,0]
    print_matrix(sample)
    print("\n please enter: 1 4 7 2 5 8 3 6 0")     
    start_node = getInitialState()
    goal_node = getGoalState()
        
    return start_node, goal_node


def Solve(start_node, goal_node):
    """
    Solves the puzzle using Breadth First Search(BFS).

    Parameters
    ----------
    start_node : list
        Start state.
    goal_node : TYPE
        Goal state.

    Returns
    -------
    None.

    """
    [success, nodes] = BFS(start_node,goal_node)
    if not success:
        print(" The puzzle could not be solved for the provided states, shown below: \n")
        print(" Start State:\n")
        print_matrix(start_node)
        print(" Goal State:\n")
        print_matrix(goal_node)
    else:
        nodePath = open("nodePath.txt","w+")
        Nodes = open("Nodes.txt","w+")
        NodesInfo = open("NodesInfo.txt","w+")
        path = generate_path(nodes)
        for node in path:
            for tile in node:
                nodePath.write(str(tile) + " ")
            nodePath.write('\n')
        nodePath.close()
        
        for i,node in enumerate(nodes):
            for j,tile in enumerate(node):
                if j != 9:
                    Nodes.write(str(tile) + " ")
            Nodes.write('\n')
            
            NodesInfo.write(str(i) + " ")
            NodesInfo.write(str(node[9]) + " ")
            NodesInfo.write(str(0) + " ")
            NodesInfo.write('\n')
        Nodes.close()
        NodesInfo.close()
        
        plot_path()
            





