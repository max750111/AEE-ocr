import difflib
str1 = "have to drag you kicking and"
str2 = "to drag me kicking and"

print(difflib.SequenceMatcher(None, str1, str2).quick_ratio())
