import emoji
import re
import collections
from collections import Counter
emoji_moods = {
    '😄': 'happy',
    '😊': 'happy',
    '😂': 'happy',
    '🤗': 'happy',
    '🤩': 'happy',     # excited → happy
    '😎': 'happy', 
    '😅': 'happy',  # cool → happy
    '🤪': 'happy',     # silly → happy
    '😍': 'love',
    '🥰': 'love',
    '😘': 'love',
    '❤️': 'love',
    '🤝': 'love',      # friendly → love
    '👋': 'love',      # greeting → love
    '🙌': 'love',      # celebration → love
    '👏': 'love',      # applause → love
    '😢': 'sad',
    '😭': 'sad',
    '😔': 'sad',
    '💔': 'sad',
    '🤕': 'sad',       # hurt → sad
    '🤧': 'sad',       # sneezy → sad
    '😷': 'sad',       # sick → sad
    '🤒': 'sad',       # sick → sad
    '🤭': 'sad',       # shy/embarrassed → sad
    '🤫': 'sad',       # quiet → sad
    '😡': 'angry',
    '😠': 'angry',
    '🤥': 'angry',     # lying → angry
    '💀': 'sarcasm',
    '🤡': 'sarcasm',
    '💩': 'sarcasm',
    '🔥': 'hype',
    '🤯': 'surprised',
    '😱': 'surprised',
    '😐': 'neutral',
    '👍': 'positive',
    '👎': 'negative',
    '😇': 'positive',  # innocent → positive
    '🤓': 'positive',  # nerdy → positive
    '🤑': 'positive',  # greedy → positive
    '🤠': 'positive',  # cowboy → positive
    '🤖': 'neutral',   # robot → neutral
    '👻': 'neutral',   # ghost → neutral
    '👽': 'neutral',   # alien → neutral
    '😴': 'neutral',   # sleepy → neutral
    '🤔': 'neutral',   # thoughtful → neutral
}
def extract_emoji(text):
    return [char for char in text if char in emoji_moods]


def map_emojis_to_moods(emojis):
    moods = [emoji_moods.get(e, 'unknown') for e in emojis]
    return Counter(moods)

def generate_sentiment(mood_counter):
    if mood_counter['happy'] + mood_counter['love'] + mood_counter['positive'] > mood_counter['sad'] + mood_counter['angry'] + mood_counter['negative']:
        return "Positive 😊"
    elif mood_counter['sad'] + mood_counter['angry'] + mood_counter['negative'] > 0:
        return "Negative 😔"
    elif mood_counter['sarcasm'] + mood_counter['surprised'] > 0:
        return "Mixed 🤯"
    else:
        return "Neutral 😐"

def emoji_mood_classifier(text):
    emojis = extract_emoji(text)
    mood_counts = map_emojis_to_moods(emojis)
    sentiment = generate_sentiment(mood_counts)
    
    return {
        "input_text": text,
        "emojis": emojis,
        "mood_counts": mood_counts,
        "overall_sentiment": sentiment
    }

print("Welcome to the Emoji Mood Classifier!")
input_text = input("Please enter a text with emojis: ")
result = emoji_mood_classifier(input_text)

for k, v in result.items():
    print(f"{k}: {v}")

