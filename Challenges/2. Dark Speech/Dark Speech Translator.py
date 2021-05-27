from tkinter import *
from centerit import *

def darkify(line):
	new_line = ""
	words = line.split(" ")
	for word in words:
		if (word[0].isupper()) and (word.isalpha()) and '"' not in word:
			word = word.lower()[:-1] + word[-1].upper()
			new_word = word[::-1]

		elif (word[0].isupper()) and word.isalpha() == False and '"' not in word:
			new_word = (word.lower()[:-2] + word[-2].upper())[::-1] + word[-1]
			
		elif word.isalpha():
			new_word = word[::-1]
		
		elif "'" in word and '"' not in word:
			new_word = word[::-1]

		elif '"' in word:
			if word[0] == '"' and word[-1] == '"':
				word = word[1:-1]
				if (word[0].isupper()) and (word.isalpha()) and '"' not in word:
					word = word.lower()[:-1] + word[-1].upper()
					new_word = word[::-1]

				elif (word[0].isupper()) and word.isalpha() == False and '"' not in word:
					new_word = (word.lower()[:-2] + word[-2].upper())[::-1] + word[-1]
					
				elif word.isalpha():
					new_word = word[::-1]
				
				elif "'" in word and '"' not in word:
					new_word = word[::-1]

				else:
					new_word = word[:-1][::-1] + word[-1]

				new_word = '"' + new_word + '"'

			elif word[0] == '"' and (word[1:].isalpha()) and (word[1].islower()):
				new_word = word[0] + word[1:][::-1]

			elif word[-1] == '"' and (word[:-1].isalpha()) and (word[0].islower()):
				new_word = word[:-1][::-1] + word[-1]

			elif word[0] == '"' and (word[1].islower()) and "'" not in word:
				new_word = word[0] + word[1:-1][::-1] + word[-1]
				
			elif word[-1] == '"' and (word[0].islower() and "'" not in word):
				new_word = word[:-2][::-1] + word[-2:]

			elif word[0] == '"' and (word[1].islower()) and (word.replace("'", "").replace('"', "").isalpha()):
				new_word = word[0] + word[1:][::-1]

			elif word[-1] == '"' and (word[0].islower()) and (word.replace("'", "").replace('"', "").isalpha()):
				new_word = word[:-1][::-1] + word[-1]

			elif word[0] == '"' and (word[1].islower()):
				new_word = word[0] + word[1:-2][::-1] + word[-1]

			elif word[-1] == '"' and (word[0].islower()):
				new_word = word[:-2][::-1] + word[-2:]

#================================================================
			elif word[0] == '"' and (word[1:].isalpha()):
				new_word = word.lower()[:-1] + word[-1].upper()
				
			elif word[-1] == '"' and (word[:-1].isalpha()):
				new_word = (word.lower()[:-2] + word.upper()[-2])[::-1] + word[-1]

			elif word[0] == '"' and "'" not in word:
				new_word = word[0] + (word[1:-2].lower() + word[-2].upper())[::-1] + word[-1]

			elif word[-1] == '"' and "'" not in word:
				new_word = (word[:-3].lower() + word[-3].upper())[::-1] + word[-2:]
				
			elif word[0] == '"' and (word.replace("'", "").replace('"', "").isalpha()):
				new_word = word[0] + (word[1:-1].lower() + word[-1].upper())[::-1]

			elif word[-1] == '"' and (word.replace("'", "").replace('"', "").isalpha()):
				new_word = (word[:-2].lower() + word[-2].upper())[::-1] + word[-1]

			elif word[0] == '"':
				new_word = word[0] + (word[1:-2].lower() + word[-2].upper())[::-1] + word[-1]

			elif word[-1] == '"':
				new_word = (word[:-3].lower() + word[-3].upper())[::-1] + word[-2:]

		else:
			new_word = word[:-1][::-1] + word[-1]

		new_line += new_word + " "	
	return new_line

def get_original():
	result = ""
	input = text_field_input.get("1.0", "end-1c")
	lines = input.split("\n")

	for line in lines:
		if len(line) > 0:
			result += darkify(line) + "\n"
		else:
			result += "\n"

	text_field_result.delete("1.0", END)
	text_field_result.insert("1.0", result)

		

text_bg = '#555555'

window = Tk()
text1 = Label(
	window,
	text='Welcome Dark Lord, to the Dark Speech Machine',
	fg='#ff0000',
	width=50,
	height=2
	).pack()

text_field_input = Text(
	window,
	fg='red',
	bg=text_bg,
	width=60,
	height=10
	)
text_field_input.pack()

convert_button = Button(
	window,
	command=lambda: get_original(),
	text='Convert to Dark Speech',
	width=20,
	height=2,
	bg='gray',
	fg='red'
	)
convert_button.pack()

text_field_result = Text(
	window,
	fg='red',
	bg=text_bg,
	width=60,
	height=10
	)
text_field_result.pack()

centertk(window, 560, 430)
window.mainloop()
