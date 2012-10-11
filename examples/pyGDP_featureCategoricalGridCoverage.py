import pyGDP

pyGDP = pyGDP.pyGDPwebProcessing()


shapefile = 'sample:CONUS_States'
attribute = 'STATE'
value = 'Alabama'

dataSetURI = 'http://cida.usgs.gov/ArcGIS/services/statsgo_numid/MapServer/WCSServer'

dataType = '1'
file_handle = pyGDP.submitFeatureCategoricalGridCoverage(shapefile, dataSetURI, dataType, attribute, value, verbose=True)