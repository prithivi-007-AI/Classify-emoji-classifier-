😄 Emoji Mood Classifier 🎭
A Python NLP tool that classifies mood and sentiment based on emojis in text — designed for social media analytics, meme detection, and Gen Z-style emotion engines.

💡 What It Does
🔍 Extracts emojis from any given text
🎯 Maps emojis to simplified mood categories like happy, sad, love, angry, surprised, etc.
🧠 Generates an overall sentiment label (Positive, Negative, Mixed, or Neutral)
🔤 Unicode-safe & supports multilingual text
🧹 Cleans and normalizes input for consistent analysis

🛠 Tech Stack
Python 3.x
emoji package for Unicode emoji handling
re for pattern matching
collections.Counter for mood stats
No ML required — fully rule-based and lightweight ⚡

🚀 Example

Input:
I love this movie 😍🔥🔥 but that ending made me cry 😭💔

Output:

{
  "emojis": ["😍", "🔥", "🔥", "😭", "💔"],
  "mood_counts": {
    "love": 1,
    "hype": 2,
    "sad": 2
  },
  "overall_sentiment": "Mixed 🤯"
}

🎯 Use Cases

Social media caption analysis
Meme mood detection
Chatbot emotion understanding
Sentiment tagging in comment sections
Gen Z-style emoji-based search engines 😆

🧪 How to Run
# Clone the repo
git clone https://github.com/yourusername/emoji-mood-classifier.git

# Install dependencies
pip install emoji

# Run the script
python mood_classifier.py


📦 Coming Soon (Ideas)
 Web version with Gradio or Flask UI
 Batch analysis for CSV/TXT data
 Support for emoji sentiment scores
 Emoji visualization charts 📊
 Integration with social media APIs (Twitter, Instagram captions)
