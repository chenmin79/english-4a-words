import json
import re

# Read the JSON vocab data
with open(r"d:\4kids\mason\prj\English-4A-Words\kitchen_kids_vocab.json", "r", encoding="utf-8") as f:
    vocab_list = json.load(f)

# Convert to JS array format
js_array_lines = []
for i, item in enumerate(vocab_list):
    # Determine "Unit" based on index just to split them up into packs
    # Let's say 10 words per pack
    pack_num = (i // 10) + 1
    
    word = item["word"]
    phonetic = item["ipa"]
    pos = item["pos"]
    chinese = item["chinese"]
    # We don't have example sentences in the JSON, so we'll just put some placeholders or empty strings
    ex_en = word
    ex_zh = chinese
    
    # Escape quotes
    word_esc = word.replace('"', '\\"')
    ex_en_esc = ex_en.replace('"', '\\"')
    ex_zh_esc = ex_zh.replace('"', '\\"')
    
    line = f'            {{ unit: {pack_num}, word: "{word_esc}", phonetic: "{phonetic}", pos: "{pos}", chinese: "{chinese}", ex_en: "{ex_en_esc}", ex_zh: "{ex_zh_esc}", star: false }},'
    js_array_lines.append(line)

js_array_str = "\n".join(js_array_lines)


# Read the template HTML
with open(r"d:\4kids\mason\prj\English-4A-Words\index-4b.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the title
html_content = re.sub(
    r"<title>.*?</title>", 
    "<title>Kitchen Kids Vocabulary! 👨‍🍳</title>", 
    html_content, 
    flags=re.IGNORECASE
)

# Replace the header
html_content = re.sub(
    r"<h1>.*?</h1>", 
    "<h1>👨‍🍳 Kitchen Kids Vocab</h1>", 
    html_content, 
    flags=re.IGNORECASE
)
html_content = re.sub(
    r"<p>2024 New Edition Vocabulary</p>", 
    "<p>Frequency Rank > 300</p>", 
    html_content, 
    flags=re.IGNORECASE
)

# Replace the VOCAB array
html_content = re.sub(
    r"const VOCAB = \[[\s\S]*?\];", 
    f"const VOCAB = [\n{js_array_str}\n        ];", 
    html_content
)

# Change local storage key so it doesn't conflict with 4B
html_content = html_content.replace("'mason4b_state'", "'kitchen_kids_state'")

# Write the new HTML
with open(r"d:\4kids\mason\prj\English-4A-Words\kitchen_kids_flashcards.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully created kitchen_kids_flashcards.html")
