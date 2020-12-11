import settings
import requests
import json
import base64
from tqdm import tqdm


# Querying products paging results:
# 1 item for page
# --------------------------------

url = settings.SERVICE_URL + settings.OB_PATH_PRODUCTS + '?' + settings.OB_TPL_PAGING.format(0, 1)


response = requests.get(url)

#controlliamo che non ci siano errori nella risposta e nel caso stampiamo a video i messaggio
if response.status_code != 200:
    raise Exception(f'Status Code: {response.status_code}, err msg: {response.content}')


jresponse = json.loads(response.content)

# verifico che mi restituisca effettivamente un elemento solo
assert len(jresponse['value']) == 1


# recupero il primo ed unico elemento
# -----------------------------------
product = jresponse['value'][0]
for k, v in product.items():
    print (f'{k}: {v}')

# salviamo la quicklook sul server
# --------------------------------
if 'quicklook' in product and product['quicklook']:
    with open(f"images/quicklook_{product['id']}.png", "wb") as fh:
        fh.write(base64.decodebytes(str.encode(product['quicklook'])))
else:
    print (f"No 'quicklook' data available for product {product['id']}")


# facciamo il download della risorsa se disponibile
# -------------------------------------------------
if product['downloadable']:
    url = settings.SERVICE_URL + settings.OB_PATH_PRODUCTS_DOWNLOAD.format(product['id'])
    file_path = f"downloads/f{product['name']}"

    max = int(product['size'] / 1024)
    counter = 0
    pbar = tqdm(total=max-1)
    with requests.get(url, stream=True, auth=(settings.OB_USERNAME, settings.OB_PASSWORD)) as response:
        response.raise_for_status()
        with open(file_path, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                pbar.update(counter)
                out_file.write(chunk)
                counter += 1
        #logger.info('Download finished successfully')

