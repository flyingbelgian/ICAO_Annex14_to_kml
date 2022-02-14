string = "12345<start>something</start>678910<start>something else</start>398402"

start = "<start>"
end = "</start>"

first_start = string.split(start)[1]
second_start = string.split(start)[2]

found = first_start.split(end)[0]
also = second_start.split(end)[0]

print(found)
print(also)
