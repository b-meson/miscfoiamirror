# PNGs created by running the image through an image converter 
# i.e. convert -density 300 -trim <file>.pdf -quality 100 -sharpen 0x1.0 M <image>.png
# density > 250 leads to poor image recogition. 

#import Image 
import pytesseract 
import ocr_utils

foia_response = '1505deposists2.pdf' 
ocr_utils.split_pdf(foia_response)

num_page_start = 1
num_page_end = 86
all_text = []
data=[]

for page in range(num_page_start, num_page_end + 1):
    indiv_filename = "{}.{}.pdf".format(ocr_utils.get_stem(foia_response), page)

    tmp_filename = indiv_filename
    tmp_image = ocr_utils.convert_to_png(tmp_filename)
    all_text.append(ocr_utils.ocr_image(tmp_image))

data=all_text[0].split('\n')

# for each data set you should read in the amounts 

reviewed=[]
# inputs moved to checkanalysis.py
#for row in data:
#
#    if row.split() == []:    pass
#    else:    
#        inputs.append(row.split()[2])

#print inputs
