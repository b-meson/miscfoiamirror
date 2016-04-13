import os
import sys
import subprocess
from PIL import Image
import pytesseract
import PyPDF2


"""
Some codes I use for processing horribly formatted FOIA
documents I receive. 
"""

def get_stem(filename):
    return filename.rstrip('.pdf')


def split_pdf(filename):
    """Take a PDF and split it into individual PDFs and saves them
    as {filename}.{pageno}.pdf
    
    Args:
        filename: String corresponding to the initial PDF
        
    Returns:
        None
    """
    pdfsplitcmd = 'gs -sDEVICE=pdfwrite -dSAFER -o {}.%d.pdf {}'.format(
        get_stem(filename), filename)
    subprocess.call(pdfsplitcmd, shell=True)
    
    return None


def rotate_pdf(filename, rotation_angle=270):
    """Take a PDF, rotate it and saves as {filename}_rotated.pdf
    
    Args: 
        filename: String, input PDF file
        rotation_angle: Integer, optional
        
    Returns:
        result_filename: String, output PDF file
    """

    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)
    pageObj.extractText()
    pageObj.rotateClockwise(rotation_angle)

    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(pageObj)
    result_filename = '{}_rotated.pdf'.format(get_stem(filename))
    resultPdfFile = open(result_filename, 'wb')
    pdfWriter.write(resultPdfFile)

    resultPdfFile.close()
    pdfFileObj.close()
    
    return result_filename


def convert_to_png(filename):
    """Convert a PDF to a PNG
    
    Args:
        filename: String, input PDF file
    
    Returns:
        result_filename: String, output PDF file
    """

    pdfconvertcmd = 'gs -sDEVICE=pngalpha -r400 -o {}.png {}'.format(
        get_stem(filename), filename)
    result_filename = '{}.png'.format(get_stem(filename))
    subprocess.call(pdfconvertcmd, shell=True)
    
    return result_filename


def ocr_image(filename):
    """Convert an image to text
    
    Args:
        filename: String, input PDF file
    
    Returns:
        text: String, output text
    """

    im = Image.open(filename)
    text = pytesseract.image_to_string(im)
    
    return text
