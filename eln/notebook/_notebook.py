from PyPDF2 import PdfFileMerger
import os

def build_notebook(path, pdfs, filename='notebook.pdf'):

	"""

	Aggregates individual pdf pages into a single multi-page document

	Parameters
	----------
	path : str
	   path to the individual pages of the pdf
	pdfs : list
	   list of the pdf file names e.g. page1.pdf, page2.pdf, etc.
	filename : str, optional
	   name of the generated notebook

	"""

	merger = PdfFileMerger()
	for pdf in pdfs:
		merger.append(pdf)
		os.remove(path + '/' + pdf)
	merger.write(filename)
	merger.close()
