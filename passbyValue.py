#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:40:36 2019

@author: chansa
"""

def BFS(g, s, discovered): 2
level = [s]
while len(level) > 0: 
    next level = [ ]
for u in level: # first level includes only s # prepare to gather newly found vertices
for e in g.incident edges(u): # for every outgoing edge from u v=e.opposite(u)
if v not in discovered: # v is an unvisited vertex discovered[v] = e
# e is the tree edge that discovered v
next level.append(v) # v will be further considered in next pass
level = next level
# relabel ’next’ level to become current