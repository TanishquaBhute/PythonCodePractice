thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print("Year:", thisdict["year"])
print(len(thisdict))
print(type(thisdict))
newdict = thisdict.copy()
print(newdict)
print(type(newdict))
x = thisdict.get("name","Mukesh")
print(x)
print(thisdict)
'''print(thisdict.keys())
print(thisdict.pop("colors"))
print(thisdict)
print(thisdict.values())
print(thisdict.clear())
print(thisdict)'''
new = dict.fromkeys(["name","age","add"])
print(new)
print(thisdict.items())
print(thisdict.popitem())
print(thisdict.setdefault("name","Tanishqua"))
print(thisdict)
print(thisdict.update(new))
print(thisdict)
