# class Trie:
#     def __init__(self) -> None:
#         self.dic = [None for _ in range(26)]
#         self.flag = False
#     def insert(self,word):
#         def insert_char(root,key,i,n):
#             if i==n:
#                 root.flag = True
#                 return
#             idx= ord(key) - ord("a")
#             if root.dic[idx] == None:
#                 root.dic[idx] = Trie()
#             root = root.dic[idx]
#             insert_char(root,word[i+1] if i<n-1 else "",i+1,n)
#         insert_char(self,word[0],0,len(word))
#     def search(self,word):
#         def search_char(root,key,i,n):
#             if i == n:return root.flag
#             idx = ord(key) - ord("a")
#             if root.dic[idx] == None:return False
#             print(key,end="")
#             return search_char(root.dic[idx] ,word[i+1] if i<n-1 else "",i+1,n)
#         return search_char(self,word[0] ,0,len(word))
# trie = Trie()

# trie.insert("hel")
# element_found = trie.search("hel")
# print("\n",element_found)




class Trie:
    def __init__(self) -> None:
        self.dic = {}
        self.flag = False
    
    def insert(self,word):
        t= self
        for i in word:
            if i not in t.dic:
                t.dic[i] = Trie()
            t = t.dic[i]
        t.flag = 1

    def search(self,word):
        t = self
        for i in word:
            
            if i not in t.dic:return False
            t = t.dic[i]
        return t.flag
    def search_prefix(self,word):
        t = self
        for i in word:
            if i not in t.dic:return False
            t = t.dic[i]
        self.display(word,t)
        return 1

    def display(self,word,t):
        def recur(word,node):
            # print(node)
            if node.flag:
                print(word)
                return
            for i in node.dic:
                recur(word+i, node.dic[i])
        recur(word,t)
    def display_pref(self,word):
        def recur(node,word):
            if node.flag:
                print(word)
                return
            for i in node.dic:
                recur(node.dic[i],word+i)
        t = self
        s = ""
        for i in word:
            if i in t.dic:
                s+=i
                t = t.dic[i]
        recur(t,s)
    def max_length(self,word):
        max_length  = 0
        max_str =""
        def recur(node,word,depth):
            nonlocal max_length
            nonlocal max_str
            if node.flag and depth >max_length:
                max_length = depth
                max_str = word
                return
            for i in node.dic:
                recur(node.dic[i],word+i,depth+1)
        t = self
        s = ""
        for i in word:
            if i in t.dic:
                s+=i
                t = t.dic[i]
            else:
                return ""
        recur(t,s,len(word))
        return max_str
            
            
        
trie = Trie()
words= ["apple" ,"word","world","hell"]
for word in words:
    trie.insert(word)
# for word in words:
#    print(f"{word} ", trie.search(word) )
# print("prefix wor in or not " , trie.search_prefix("wor"))
# trie.search_prefix("wo")
# trie.display("wo",None)
# trie.display_pref("he")
prefixes = ["b" ,"ba" ,"wo" ,"ap"]
max_prefix = ""
for i in prefixes:
    cur_max = trie.max_length(i)
    if len(max_prefix) < len(cur_max) or(len(max_prefix) == len(cur_max) and cur_max < max_prefix) :
        max_prefix =  cur_max
print(max_prefix)
