# PNGs created by running the image through an image converter 
# i.e. convert -density 300 -trim <file>.pdf -quality 100 -sharpen 0x1.0 M <image>.png
# density > 250 leads to poor image recogition. 

# depends on tesseract-ocr and tesseract-devvel nd leptonica to run properly

import ocr_utils
import numpy

png_response = '1505deposists2.1.png'

all_text=[]
all_text.append(ocr_utils.ocr_image(png_response))

data=all_text[0].split('\n')

# for each data set you should read in the amounts 
inputs=[]
for row in data:
    if row.split() == []:    pass
    try:    
        inputs.append(row.split()[2])
    except IndexError:
        inputs.append('null')
# check which checks require review and mark them for review
review=[]
# create new array and flag which amounts require review
# afterwards, remove paranthesis to get purely dollar amounts

char_remove = ['(', '$', ')']
outputs = []
for amounts in inputs:
    amounts = str(amounts)
    if (amounts[:2]=='(0' or amounts=='($1,') or amounts[0]=='3':
        review_status = True
    else:
        review_status = False

    for char in char_remove:
	amounts = amounts.replace(char, '')
    outputs.append( (amounts, review_status) )

dates=[]
for row in data:
    if row.split() == []:    pass
    else:
        dates.append(row.split()[0])

# sanity check the data is complete 
# print len(dates)
# print len(inputs)
# print len (review)
print outputs


# Output data into txt file
newfile=png_response[:-4]
print "Outputting data in " + newfile
target = open(newfile,'w')
finaldata=str(outputs)
target.write(finaldata)
target.write("\n")
target.close()
