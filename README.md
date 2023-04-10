# Recursive Floyd Warshall Algorithm

# Overview
The recursive version of the Floyd Warshall algorithm is implemented using three main functions:

floyd_warshall_recursive(graph, dist, i, j, k): The core recursive function that computes the shortest path between nodes i and j considering node k as an intermediate node.

initialize_distance_matrix(graph): Initializes the distance matrix using the input graph.

floyd_warshall(graph): The main function that calls the recursive algorithm and returns the shortest path matrix.
Additionally, the repository includes an imperative implementation of the Floyd Warshall algorithm, floyd_warshall_imperative(graph), for comparison purposes.

# Performance Testing
The script tests the performance of both the recursive and imperative implementations using a sample graph. The execution time is measured and printed for each implementation, as well as the performance difference between the two.

# Unit Testing
The script includes unit tests for the three main functions of the recursive Floyd Warshall implementation using the unittest module:

TestFloydWarshallRecursive: Tests the floyd_warshall_recursive function with a simple graph.
TestInitializeDistanceMatrix: Tests the initialize_distance_matrix function with a simple graph.
TestFloydWarshall: Tests the floyd_warshall function with a sample graph and checks the expected result.

To run the unit tests, execute the script, and the test results will be displayed in the console.

# Usage
Clone or download the repository.
Open a terminal or command prompt in the directory containing the script.
Run the script using Python 3: python recursive_floyd_warshall.py
The script will execute the performance tests and unit tests, and display the results in the console.