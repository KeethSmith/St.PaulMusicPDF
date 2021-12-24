import PyPDF2
import os
import textract
from PIL import Image
from pdf2image import convert_from_path
import io
import re



# Open PDF Source #
# app_path = os.path.dirname(__file__)




vol = "vol1"

with open(f"{vol}.txt", "w") as file:
	pass

# pil_image_lst = convert_from_path(f"{vol}.pdf") # This returns a list even for a 1 page pdf
# pil_image = pil_image_lst[0]


# src_pdf= PdfFileReader(open(os.path.join(app_path, "../../../uploads/%s" % filename), "rb"))
src_pdf= PyPDF2.PdfFileReader(open(f"{vol}.pdf", "rb"))
# for x in range(src_pdf.getNumPages()):
start_page = 52
end_page = 461
prev_first_page_num = 0
prev_last_page_num = 0
prev_title = "Null"


class X():
	pass

prev = X()
prev.first_page = 0
prev.last_page = 0
prev.title = ""

current = X()
current.first_page = 0
current.last_page = 0
current.title = ""



for page_num in range(start_page,end_page):

	page = src_pdf.getPage(page_num-1)
	text = page.extractText()
	
	# print(text)
# 
	# exit()
	# print(text.split('\n'))
	
	
	
	try:
		text = text.split('\n')[-3] + "\n" + text.split('\n')[-2] + "\n" + text.split('\n')[-1]
		regex = re.compile('\w+\s\d+: \D+')
		# print(text)
		# print(text.split('\n')[-1] + " " + text.split('\n')[-2] + " " + text.split('\n')[-3])
		title = regex.findall(text)[-1]
		# print(title)
		title = title.split(':')[-1].strip().replace('\n', '').replace('  ', ' ').split('  ')[0]
		# print(title)

		
	except:
		prev_last_page_num = page_num
		# print(f"Failed: {page_num}")
		continue

	with open(f"{vol}.txt", "a") as file:
		file.write(f"{prev_first_page_num}-{prev_last_page_num} : {prev_title}\n")


	print(f"{prev_first_page_num}-{prev_last_page_num} : {prev_title}")

	prev_first_page_num = page_num
	prev_title = title

