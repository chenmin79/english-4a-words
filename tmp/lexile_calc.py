import re

text = """
Harry doesn't want to be a star chef when he's 20. He wants to be one now. This is why he's on the TV programme Kitchen Kids.

The ten-year-old New Yorker likes cooking. He can make fantastic soups and salads, excellent omelettes and the best cakes. But there are many other children on the show, too. And they are all very good. More and more young people are interested in cooking. Many of them learn it from their parents. Others watch special cooking videos for children. In many cities, there are special cooking classes for young people. Some of them are for children from the age of three!

But what must you do to become a star chef? Of course, it's important that you like cooking and are really good at it. But there are some rules. You must be nine years old or more to be on Kitchen Kids.

'We must wash our hands before we start cooking,' Harry says. 'And of course we mustn't put them in our mouths. A chef doesn't do that! And we must be very careful with hot plates.'

The show starts. Harry is excited. He knows he's an excellent cook. This time he makes tomato soup, some salad, steak and carrot cake. The experts in the studio love Harry's food, and he stays on the show.

It's 5 pm. The show is over. Harry is happy, and a little tired. He goes home. It's time to do his homework.
"""

def estimate_lexile(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    num_sentences = len(sentences)
    
    words = re.findall(r'\b\w+\b', text.lower())
    num_words = len(words)
    
    # Calculate average sentence length (ASL)
    asl = num_words / num_sentences if num_sentences > 0 else 0
    
    # Calculate average syllables per word (ASW) - A rough approximation
    def count_syllables(word):
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count
    
    syllables = sum(count_syllables(w) for w in words)
    asw = syllables / num_words if num_words > 0 else 0
    
    # Flesch-Kincaid Grade Level formula
    fkgl = 0.39 * asl + 11.8 * asw - 15.59
    
    # Approximate Lexile mapping from FKGL (Lexile = 500 * ln(FKGL) or similar rough conversion)
    # Simple mapping: Grade 1 ~ 200L, Grade 2 ~ 400L, Grade 3 ~ 500L, Grade 4 ~ 600L, etc.
    if fkgl <= 0:
        lexile = 100
    else:
        lexile = int(round(min(max(fkgl * 150 + 100, 100), 1300), -1)) # Round to nearest 10
        
    return num_words, num_sentences, asl, asw, fkgl, lexile

words, sentences, asl, asw, fkgl, lexile = estimate_lexile(text)

print(f"Total Words: {words}")
print(f"Total Sentences: {sentences}")
print(f"Average Sentence Length: {asl:.2f}")
print(f"Average Syllables per Word: {asw:.2f}")
print(f"Flesch-Kincaid Grade Level: {fkgl:.1f}")
print(f"Estimated Lexile Range: {lexile-50}L - {lexile+50}L")
