def palindrome_checker(s):
 list(s)
 rev = reversed(s)
 rev="".join(rev)
 if rev == s:
   print("True")
 else:
   print('No')
