text = open ('Trifelios/trifelios.txt','r')

for line in text:
    line = line.split("-")
    comparison = line[0]
    reference = line[1].replace('\n',"")
        
    if reference in comparison*2 and reference != comparison:
        print("Es trifelio")
    else:
        print("No es trifelio")    

text.close()