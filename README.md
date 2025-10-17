# 🎓 Vocabulary Builder Suite

A comprehensive English vocabulary learning system designed specifically for ESL (English as Second Language) learners. This suite offers three progressive applications with an integrated master interface and individual app options.

![Vocabulary Builder Suite](https://img.shields.io/badge/Vocabulary-Builder-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge)

## 🌟 Features Overview

### 🎯 Two Access Methods
- **🎓 Master App**: All-in-one integrated interface with app switching
- **🚀 Individual Apps**: Standalone applications for focused learning

### 📚 Three Learning Levels
- **📚 Basic**: Perfect for beginners with simple vocabulary management
- **🎯 Advanced 1**: Intermediate learners with quizzes and phonetic transcription  
- **🚀 Advanced 2**: Expert-level with AI-powered features and comprehensive analytics

### 🎨 Core Capabilities
- **3 Difficulty Levels** with 160 words each (480 total vocabulary words)
- **Level-Based Progression** from beginner to advanced vocabulary
- **American English Pronunciation** with multiple speed options (normal, 90%, 80%)
- **Interactive Learning** with quizzes, memory techniques, and progress tracking
- **Enhanced Readability** with 30% larger fonts for better visibility
- **Modular Architecture** for easy customization and extension

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Windows/macOS/Linux
- Virtual environment recommended

### Installation

1. **Clone or Download** this repository
```bash
git clone <repository-url>
cd vocabulary-builder
```

2. **Create Virtual Environment** (Recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### Launch Options

#### 🎓 **Option 1: Master App (Recommended)**
All three apps integrated in one interface:
```bash
streamlit run app.py
```

#### 🚀 **Option 2: App Launcher**
Visual selector with feature comparison:
```bash
streamlit run launcher.py
```

#### 📚 **Option 3: Individual Apps**
Run specific apps directly:
```bash
# Basic Vocabulary Builder
streamlit run app_basic.py

# Advanced Learning with Quizzes
streamlit run app_advanced1.py

# Expert Learning Suite
streamlit run app_advanced2.py
```

---

## 📱 Application Details

### � Master App (`app.py`) - **RECOMMENDED**
**All-in-one integrated vocabulary learning platform**

#### Master Features:
- 🎯 **Unified Interface**: Switch between all three apps seamlessly
- 📊 **Integrated Dashboard**: Quick stats and app descriptions
- 🔄 **Real-time Switching**: No need to restart applications
- 🎨 **Consistent Styling**: Unified design across all learning modes
- 📱 **Single Entry Point**: One command launches everything

#### How It Works:
1. Select your learning level from the sidebar (Basic/Advanced 1/Advanced 2)
2. Each app loads with full functionality
3. Switch between apps anytime without losing progress
4. All 480 vocabulary words available across 3 difficulty levels

### 🚀 Launcher App (`launcher.py`)
**Visual app selector with comprehensive feature comparison**

#### Launcher Features:
- **Visual App Cards**: Beautiful interface showcasing each app
- **Feature Comparison Table**: Side-by-side feature analysis
- **Learning Path Guidance**: Recommendations based on skill level
- **Quick Launch Commands**: Direct terminal commands for each app

### 📚 Basic App (`app_basic.py`)
**Perfect for beginners starting their vocabulary journey**

#### Features:
- ✅ **3-Level Vocabulary System**: 160 words per level (480 total)
- ✅ **Audio Pronunciation**: 3 speed options (Normal, 90%, 80%)
- ✅ **8 Categories**: General, Science, Business, Literature, Travel, History, Geography, Health
- ✅ **Enhanced Readability**: 30% larger fonts for better visibility
- ✅ **Level-Based Learning**: Progress from basic to advanced vocabulary
- ✅ **Simple Interface**: Clean, intuitive design

#### Sample Vocabulary by Level:
- **Level 1 (Beginner)**: Important, Beautiful, Animal, Work, Travel...
- **Level 2 (Intermediate)**: Magnificent, Hypothesis, Entrepreneur, Expedition...
- **Level 3 (Advanced)**: Ubiquitous, Mitochondria, Conglomerate, Peripatetic...

#### Best For:
- New English learners
- Users who prefer simple interfaces
- Progressive vocabulary building
- Basic pronunciation practice
- **Health**: cardiovascular, immunity, diagnosis, wellness...

### 🎯 Advanced 1 App (`app_advanced1.py`)
**Enhanced learning for intermediate students**

#### Advanced Features:
- ✅ **Phonetic Transcription (IPA)**: /ˌsɛrənˈdɪpɪti/
- ✅ **Word Difficulty Levels**: ⭐ Easy, ⭐⭐ Medium, ⭐⭐⭐ Hard
- ✅ **Interactive Quiz System**: Multiple choice with instant feedback
- ✅ **Progress Tracking**: Track your quiz performance
- ✅ **Study Mode Filters**: Filter by difficulty and category
- ✅ **Enhanced Statistics**: Detailed progress analytics

#### Quiz Features:
- **Meaning → Word**: Given a definition, choose the correct word
- **Word → Meaning**: Given a word, choose the correct definition
- **Adaptive Scoring**: Track accuracy and improvement over time
- **Instant Feedback**: Learn from mistakes immediately

#### Best For:
- ESL students ready for challenges
- Pronunciation-focused learning
- Users who enjoy interactive quizzes
- Learners wanting structured progress tracking

### 🚀 Advanced 2 App (`app_advanced2.py`)
**AI-powered comprehensive learning suite for serious learners**

#### Expert Features:
- 🧠 **Smart Study Mode**: AI-powered personalized learning
- 🏰 **Memory Palace**: Visual learning with location-based memory techniques
- 🎯 **Adaptive Quiz System**: Questions adapt based on your performance
- ✍️ **Writing Practice**: Create sentences and stories with feedback
- 🔍 **Word Explorer**: Deep linguistic analysis and word relationships
- 📊 **Analytics Dashboard**: Comprehensive learning analytics
- ⚙️ **Learning Settings**: Personalized study preferences

#### Advanced Learning Techniques:
- **Spaced Repetition**: Optimal review scheduling
- **Etymology**: Word origins and historical development
- **Synonyms & Antonyms**: Expand vocabulary connections
- **Collocations**: Learn natural word combinations
- **Word Forms**: Noun, verb, adjective variations
- **Usage Context**: Formal vs. informal registers

#### Memory Palace:
Create visual stories in different "rooms":
- 🚪 Entrance Hall
- 🛋️ Living Room
- 🍽️ Dining Room
- 🛏️ Bedroom
- 🌿 Garden

#### Best For:
- Advanced ESL students
- Language teachers and tutors
- Comprehensive vocabulary mastery
- Data-driven learning approach
- Professional English proficiency goals

---

## 📂 Project Structure

```
vocabulary-builder/
├── app.py                   # 🎓 Master app (all-in-one interface)
├── launcher.py              # 🚀 App selector and feature comparison
├── app_basic.py             # 📚 Basic vocabulary builder
├── app_advanced1.py         # 🎯 Advanced learning with quizzes
├── app_advanced2.py         # 🚀 Expert-level comprehensive suite
├── main.py                  # ⚙️ Shared utility functions
├── level1.json              # 📚 160 beginner vocabulary words
├── level2.json              # 📖 160 intermediate vocabulary words
├── level3.json              # 🎓 160 advanced vocabulary words
├── word_pools.json          # 📄 Legacy vocabulary database (for compatibility)
├── vocabulary.txt           # 📝 User's personal vocabulary file
├── requirements.txt         # 📦 Python dependencies
└── README.md               # 📖 This documentation
```

---

## 📖 Usage Guide

### 🎯 **Recommended Workflow**

#### For New Users:
1. **Start with Master App**: `streamlit run app.py`
2. **Select Basic level** from sidebar
3. **Load Level 1 vocabulary** (160 beginner words)
4. **Practice pronunciation** with audio features
5. **Progress to Level 2 and 3** as you improve

#### For Experienced Users:
1. **Launch Master App**: `streamlit run app.py`
2. **Switch to Advanced 1 or Advanced 2** from sidebar
3. **Take quizzes** and track progress
4. **Use advanced features** like memory palace and spaced repetition

### 📚 **Getting Started**
1. **New learners**: Start with Master App → Basic level → Level 1 vocabulary
2. **Intermediate students**: Master App → Advanced 1 → Level 2 vocabulary
3. **Advanced learners**: Master App → Advanced 2 → Level 3 vocabulary

### 🎯 **Three Ways to Access Apps**

#### 🎓 **Method 1: Master App (Recommended)**
```bash
streamlit run app.py
```
**Advantages:**
- All apps in one interface
- Easy switching between levels
- Unified experience
- No need to restart

#### 🚀 **Method 2: Individual Apps**
```bash
# For focused learning on specific app
streamlit run app_basic.py      # Basic learning
streamlit run app_advanced1.py  # Intermediate features  
streamlit run app_advanced2.py  # Advanced features
```
**Advantages:**
- Dedicated app experience
- Full feature access
- No interference between apps

#### 🎨 **Method 3: Visual Launcher**
```bash
streamlit run launcher.py
```
**Advantages:**
- Beautiful visual interface
- Feature comparison table
- Learning path guidance
- App recommendations

### 📈 **Learning Progression Path**

1. **Beginner** → Master App → Basic → Level 1 (160 words)
2. **Elementary** → Master App → Basic → Level 2 (160 words)  
3. **Intermediate** → Master App → Advanced 1 → Level 2/3 + Quizzes
4. **Advanced** → Master App → Advanced 2 → Level 3 + All Features
5. **Expert** → Advanced 2 → Memory Palace + Analytics

### Study Workflow
1. **Load Level Vocabulary**: Click "Load Level X Vocabulary" button for your chosen level
2. **Choose Category**: Select from 8 available categories
3. **Set Speed**: Choose pronunciation speed (Normal/90%/80%)
4. **Study Words**: Read, listen, and practice
5. **Take Quizzes**: Test your knowledge (Advanced apps)
6. **Track Progress**: Monitor your improvement

### Best Practices
- **Daily Practice**: 15-60 minutes depending on app level
- **Start Slow**: Begin with easier words and slower speeds
- **Use Examples**: Practice with the provided example phrases
- **Regular Review**: Revisit difficult words frequently
- **Progress Gradually**: Move to advanced apps when comfortable

---

## 🛠️ Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **pyttsx3**: Text-to-speech engine for pronunciation
- **Python Standard Library**: json, os, tempfile, datetime, random

### Audio Features
- **American English Voices**: Automatically detects and uses US English voices
- **Multiple Speeds**: Normal (100%), Slower (90%), Slowest (80%)
- **Temporary Files**: Audio files are automatically cleaned up

### Data Storage
- **JSON Format**: Word pools stored in structured JSON
- **Text Files**: User vocabulary in simple pipe-delimited format
- **Session State**: Progress and preferences stored during app session

---

## 🎯 Learning Path Recommendations

### 👶 Beginner Path (Basic App)
- **Time**: 15-30 minutes/day
- **Focus**: Basic vocabulary and pronunciation
- **Goal**: Build foundation with 50-100 words
- **Duration**: 2-4 weeks

### 📈 Intermediate Path (Advanced 1)
- **Time**: 30-45 minutes/day
- **Focus**: Pronunciation accuracy and quiz practice
- **Goal**: Master 200+ words with proper pronunciation
- **Duration**: 4-8 weeks

### 🎓 Advanced Path (Advanced 2)
- **Time**: 45-60 minutes/day
- **Focus**: Comprehensive mastery and usage
- **Goal**: Professional-level vocabulary (500+ words)
- **Duration**: Ongoing

---

## 📊 Vocabulary Categories

### 📚 General (20 words)
Everyday advanced vocabulary for general communication
- serendipity, eloquent, resilient, pragmatic, ubiquitous...

### 🔬 Science (20 words)
Scientific terms and concepts
- hypothesis, catalyst, ecosystem, photosynthesis, quantum...

### 💼 Business (20 words)
Professional and business terminology
- entrepreneur, revenue, stakeholder, synergy, leverage...

### 📖 Literature (20 words)
Literary terms and concepts
- metaphor, allegory, protagonist, symbolism, irony...

### ✈️ Travel (20 words)
Travel and adventure vocabulary
- itinerary, wanderlust, expedition, accommodation...

### 🏛️ History (20 words)
Historical terms and concepts
- civilization, dynasty, revolution, renaissance...

### 🌍 Geography (20 words)
Geographic and environmental terms
- latitude, topography, archipelago, ecosystem...

### 🏥 Health (20 words)
Health and medical vocabulary
- metabolism, cardiovascular, immunity, diagnosis...

---

## 🔧 Customization

### Adding New Words
```python
# In any app, use the "Add Word" feature or modify level files (level1.json, level2.json, level3.json)
{
  "word": "Your Word",
  "meaning": "Definition here",
  "phrase": "Example sentence here"
}
```

### Adding New Categories
1. Update `DEFAULT_CATEGORIES` in `main.py`
2. Add corresponding words to appropriate level files (`level1.json`, `level2.json`, `level3.json`)
3. Update the apps as needed

### Modifying Audio Settings
```python
# In main.py, adjust speech rates
base_word_rate = 160      # Words per minute for individual words
base_phrase_rate = 140    # Words per minute for phrases
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Add Vocabulary**: Contribute new words to existing categories
2. **New Categories**: Suggest and implement new word categories
3. **Features**: Enhance existing functionality
4. **Bug Fixes**: Report and fix issues
5. **Documentation**: Improve guides and examples
6. **Translations**: Help make the app multilingual

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🆘 Troubleshooting

### Common Issues

#### Audio Not Working
- **Windows**: Ensure Windows Speech API is available
- **macOS**: Check speech synthesis permissions
- **Linux**: Install espeak: `sudo apt-get install espeak`

#### App Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### File Not Found Errors
```bash
# Ensure you're in the correct directory
ls -la  # Should see app.py, main.py, etc.

# Check file permissions
chmod +r word_pools.json
```

### Getting Help
1. Check this README first
2. Look at error messages in the terminal
3. Ensure all files are in the same directory
4. Try running `python main.py` to test core functions

---

## 🎉 Success Stories

### What Users Say:
- **"Transformed my vocabulary learning!"** - ESL Student from Japan
- **"The progressive difficulty is perfect"** - Language Teacher, Mexico
- **"Memory Palace technique actually works!"** - Advanced Learner, Brazil
- **"Best pronunciation practice tool I've found"** - Student from South Korea

---

## 📈 Roadmap

### Upcoming Features:
- [ ] **Mobile App Version**: React Native implementation
- [ ] **More Languages**: Spanish, French, German support
- [ ] **Voice Recognition**: Speaking practice with feedback
- [ ] **Social Features**: Study groups and challenges
- [ ] **Offline Mode**: Work without internet connection
- [ ] **Advanced Analytics**: ML-powered learning insights

---

## 💡 Tips for Maximum Learning

### Study Strategies:
1. **Consistency**: Study daily, even if just 10 minutes
2. **Active Practice**: Don't just read - speak, write, quiz yourself
3. **Context Learning**: Always learn words with example sentences
4. **Review Cycle**: Review previous words before learning new ones
5. **Real Usage**: Try using new words in conversation

### Pronunciation Tips:
1. **Start Slow**: Use 80% speed initially
2. **Repeat**: Listen to each word multiple times
3. **Record Yourself**: Compare with the app's pronunciation
4. **IPA Learning**: Learn basic phonetic symbols (Advanced apps)
5. **Mouth Position**: Pay attention to how sounds are formed

---

**Ready to transform your English vocabulary? Start with `streamlit run launcher.py` and begin your learning journey today! 🚀**