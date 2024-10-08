# Copyright 2023 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_geometry_closestPoint]
# Define a Geometry object.
geometry = ee.Geometry({
    'type': 'Polygon',
    'coordinates': [[
        [-122.081, 37.417],
        [-122.086, 37.421],
        [-122.084, 37.418],
        [-122.089, 37.416],
    ]],
})

# Define other inputs.
input_geom = ee.Geometry.Polygon(
        [[[-122.068, 37.418],
          [-122.068, 37.416],
          [-122.064, 37.416],
          [-122.064, 37.418]]])

# Apply the closestPoints method to the Geometry objects.
closest_points = ee.Dictionary(
    geometry.closestPoints(right=input_geom, maxError=1)
)

# Print the result.
display('geometry.closestPoints(...) =', closest_points)

# There is also a one-sided API for convenience.
closest_point_on_input_geom = geometry.closestPoint(
    right=input_geom, maxError=1
)
display('geometry.closestPoint(...) =', closest_point_on_input_geom)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m.add_layer(
    closest_points.getGeometry('left'),
    {'color': 'red'},
    'Result [red]: closest_point_on_left',
)
m.add_layer(
    closest_points.getGeometry('right'),
    {'color': 'red'},
    'Result [red]: closest_point_on_right',
)
m
# [END earthengine__apidocs__ee_geometry_closestPoint]
