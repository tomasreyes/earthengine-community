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

# [START earthengine__reducers09__grouping_fc]
# Load a collection of US census blocks.
blocks = ee.FeatureCollection('TIGER/2010/Blocks')

# Compute sums of the specified properties, grouped by state code.
sums = blocks.filter(
    ee.Filter.And(
        ee.Filter.neq('pop10', None), ee.Filter.neq('housing10', None)
    )
).reduceColumns(
    selectors=['pop10', 'housing10', 'statefp10'],
    reducer=ee.Reducer.sum()
    .repeat(2)
    .group(groupField=2, groupName='state-code'),
)

# Print the resultant Dictionary.
display(sums)
# [END earthengine__reducers09__grouping_fc]
