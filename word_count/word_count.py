on_mind = input("What's on your mind today?\r\n")
mind_list = on_mind.split()
print(f"Oh nice, you just told me what was on your mind in {len(mind_list)} words.")


with open("word_count.txt",'r') as file:
    doc = file.read()

doc_words = doc.split()
print(f"the length of your file is {len(doc_words)} words")