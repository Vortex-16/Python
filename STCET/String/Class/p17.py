record='Dr. Crazy*1987-8-23*2032-11-24'
fields=record.split("*")
print(fields)

born=fields[1].split("-")
print(born)

died=fields[2].split("-")
print(died)

print("Lived about: ",int(died[0])-int(born[0]),"years")