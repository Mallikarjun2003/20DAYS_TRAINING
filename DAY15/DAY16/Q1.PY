# ip : number of queries 5
# 1 school
# 1 world
# 1 word
# 1 scholar
# 2 word
# 3 sch
# 1 is insert the word  return none
# 2 is search for the word prints true if there else print false
# 3 seacrches for the prefix given

class List:
    def __init__(self):
        self.words = set()
    def insert(self,word):
        self.words.add(word)
    def search(self,word):
        if word in self.words:return True
        return False
    def search_prefix(self,word):
        for w in self.words:
            if w.startswith(word):return True
        return False
    def search_prefix_count(self,word):
        p_count = 0
        for w in self.words:
            if w.startswith(word):p_count +=1
        return p_count
    def delete(self,word):
        self.words.discard(word)

t = int(input())
words_list = List()
for _ in range(t):
    i ,word = input().split()
    if i == "1":words_list.insert(word)
    elif i == "2":
        print(f"{word}  ",words_list.search(word))
    elif i == "3":
        print(f"{word}",words_list.search_prefix(word))
    elif i == "4":
        print(f"{word}" ,"is repeated ",words_list.search_prefix_count(word))
    else:
        words_list.delete(word)
