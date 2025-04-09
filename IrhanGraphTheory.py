#Name: Irhan Iftikar
#Date: April 2025
#Description: Hamiltonian Circuit - Discrete Mathematics
#Assumes the "cost" of travel between two cities is the distance between them, in kilometers

#Imports itertools library and defines list of cities in the graph
import itertools
cities = ["New York", "Amsterdam", "Oslo", "Copenhagen", "Milan", "Istanbul"]

#Distance matrix that contains the distance between each pair of cities (in kms)
distance = [
    [0, 5850, 5920, 6180, 6450, 8000],
    [5850, 0, 960, 620, 830, 2200],
    [5920, 960, 0, 480, 1600, 2450],
    [6180, 620, 480, 0, 1150, 2200],
    [6450, 830, 1600, 1150, 0, 1700],
    [8000, 2200, 2450, 2200, 1700, 0]
]

#Function that calculates the total distance of a round trip
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]
    total += distance[route[-1]][route[0]]
    return total

#Arbitraily chooses an extreme number as the shortest distance
shortest_distance = 99999999
best_route = []

#For loop that uses the brute force method to find the optimal path
count = 1
for order in itertools.permutations([1, 2, 3, 4, 5]):
    route = [0] + list(order)
    current_distance = total_distance(route)
    route_names = [cities[i] for i in route] + [cities[route[0]]]
    print(f"{count}. {' --> '.join(route_names)} | Distance: {current_distance} kms")
    count += 1

    if current_distance < shortest_distance:
        shortest_distance = current_distance
        best_route = route

#Prints most efficient route of the brute force method
print("\nMost Efficient Route / Hamiltonian Circuit:")
for i in best_route:
    print(cities[i], end=" --> ")
print(cities[best_route[0]])
print(f"Distance: {shortest_distance} kms")