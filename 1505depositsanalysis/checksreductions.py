# PNGs created by running the image through an image converter 
# i.e. convert -density 300 -trim <file>.pdf -quality 100 -sharpen 0x1.0 M <image>.png
# density > 250 leads to poor image recogition. 

import ocr_utils
import numpy

foia_response = '1505deposists1.1.pdf' 
png_response = '1505deposists1.1.png'

all_text=[]
all_text.append(ocr_utils.ocr_image(png_response))

data=all_text[0].split('\n')

# for each data set you should read in the amounts 
inputs=[]
for row in data:
    if row.split() == []:    pass
    else:    
        inputs.append(row.split()[2])
print inputs 

# check which checks require review and mark them

review=[]
# create new array and flag which amounts require review
for amounts in inputs:
    if (amounts[:2]=='13' or amounts[:2]=='16' or amounts[:2]=='18' or amounts[:2]=='($') or amounts[:2]=='(3':
        review.append('True')
    else: review.append('False')

totals=numpy.concatenate([inputs,review], axis=1)
print totals[:,None].shape
