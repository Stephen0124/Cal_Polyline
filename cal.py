import math

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def polyline_length(coordinates):
    total_length = 0.0
    for i in range(len(coordinates) - 1):
        total_length += euclidean_distance(coordinates[i], coordinates[i + 1])
    return total_length

def parse_coordinates(data):
    coordinates = []
    coord_strs = data.split('][')
    for coord_str in coord_strs:
        coord_str = coord_str.strip('[').strip(']')
        coords = [float(coord) for coord in coord_str.split(',')]
        coordinates.append(coords)
    return coordinates

def main(data):
    coordinates = parse_coordinates(data)
    total_length = polyline_length(coordinates)/100
    return("%.2f"%total_length)