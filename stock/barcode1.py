import barcode
import random
import os,sys
from barcode.writer import ImageWriter

path = '../media/media/'




ean = barcode.get('Code39', '123456789102A', writer=ImageWriter())
filename = ean.save(path+'Code39')
