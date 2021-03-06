import json, os
import shutil


quote_text = "quotes_output"

with open("quotes.json", 'r') as quotes_file:
	data = json.load(quotes_file)

if os.path.exists(quote_text):
	shutil.rmtree(quote_text)

os.mkdir(quote_text) 
os.chdir(quote_text) 
print("Created quote_text", quote_text)

for node in data:
	corrected_author = node["author"] if node["author"] is not None else "Unknown"
	dir_name = corrected_author.replace(" ", "_")
	os.mkdir(dir_name) if not os.path.exists(dir_name) else print("{} already exists".format(dir_name))
	os.chdir(dir_name)
	ls=os.listdir()
	if not ls:
		out = open("quote.txt", "w")
		out.write(node["text"])
		out.write("\n\n")
		out.close()
	else:
		f="qoute_"+str(len(ls)+1)+".txt"
		out = open(f, "w")
		out.write(node["text"])
		out.write("\n\n")
		out.close()	
	
	os.chdir("..") 
 