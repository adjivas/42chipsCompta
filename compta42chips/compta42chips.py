#!/usr/bin/env python

import json
import pyFarnell

f = pyFarnell.Farnell(apiKey='secret', region='fr.farnell.com')
dp = json.loads(f.get_part_number('2507703', part={
                   'resultsSettings.responseGroup': '{Prices}',
                   'resultsSettings.refinements.filters': '{rohsCompliant,inStock}',
                 }).get('_content')).get('premierFarnellPartNumberReturn')

assert(dp.get("numberOfResults") == 1)

product0 = dp.get("products")[0]

assert(product0.get("productStatus") == "STOCKED")
assert(product0.get("rohsStatusCode") == "YES_YES")

datasheet0 = product0.get("datasheets")[0]
prices = product0.get("prices")

print("Datasheet", datasheet0.get("url"))
print("Description", product0.get("displayName"))
print("Fabricant", product0.get("brandName"))
print("RefFabricant", product0.get("translatedManufacturerPartNumber"))
print("Fournisseur", "Farnell")
print("RefFournisseur", product0.get("sku"))
print("costFournisseur", prices)
print("deviceFournisseur", "EUR")
