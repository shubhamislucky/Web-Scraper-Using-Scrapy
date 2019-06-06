#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:29:27 2019

@author: shubhamislucky
"""
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
    MovieJSON = json.loads(data.read())
    # print(MovieJSON)
    # print(MovieJSON[0]['title'])
    # print(len(MovieJSON))
    for x in range(0,228):
      print(MovieJSON[x]['title'], " : ", MovieJSON[x]['popularity'])
    
def main():
    
    with open('MovieData.json') as data:
        printResults(data)


if __name__ == "__main__":
    main()
    