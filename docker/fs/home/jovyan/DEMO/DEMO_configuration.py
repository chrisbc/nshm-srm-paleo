## Configuration

#LAYER_ID = "WellWHV_2019-10-21"
LAYER_ID = "AhuririR_2019-10-21"
LAYER_FILE = "/demo-data/%s.hdf5" % LAYER_ID

# GEOJSON_FILE = '/demo-data/nz-regions-simple.json'
GEOJSON_FILE = '/demo-data/nz-ta-simple.json'
GEOJSON_KEY_ID = 'TA2020_V1_' # 'REGC2016'

ASSET_SAMPLE = int(1e4) #1e5
SITE_SAMPLE = int(1e4) #int(2e4) #0 #int(1e5) #4