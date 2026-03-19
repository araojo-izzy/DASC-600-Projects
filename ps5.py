#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 14:02:17 2026

@author: izzy.araojo
"""

# Problem Set 5
# Name: Izzy Araojo
# Collaborators: N/a
#Time spent on assignment: 1 hr, 15 mins
    
import matplotlib.pyplot as plt
import numpy as np

#species names
species = ["Adelie", "Chinstrap", "Gentoo"]

#penguin data [0 = adalie, 1 = chinstrap, 2 = gentoo]
bill_depth = [18.35, 18.43, 14.98]
bill_length = [38.79, 48.83, 47.50]
flipper_length = [189.95, 195.82, 217.19]
body_mass = [3700, 3733, 5076]

#x positions
x=np.arange(len(species)) 
#create array w/ species and calculate number of elements
width = 0.35 # so the bars do not overlap

#graph 1: Bill Depth and Length
plt.subplot(2, 1, 1) #2 rows, 1 column, position 1

bars1 = plt.bar(x - width/2, bill_depth, width, label = "Bill Depth (mm)", color = "lightblue")
bars2 = plt.bar(x + width/2, bill_length, width, label = "Bill Length (mm)", color = "pink")
#bars shifted to left/right to not overlap

plt.title("Bill Measurements by Species")
plt.xlabel("Species", fontsize = 11.5)
plt.ylabel("Millimeters (mm)")
plt.xticks(x, species)
plt.ylim(0, 60)
plt.legend(loc = 'best', fontsize = 9)

#adding value labels above each bar
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height}", ha="center", va= "bottom", fontsize = 8)

#graph 2: Flipper and Body
plt.subplot(2, 1, 2) #2 rows, 1 column, position 2

bars3 = plt.bar(x - width/2, flipper_length, width, label = "Flipper Length (mm)", color = "lightgreen")
bars4 = plt.bar(x + width/2, body_mass, width, label = "Body Mass (g)", color = "lightsalmon")
#bars shifted to left/right to not overlap

plt.title("Flipper Length and Body Mass by Species")
plt.xlabel("Species", fontsize = 11.5)
plt.ylabel("Measurements (mm and g)")
plt.xticks(x, species)
plt.ylim (0, 6000)
plt.legend(loc = 'best', fontsize = 9)

#adding value labels above each bar
for bars in [bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height}", ha="center", va= "bottom", fontsize = 8)
        
#adjust spacing between the two graphs
plt.tight_layout()

#show the plot
plt.show()
        