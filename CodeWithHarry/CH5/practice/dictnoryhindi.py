words={
    "hello": "नमस्ते",
    "world": "दुनिया",
    "python": "पाइथन",
    "programming": "कार्यक्रमिंग"
}
word=input("What you want meaning of: ")
print(words.get(word, "Word not found"))