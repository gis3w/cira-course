from local_settings import *

# ENDPOINT SERVICE
# ================
SERVICE_URL = 'https://catalogue.onda-dias.eu/dias-catalogue/'
OB_PATH_PRODUCTS = 'Products'
OB_PATH_PRODUCTS_DOWNLOAD = 'Products({})/$value'


# QUERY TEMPLATES
# ===============
OB_TPL_METADATA = "$expand=Metadata"
OB_TPL_PAGING = "$skip={}&$top={}"

# Subset searching templates
# --------------------------
OB_TPL_SEARCHING_TIME_FROM = "beginPosition:[{}]"
OB_TPL_SEARCHING_TIME_TO = "endPosition:[{}]"
