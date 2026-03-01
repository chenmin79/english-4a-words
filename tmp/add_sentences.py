import json
import re

# Exact sentences from the text and their translations
sentences_db = {
    "chef": {"en": "Harry doesn't want to be a star chef when he's 20.", "zh": "哈利不想等到20岁才成为一名明星厨师。"},
    "programme": {"en": "This is why he's on the TV programme Kitchen Kids.", "zh": "这就是为什么他参加了电视节目《厨房孩子》(Kitchen Kids)。"},
    "kitchen": {"en": "This is why he's on the TV programme Kitchen Kids.", "zh": "这就是为什么他参加了电视节目《厨房孩子》(Kitchen Kids)。"},
    "yorker": {"en": "The ten-year-old New Yorker likes cooking.", "zh": "这个十岁的纽约男孩喜欢烹饪。"},
    "cooking": {"en": "More and more young people are interested in cooking.", "zh": "越来越多的年轻人对烹饪感兴趣。"},
    "fantastic": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "soups": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "salads": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "excellent": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "omelettes": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "cakes": {"en": "He can make fantastic soups and salads, excellent omelettes and the best cakes.", "zh": "他能做出很棒的汤和沙拉、极好的煎蛋卷以及最棒的蛋糕。"},
    "interested": {"en": "More and more young people are interested in cooking.", "zh": "越来越多的年轻人对烹饪感兴趣。"},
    "special": {"en": "Others watch special cooking videos for children.", "zh": "其他人则观看专门为儿童制作的烹饪视频。"},
    "videos": {"en": "Others watch special cooking videos for children.", "zh": "其他人则观看专门为儿童制作的烹饪视频。"},
    "cities": {"en": "In many cities, there are special cooking classes for young people.", "zh": "在许多城市，都有专门针对年轻人的烹饪培训班。"},
    "classes": {"en": "In many cities, there are special cooking classes for young people.", "zh": "在许多城市，都有专门针对年轻人的烹饪培训班。"},
    "age": {"en": "Some of them are for children from the age of three!", "zh": "其中一些甚至针对三岁的儿童！"},
    "become": {"en": "But what must you do to become a star chef?", "zh": "但是要想成为一名明星厨师，你必须要怎么做呢？"},
    "important": {"en": "Of course, it's important that you like cooking and are really good at it.", "zh": "当然，喜欢烹饪并且真的很擅长烹饪也很重要。"},
    "rules": {"en": "But there are some rules.", "zh": "但这也有一些规则。"},
    "wash": {"en": "'We must wash our hands before we start cooking,' Harry says.", "zh": "“在开始做饭之前，我们必须洗手，”哈利说。"},
    "mouths": {"en": "'And of course we mustn't put them in our mouths.", "zh": "“当然我们绝不能把手放进嘴里。"},
    "careful": {"en": "And we must be very careful with hot plates.'", "zh": "而且我们必须非常小心热盘子。”"},
    "plates": {"en": "And we must be very careful with hot plates.'", "zh": "而且我们必须非常小心热盘子。”"},
    "excited": {"en": "Harry is excited.", "zh": "哈利很兴奋。"},
    "tomato": {"en": "This time he makes tomato soup, some salad, steak and carrot cake.", "zh": "这次他做了番茄汤、一些沙拉、牛排和胡萝卜蛋糕。"},
    "steak": {"en": "This time he makes tomato soup, some salad, steak and carrot cake.", "zh": "这次他做了番茄汤、一些沙拉、牛排和胡萝卜蛋糕。"},
    "carrot": {"en": "This time he makes tomato soup, some salad, steak and carrot cake.", "zh": "这次他做了番茄汤、一些沙拉、牛排和胡萝卜蛋糕。"},
    "experts": {"en": "The experts in the studio love Harry's food, and he stays on the show.", "zh": "演播室里的专家们很喜欢哈利的食物，他留在了节目中。"},
    "studio": {"en": "The experts in the studio love Harry's food, and he stays on the show.", "zh": "演播室里的专家们很喜欢哈利的食物，他留在了节目中。"},
    "tired": {"en": "Harry is happy, and a little tired.", "zh": "哈利很高兴，但也稍微有点累。"},
    "homework": {"en": "It's time to do his homework.", "zh": "现在是该做家庭作业的时间了。"}
}

# Read the JSON vocab data
vocab_path = r"d:\4kids\mason\prj\English-4A-Words\kitchen_kids_vocab.json"
with open(vocab_path, "r", encoding="utf-8") as f:
    vocab_list = json.load(f)

# Update the JSON entries with example sentences
for item in vocab_list:
    word = item["word"]
    if word in sentences_db:
        item["ex_en"] = sentences_db[word]["en"]
        item["ex_zh"] = sentences_db[word]["zh"]
    else:
        item["ex_en"] = ""
        item["ex_zh"] = ""

# Save updated JSON
with open(vocab_path, "w", encoding="utf-8") as f:
    json.dump(vocab_list, f, ensure_ascii=False, indent=2)

# Convert to JS array format for the HTML
js_array_lines = []
for i, item in enumerate(vocab_list):
    pack_num = (i // 10) + 1
    word = item["word"]
    phonetic = item["ipa"]
    pos = item["pos"]
    chinese = item["chinese"]
    ex_en = item.get("ex_en", "")
    ex_zh = item.get("ex_zh", "")
    
    # Escape quotes
    word_esc = word.replace('"', '\\"')
    ex_en_esc = ex_en.replace('"', '\\"').replace("'", "\\'")
    ex_zh_esc = ex_zh.replace('"', '\\"')
    
    line = f'            {{ unit: {pack_num}, word: "{word_esc}", phonetic: "{phonetic}", pos: "{pos}", chinese: "{chinese}", ex_en: "{ex_en_esc}", ex_zh: "{ex_zh_esc}", star: false }},'
    js_array_lines.append(line)

js_array_str = "\n".join(js_array_lines)

# Read the generated HTML
html_path = r"d:\4kids\mason\prj\English-4A-Words\kitchen_kids_flashcards.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the VOCAB array with the new one containing example sentences
# Note: we are replacing the existing VOCAB array in the kitchen_kids_flashcards.html
html_content = re.sub(
    r"const VOCAB = \[[\s\S]*?\];", 
    f"const VOCAB = [\n{js_array_str}\n        ];", 
    html_content
)

# Write the updated HTML
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully updated kitchen_kids_flashcards.html and JSON with text sentences.")
