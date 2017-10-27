#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:08:13 2017

@author: emg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output-2017-10-11.csv')
am = (pd.read_csv('am-output-2017-10-11.csv', usecols=['date','comments'])
        .rename(columns={'comments':'amcomments'}))
df = df.merge(am, how='outer', on='date').fillna(0)
df.index = pd.to_datetime(df['date'])

cmap = plt.get_cmap('Dark2')

def plot_monthly_change(df):
    prev_a = [0] + list(df['authors'])
    df['prev_a'] = prev_a[:-1]
    df['diff_a'] = df['authors'] - df['prev_a']
    df['achange'] = df['diff_a'].divide(df['prev_a'])*100
    
    
    prev_c = [0] + list(df['comments'])
    df['prev_c'] = prev_c[:-1]
    df['diff_c'] = df['comments'] - df['prev_c']
    df['cchange'] = df['diff_c'].divide(df['prev_c'])*100
      
      
    labels = pd.to_datetime(df.date).dt.strftime('%m-%y')
      
    fig = plt.figure() # Create matplotlib figure
    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
    width = 0.4
    
    df.cchange.plot(kind='bar', color='red', ax=ax, width=width, position=1)
    df.achange.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)
    
    ax.set_ylabel('% comment change')
    ax2.set_ylabel('% author change')
    ax.set_xticklabels(labels)

    plt.axhline(y=0, color='black')
    
    plt.title('Monthly % change in comment (red) & author (blue) counts for r/The_Donald')
    plt.savefig('/Users/emg/Programming/GitHub/aws/images/td-monthly-change.png', dpi=100)
    plt.show()


subset = df.drop([df.index[0]])
plot_monthly_change(subset)

def plot_monthly_counts():
    labels = pd.to_datetime(df.date).dt.strftime('%m-%y')
      
    fig = plt.figure() # Create matplotlib figure
    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
    width = 0.4
    
    df.comments.plot(kind='bar', color='red', ax=ax, width=width, position=1)
    df.authors.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)
    
    ax.set_ylabel('Number of Comments')
    ax2.set_ylabel('Number of Unique Authors')
    plt.xticks(df.index, labels, rotation='vertical')
    plt.title('Monthly Comment (red) & Author (blue) Counts for r/The_Donald')
    plt.savefig('/Users/emg/Programming/GitHub/aws/images/td-monthly-counts.png', dpi=100)
    plt.show()

plot_monthly_counts()
 
def plot_ratio():  
    df['a_c_ratio'] = df['authors'].divide(df['comments'])
    labels = pd.to_datetime(df.date).dt.strftime('%m-%y')
    
    fig = plt.figure() # Create matplotlib figure 
    ax = fig.add_subplot(111) # Create matplotlib axes
    width = 0.4
    df.a_c_ratio.plot(kind='bar', color='green', ax=ax, width=width, position=1)
    
    ax.set_ylabel('Ratio')
    plt.xticks(df.index, labels, rotation='vertical')
    plt.title('Monthly Ratio of unique authors to comments in r/The_Donald')
    plt.savefig('/Users/emg/Programming/GitHub/aws/images/td-monthly-ratio.png', dpi=100)
    plt.show()

plot_ratio()
    
def plot_am_counts():    
    labels = pd.to_datetime(df.date).dt.strftime('%m-%y')
    
    fig = plt.figure() # Create matplotlib figure
    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
    width = 0.4
    
    df.comments.plot(kind='bar', color=cmap.colors[0], ax=ax, width=width, position=1)
    df.amcomments.plot(kind='bar', color=cmap.colors[2], ax=ax2, width=width, position=0)
    
    ax.set_ylabel('Number of Comments')
    ax2.set_ylabel('Number of AutoModerator Comments')
    ax.set_xticklabels(labels)
    
    
    ax.legend(loc=2)
    ax2.legend(loc=(0.015,0.8))
    
    plt.title('Monthly Comment & Author Counts for r/The_Donald')
    plt.savefig('/Users/emg/Programming/GitHub/aws/images/td-monthly-am-counts.png', dpi=100)
    plt.show()

plot_am_counts()