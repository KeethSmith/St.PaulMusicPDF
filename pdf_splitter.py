import PyPDF2
import os
import textract
import io
import re


vol = "vol6"

src_pdf= PyPDF2.PdfFileReader(open(f"{vol}.pdf", "rb"))


with open(f"{vol}.txt", "r",encoding='utf-8-sig') as file:
	text = file.readlines()
	# print(text[0].strip())

if not os.path.exists(f'{vol}'):
	os.makedirs(f'{vol}')

for sub_text in text:
	
	sub_text = sub_text.strip()
	split_text = sub_text.split(' : ')
	first_page = int(split_text[0].split('-')[0])
	last_page = int(split_text[0].split('-')[1])
	orig_title = split_text[1]
	title = re.split('(\d+)', orig_title, maxsplit = 1)[-1].strip()
	title_num = re.split('(\d+)', orig_title, maxsplit = 1)[-2].strip()
	# print(title_num, title)
	# exit()


	writer = PyPDF2.PdfFileWriter()

	if (first_page == last_page):
		writer.addPage(src_pdf.getPage(first_page-1))

	else:
		for x in range(first_page, last_page+1):
			writer.addPage(src_pdf.getPage(x-1))

	
	with open(f'{vol}/{title} - {title_num} - G4.pdf', 'wb') as outfile:
		writer.write(outfile)



	# print(f'{first_page} : {last_page} : {title}')

	# exit()



# exit()
