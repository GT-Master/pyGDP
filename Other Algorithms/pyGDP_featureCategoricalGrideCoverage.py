import pyGDP

shapefile = 'sample:CONUS_States'
attribute = 'STATE'
value = 'Alabama'

dataSetURI = 'http://cida.usgs.gov/ArcGIS/services/statsgo_numid/MapServer/WCSServer'

dataType = '1'

pyGDP.featureCategoricalGridCoverage(shapefile, dataSetURI, dataType, attribute, value)