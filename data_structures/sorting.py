from operator import itemgetter


l = ["hello", "HELP", "Helo"]
l.sort()
print(l)
l.sort(key=str.lower)
print(l)

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1))
print(l)