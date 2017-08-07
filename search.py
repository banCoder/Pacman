# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Expands deepets node first.

    Frontier is a Stack."""
    stack, closed_set = util.Stack(), set()
    stack.push(([problem.getStartState()], []))
    while not stack.isEmpty():
        path, actions = stack.pop()
        node = path[-1]
        if problem.isGoalState(node) == True:
            return actions
        if str(node) not in closed_set:
            for neighbour in problem.getSuccessors(node)[::-1]:
                n_node, n_action, n_cost = neighbour
                if n_node not in path:
                    stack.push((path + [n_node], actions + [n_action]))
            closed_set.add(str(node))
    return []

def breadthFirstSearch(problem):
    """Expands shallowest first.
    
    Frontier is a Queue.
    Better to use deque!"""
    queue, closed_set = util.Queue(), set()
    queue.push(([problem.getStartState()], []))
    while not queue.isEmpty():
        path, actions = queue.pop()
        node = path[-1]   
        if problem.isGoalState(node) == True:
            return actions
        if str(node) not in closed_set:
            closed_set.add(str(node))
            for neighbour in problem.getSuccessors(node):
                n_node, n_action, n_cost = neighbour
                if n_node not in path:
                    queue.push((path + [n_node], actions + [n_action]))
    return []

def uniformCostSearch(problem):
    """Expands most cost effective first.
    
    Frontier is a Priority queue with accumulative cost.
    Counter is used to break ties."""
    p_queue, closed_set = util.PriorityQueue(), set()
    p_queue.push(([problem.getStartState()], [], 0), [0, 0])
    counter = 0
    while not p_queue.isEmpty():
        path, actions, cost = p_queue.pop()
        node = path[-1]   
        if problem.isGoalState(node) == True:
            return actions
        if str(node) not in closed_set:
            closed_set.add(str(node))
            for neighbour in problem.getSuccessors(node):
                n_node, n_action, n_cost = neighbour
                if n_node not in path:
                    counter += 1
                    p_queue.push((path + [n_node], actions + [n_action], n_cost + cost), [n_cost + cost, counter])
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    p_queue, closed_set = util.PriorityQueue(), set()
    start = problem.getStartState()
    p_queue.push(([start], [], 0), [heuristic(start, problem), 0])
    counter = 0
    while not p_queue.isEmpty():
        path, actions, cost = p_queue.pop()
        node = path[-1]   
        if problem.isGoalState(node) == True:
            return actions
        if str(node) not in closed_set:
            closed_set.add(str(node))
            for neighbour in problem.getSuccessors(node):
                n_node, n_action, n_cost = neighbour
                if n_node not in path:
                    counter += 1
                    p_queue.push((path + [n_node], actions + [n_action], n_cost + cost), [heuristic(n_node, problem) + n_cost + cost, counter])
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
