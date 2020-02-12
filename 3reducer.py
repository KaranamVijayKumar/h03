s = open("02.txt","r")
r = open("r.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  store, amount = data

  if store != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

d = dict((line.strip().split('	') for line in open("r.txt")))
#print(d)
# print(max(d.keys()))

#print(max(zip(d.values(),d.keys())))
#print(d["Austin"])
abc = list((d.values()))
newList = []
for each in abc:
  newList.append(float(each))


maxValue = min((newList))
#print(maxValue)
keyValue = "" 
for key, value in d.items():
  if float(value) == maxValue:
    keyValue = key
    break
print(keyValue,' : ',maxValue)

#print(max(d, key=d.get))

#for key value in d:


# a_dictionary = {"a": 1, "b": 2, "c": 3}
# max_key = max(d, key=d.get)
# print(max_key)

# max_key = max(d, key=d.get)
# print(max_key)