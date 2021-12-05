jokes = []
current_joke = []
# questions = []
# anwsers = []

f = open("readme.md","r")
for line in f:
    if "---" in line:
        jokes.append(current_joke)
        current_joke = []
    else:
        cleaned_line = line.replace("\n","")
        if cleaned_line:
            current_joke.append(cleaned_line)
f.close()
output = open("output.txt",'w')

for joke in jokes:
     output.write(str(joke)+ "\n")
output.close()
    # if "**A:**" in line:
    #     anwsers.append(line.replace("**A:**",""))
    # elif "**Q:**" in line:
    #     questions.append(line.replace("**Q:**",""))


print(jokes)
