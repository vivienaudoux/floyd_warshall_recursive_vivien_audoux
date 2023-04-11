# Recursive Floyd Warshall Algorithm

# Overview
The recursive version of the Floyd Warshall algorithm is implemented using three main functions in the functions.py file:

1) floyd_warshall_recursive(graph, dist, i, j, k): The core recursive function that computes the shortest path between nodes i and j considering node k as an intermediate node.
2) initialize_distance_matrix(graph): Initializes the distance matrix using the input graph.
3) floyd_warshall(graph): The main function that calls the recursive algorithm and returns the shortest path matrix.

Additionally, the repository includes an imperative implementation of the Floyd Warshall algorithm, floyd_warshall_imperative(graph), for comparison purposes. The code of this imperative implementation is copy/pasted from https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

# Performance Testing
The script floyd_warshall_performance_test tests the performance of both the recursive and imperative implementations using a sample graph. The execution time is measured and printed for each implementation, as well as the performance difference between the two.

# Unit Testing
The script floyd_warshall_recursive_unittest includes unit tests for the three main functions of the recursive Floyd Warshall implementation using the unittest module:

1) TestFloydWarshallRecursive: Tests the floyd_warshall_recursive function with a simple graph.
2) TestInitializeDistanceMatrix: Tests the initialize_distance_matrix function with a simple graph.
3) TestFloydWarshall: Tests the floyd_warshall function with a sample graph and checks the expected result.

To run the unit tests, execute the script, and the test results will be displayed in the console.

# Usage
1) Clone or download the repository.
2) Open a terminal or command prompt in the directory containing the script.
3) Run the script of your choice using Python 3: python file_name.py
The script will execute the performance tests or unit tests, and display the results in the console.
