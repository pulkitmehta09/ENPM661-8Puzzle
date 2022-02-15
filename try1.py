#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:12:34 2022

@author: pulkit
"""

import numpy as np
import os

class node:
    def __init__(self, node_i, data, parent_node, visited, cost):
        self.node_i = node_i
        self.data = data
        self.parent_node = parent_node
        self.visited = False
        self.cost = cost
        

           
        
def blank_tile_location(node):
    i, j = np.where(node == 0)
    i = int(i)
    j = int(j)
    return i,j

def ActionMoveLeft(CurrentNode):
    i, j = blank_tile_location(CurrentNode)
    if(j == 0):
        newNode = None
        Status = False
    else:
        newNode = np.copy(CurrentNode)
        newNode[i,j-1], newNode[i,j] = newNode[i,j], newNode[i,j-1]
        Status = True
    return Status, newNode

def ActionMoveRight(CurrentNode):
    i, j = blank_tile_location(CurrentNode)
    if(j == 2):
        newNode = None
        Status = False
    else:
        newNode = np.copy(CurrentNode)
        newNode[i,j+1], newNode[i,j] = newNode[i,j], newNode[i,j+1]
        Status = True
    return Status, newNode

def ActionMoveUp(CurrentNode):
    i, j = blank_tile_location(CurrentNode)
    if(i == 0):
        newNode = None
        Status = False
    else:
        newNode = np.copy(CurrentNode)
        newNode[i-1,j], newNode[i,j] = newNode[i,j], newNode[i-1,j]
        Status = True
    return Status, newNode

def ActionMoveDown(CurrentNode):
    i, j = blank_tile_location(CurrentNode)
    if(i == 2):
        newNode = None
        Status = False
    else:
        newNode = np.copy(CurrentNode)
        newNode[i+1,j], newNode[i,j] = newNode[i,j], newNode[i+1,j]
        Status = True
    return Status, newNode

def getInitialState():
    state = [int(item) for item in input("Enter the list items : ").split()]
    state = np.array(state)
    if(state.size != 9):
        print("Enter valid state")
        getInitialState()
    state = state.reshape(3,3)
    
    return state

def getGoalState():
    state = [int(item) for item in input("Enter the list items : ").split()]
    state = np.array(state)
    if(state.size != 9):
        print("Enter valid state")
        getGoalState()
    state = state.reshape(3,3)
    return state

def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)
 
A = getInitialState()
# B = isSolvable(A)

def move_tile(move, data):
    if move == 'Up':
        return ActionMoveUp(data)
    if move == 'Right':
        return ActionMoveRight(data)
    if move == 'Down':
        return ActionMoveDown(data)
    if move == 'Left':
        return ActionMoveLeft(data)
    else:
        return None

def CheckVisited(node, list):
    for item in list:
        if(np.array_equal(item, node)):
            return True
    else:
        return False
    
def get_child_nodes(node:node,list):
    move = ["Up", "Right", "Down", "Left"]
    for direction in move:
        Status, child_node = move_tile(direction, node.data)
        if (Status):
            list.append(child_node)
    return list

def BFS(Initial_node):
    
    queue = []          # list of found nodes
    visited = []
    start_node = node(0,Initial_node,None,None,0)
    queue.append(start_node.data)    
    visited.append(start_node.data)
    while (queue.len > 0):
        for item in queue:
            if (item.visited):
                popped = queue.pop(0)
            else:
                queue = get_child_nodes(item,queue)
        
        