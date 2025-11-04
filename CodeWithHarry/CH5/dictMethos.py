marks= {
    "Vikash": 100,
    "Divya": 98,
    "Sakshi": 100,
    0:"Vikash"
}
#print(marks,type(marks))
#print(marks["Divya"]) // return error vs # print(marks.get("Vikash"))
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get()) print none
marks.update({"Vikash": 99})
print(marks)