import shelve

with shelve.open("Zaidan") as db:
    print("ISI DALAM SHELVE:")
    for k in db:
        print(k, ":", db[k])