from difflib import SequenceMatcher
s1="Python lab"
s2="Python lsb" 
sim=SequenceMatcher(None,s1,s2).ratio()
print("original stmt:")
print(s1)
print(s2)
print("similarities")
print(sim)