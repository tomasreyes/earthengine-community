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

"""Earth Engine Developer's Guide examples from 'Reducers - Grouping' section."""

# [START earthengine__reducers10__grouping_image]
# Load a region representing the United States
region = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(
    ee.Filter.eq('country_na', 'United States')
)

# Load MODIS land cover categories in 2001.
landcover = ee.Image('MODIS/051/MCD12Q1/2001_01_01').select(
    # Select the IGBP classification band.
    'Land_Cover_Type_1'
)

# Load nightlights image inputs.
nl_2001 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F152001').select(
    'stable_lights'
)
nl_2012 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012').select(
    'stable_lights'
)

# Compute the nightlights decadal difference, add land cover codes.
nl_diff = nl_2012.subtract(nl_2001).addBands(landcover)

# Grouped a mean reducer: change of nightlights by land cover category.
means = nl_diff.reduceRegion(
    reducer=ee.Reducer.mean().group(groupField=1, groupName='code'),
    geometry=region.geometry(),
    scale=1000,
    maxPixels=1e8,
)

# Print the resultant Dictionary.
display(means)
# [END earthengine__reducers10__grouping_image]
