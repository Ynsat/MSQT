"""
Contiene constantes que se van a usar durante todo el proceso
"""

import ee
ee.Initialize()

GEE_USER_PATH = ee.data.getAssetRoots()[0]['id']  # Retrieves the user's GEE path to be used for saving assets
