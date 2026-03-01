import re

# Transcribed text from the image
lesson_text = """
Harry doesn't want to be a star chef when he's 20. He wants to be one now. This is why he's on the TV programme Kitchen Kids.

The ten-year-old New Yorker likes cooking. He can make fantastic soups and salads, excellent omelettes and the best cakes. But there are many other children on the show, too. And they are all very good. More and more young people are interested in cooking. Many of them learn it from their parents. Others watch special cooking videos for children. In many cities, there are special cooking classes for young people. Some of them are for children from the age of three!

But what must you do to become a star chef? Of course, it's important that you like cooking and are really good at it. But there are some rules. You must be nine years old or more to be on Kitchen Kids.

'We must wash our hands before we start cooking,' Harry says. 'And of course we mustn't put them in our mouths. A chef doesn't do that! And we must be very careful with hot plates.'

The show starts. Harry is excited. He knows he's an excellent cook. This time he makes tomato soup, some salad, steak and carrot cake. The experts in the studio love Harry's food, and he stays on the show.

It's 5 pm. The show is over. Harry is happy, and a little tired. He goes home. It's time to do his homework.
"""

# Words likely in the TOP 300 (we exclude these)
# This is a refinement to ensure we only get "difficult" words.
top_300_words = set([
    "the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "i", "his", "they",
    "be", "at", "one", "have", "this", "from", "or", "had", "by", "hot", "but", "some", "what", "there", "we", "can", "out", "other",
    "were", "all", "your", "when", "up", "use", "word", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if",
    "will", "way", "about", "many", "then", "them", "would", "write", "like", "so", "these", "her", "long", "make", "thing", "see",
    "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "my", "sound", "no", "most", "number", "who", "over",
    "know", "water", "than", "call", "first", "people", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part",
    "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show",
    "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "much", "great", "think", "say",
    "help", "low", "line", "before", "turn", "cause", "same", "mean", "differ", "move", "right", "boy", "old", "too", "does",
    "tell", "sentence", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand",
    "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men",
    "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother",
    "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer",
    "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "thought", "let", "keep", "eye", "never",
    "last", "door", "between", "city", "tree", "cross", "since", "hard", "start", "might", "story", "saw", "far", "sea", "draw",
    "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few", "stop", "open", "seem", "together",
    "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "often", "always", "music", "those", "both",
    "mark", "book", "letter", "until", "mile", "river", "car", "feet", "care", "second", "enough", "plain", "girl", "usual",
    "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family",
    "direct", "pose", "leave", "song", "measure", "state", "product", "happen", "complete", "ship", "area", "half", "rock",
    "order", "fire", "south", "problem", "piece", "told", "knew", "pass", "top", "whole", "king", "space", "heard", "best"
])

# Extract words from the lesson text
words_in_lesson = re.findall(r'\b\w+\b', lesson_text.lower())

# Filter "difficult words" (not in top 300)
# We want to identify words that are truly uncommon for a 4th grader or are "生僻" (rare/less frequent).
difficult_words = []
seen = set()
for w in words_in_lesson:
    if w not in top_300_words and w not in seen and not w.isdigit():
        difficult_words.append(w)
        seen.add(w)

# Dictionary data with POS, IPA, and Translation
vocab_db = {
    "chef": {"pos": "n.", "ipa": "/ʃef/", "zh": "主厨，厨师"},
    "programme": {"pos": "n.", "ipa": "/ˈprəʊɡræm/", "zh": "（电视）节目"},
    "kitchen": {"pos": "n.", "ipa": "/ˈkɪtʃɪn/", "zh": "厨房"},
    "yorker": {"pos": "n.", "ipa": "/ˈjɔːkə/", "zh": "纽约人（New Yorker）"},
    "cooking": {"pos": "n.", "ipa": "/ˈkʊkɪŋ/", "zh": "烹饪，做饭"},
    "fantastic": {"pos": "adj.", "ipa": "/fænˈtæstɪk/", "zh": "极好的，了不起的"},
    "soup": {"pos": "n.", "ipa": "/suːp/", "zh": "汤"},
    "salad": {"pos": "n.", "ipa": "/ˈsæləd/", "zh": "沙拉"},
    "excellent": {"pos": "adj.", "ipa": "/ˈeksələnt/", "zh": "卓越的，杰出的"},
    "omelette": {"pos": "n.", "ipa": "/ˈɒmlət/", "zh": "煎蛋卷"},
    "cake": {"pos": "n.", "ipa": "/keɪks/", "zh": "蛋糕"},
    "interested": {"pos": "adj.", "ipa": "/ˈɪntrəstɪd/", "zh": "感兴趣的"},
    "special": {"pos": "adj.", "ipa": "/ˈspeʃl/", "zh": "特殊的，专门的"},
    "video": {"pos": "n.", "ipa": "/ˈvɪdiəʊ/", "zh": "视频"},
    "become": {"pos": "v.", "ipa": "/bɪˈkʌm/", "zh": "成为"},
    "important": {"pos": "adj.", "ipa": "/ɪmˈpɔːtnt/", "zh": "重要的"},
    "rule": {"pos": "n.", "ipa": "/ruːl/", "zh": "规则"},
    "wash": {"pos": "v.", "ipa": "/wɒʃ/", "zh": "洗，清洗"},
    "mouth": {"pos": "n.", "ipa": "/maʊθ/", "zh": "嘴巴"},
    "careful": {"pos": "adj.", "ipa": "/ˈkeəf(ə)l/", "zh": "小心的，仔细的"},
    "plate": {"pos": "n.", "ipa": "/pleɪt/", "zh": "盘子"},
    "excited": {"pos": "adj.", "ipa": "/ɪkˈsaɪtɪd/", "zh": "兴奋的"},
    "tomato": {"pos": "n.", "ipa": "/təˈmɑːtəʊ/", "zh": "西红柿"},
    "steak": {"pos": "n.", "ipa": "/steɪk/", "zh": "牛排"},
    "carrot": {"pos": "n.", "ipa": "/ˈkærət/", "zh": "胡萝卜"},
    "expert": {"pos": "n.", "ipa": "/ˈekspɜːt/", "zh": "专家"},
    "studio": {"pos": "n.", "ipa": "/ˈstjuːdiəʊ/", "zh": "工作室，演播室"},
    "tired": {"pos": "adj.", "ipa": "/ˈtaɪəd/", "zh": "疲倦的，累的"},
    "homework": {"pos": "n.", "ipa": "/ˈhəʊmwɜːk/", "zh": "家庭作业"},
}

# Mapping lesson words to dictionary entries (handling plurals etc.)
final_list = []
for word in difficult_words:
    entry = None
    if word in vocab_db:
        entry = vocab_db[word]
    elif word.endswith('s') and word[:-1] in vocab_db:
        entry = vocab_db[word[:-1]]
    elif word.endswith('es') and word[:-2] in vocab_db:
        entry = vocab_db[word[:-2]]
    elif word.endswith('ies') and word[:-3] + 'y' in vocab_db:
        entry = vocab_db[word[:-3] + 'y']
    
    if entry:
        final_list.append((word, entry))

print("| 英文原文 | 词性 | 音标 | 中文翻译 |")
print("| :--- | :--- | :--- | :--- |")
for word, info in final_list:
    print(f"| {word} | {info['pos']} | {info['ipa']} | {info['zh']} |")
