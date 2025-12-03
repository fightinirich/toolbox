#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_monomer_data(file_data):
    # Parse the tab-delimited data
    df = pd.read_csv(file_data, sep='\t')
    
    # Create figure and primary y-axis
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot lines with error bars on primary y-axis
    line1 = ax1.errorbar(df['Monomer Length'], df['Linear'], yerr=df['SEM-Linear'], fmt='o-', color='#1f77b4', label='Linear', capsize=3, markersize=5)
    line2 = ax1.errorbar(df['Monomer Length'], df['Monocyclic'], yerr=df['SEM-Monocyclic'], fmt='o-', color='#ff7f0e', label='Monocyclic', capsize=3, markersize=5)
    line3 = ax1.errorbar(df['Monomer Length'], df['Bicyclic'], yerr=df['SEM-Bicyclic'], fmt='o-', color='#2ca02c', label='Bicyclic', capsize=3, markersize=5)
    
    # Set up primary y-axis
    ax1.set_xlabel('Monomer Length', fontsize=12, color='black')
    ax1.set_ylabel('Time (seconds)', fontsize=12, color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.set_xticks(np.arange(9, 26, 1))
    ax1.set_yscale('log') # log scale for better visualization
    
    # Create secondary y-axis
    ax2 = ax1.twinx()
    
    # Calculate bar positions for side-by-side (clustered) display
    bar_width = 0.3
    x1 = np.array(df['Monomer Length']) - bar_width
    x2 = np.array(df['Monomer Length'])
    x3 = np.array(df['Monomer Length']) + bar_width
    
    # Plot clustered bars on secondary y-axis
    bar1 = ax2.bar(x1, df['Frags-Linear'], width=bar_width, alpha=0.5, color='#b3ecff', label='Frags-Linear')
    bar2 = ax2.bar(x2, df['Frags-Monocyclic'], width=bar_width, alpha=0.5, color='#ffd9b3', label='Frags-Monocyclic')
    bar3 = ax2.bar(x3, df['Frags-Bicyclic'], width=bar_width, alpha=0.5, color='#c2f0c2', label='Frags-Bicyclic')
    
    # Set up secondary y-axis
    ax2.set_ylabel('Number of Fragments', fontsize=12, color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    
    # Add legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    
    # Create a combined legend
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    # Set title and layout
    plt.title('Monomer Length vs Time and Number of Fragments', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Display the plot
    plt.show()
    
    # If you want to save the figure, uncomment this line
    # plt.savefig('length_vs_time_plot.png', dpi=300, bbox_inches='tight')
