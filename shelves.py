import shelve 
import time

def time_taken(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def retrieve_shelve_data():
    return shelvefile['cats']


def retrieve_dict_data():
    return dictionary['cats']


cats =['Zophie', 'pooka', 'simon'] 

shelvefile = shelve.open("shelf_file") 

shelvefile['cats']= cats

dictionary = { 'cats': cats }

print("Time taken by shelve")
time_taken(retrieve_shelve_data)

print("Time taken by dictionary")
time_taken(retrieve_dict_data)

shelvefile.close()

