import os
import re
import urllib
from multiprocessing import Process
SUPPORTED_FORMATS=['jpg','png','JPEG']
URL_TEMPLATE=r'https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=15#'
