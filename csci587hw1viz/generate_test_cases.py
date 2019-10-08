import random

import shapely.geometry
import shapely.ops

min_lon, min_lat, max_lon, max_lat = 139.49, 35.55, 139.91, 35.76
boundary_error = 0.000001
center_lon = (min_lon + max_lon) / 2
center_lat = (min_lat + max_lat) / 2

test_cases = []
for i in range(0, 10000):
    nn_or_rq = random.choice(['NN', 'RQ'])
    if nn_or_rq == 'NN':
        var = random.randrange(1, 100)
    else:
        var = random.uniform(0.1, 5.0)

    lat = random.uniform(min_lat + boundary_error, max_lat)
    lon = random.uniform(min_lon + boundary_error, max_lon)

    test_cases.append((shapely.geometry.Point(lon, lat), var, nn_or_rq))

with open('my_random_test_cases.txt', 'w') as cases:
    for test_case in test_cases:
        cases.write("{lat} {lon} {var} {query_type}\n".format(
            lat=test_case[0].y,
            lon=test_case[0].x,
            var=test_case[1],
            query_type=test_case[2]
        ))
