# Copyright 2024 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Earth Engine Developer's Guide examples from 'Reducers - reduceNeighborhood' section."""

# [START earthengine__reducers04__reduce_neighborhood]
# Define a region in the redwood forest.
redwoods = ee.Geometry.Rectangle(-124.0665, 41.0739, -123.934, 41.2029)

# Load input NAIP imagery and build a mosaic.
naip_collection = (
    ee.ImageCollection('USDA/NAIP/DOQQ')
    .filterBounds(redwoods)
    .filterDate('2012-01-01', '2012-12-31')
)
naip = naip_collection.mosaic()

# Compute NDVI from the NAIP imagery.
naip_ndvi = naip.normalizedDifference(['N', 'R'])

# Compute standard deviation (SD) as texture of the NDVI.
texture = naip_ndvi.reduceNeighborhood(
    reducer=ee.Reducer.stdDev(), kernel=ee.Kernel.circle(7)
)

# Display the results.
m = geemap.Map()
m.center_object(redwoods, 12)
m.add_layer(naip, {}, 'NAIP input imagery')
m.add_layer(
    naip_ndvi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, 'NDVI'
)
m.add_layer(texture, {'min': 0, 'max': 0.3}, 'SD of NDVI')
m
# [END earthengine__reducers04__reduce_neighborhood]
