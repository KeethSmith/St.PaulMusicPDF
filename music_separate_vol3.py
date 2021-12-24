import PyPDF2
import os
import textract
from PIL import Image
from pdf2image import convert_from_path
import io
import re



vol = "vol3"

with open(f"{vol}.txt", "w") as file:
	pass


src_pdf= PyPDF2.PdfFileReader(open(f"{vol}.pdf", "rb"))

start_page = 42
end_page = 540
# start_page = 119
# end_page = 120
prev_first_page_num = 0
prev_last_page_num = 0
prev_title = "Null"



for page_num in range(start_page,end_page):

	page = src_pdf.getPage(page_num-1)
	text = page.extractText()
	
	# print(text)

	regex = re.compile('[A-Z]^(?!.*page)$[a-z]+[A-Za-z,/ ]+\s.\d{3}|\d{3}\s+[A-Za-z]+.[A-Za-z,/ ]+')
	
	
	
	try:
		title = regex.findall(text)[0]
		if ("Tune:" in title or "Text" in title or "This tune" in title):
			prev_last_page_num = page_num
			continue

		if (re.search(r'[A-Z ]+\s+\d{3}',title)):
			title = re.split('(\d+)', title, maxsplit = 1)[0:2]
			# title_temp = title
			title = ' '.join(reversed(title)).strip()
			# print(f"reversed: {title}:{title_temp}")

		title = title.split()
		title = ' '.join(title)

		# print(title)

		prev_last_page_num = page_num - 1

		
	except:
		prev_last_page_num = page_num
		# print(f"Failed: {page_num}")
		continue

	if (prev_first_page_num == 0):
		prev_first_page_num = page_num
		prev_title = title
		continue

	with open(f"{vol}.txt", "a") as file:
		file.write(f"{prev_first_page_num}-{prev_last_page_num} : {prev_title}\n")


	print(f"{prev_first_page_num}-{prev_last_page_num} : {prev_title}")

	prev_first_page_num = page_num
	prev_title = title

