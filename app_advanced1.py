import streamlit as st 
import os
import random
from main import (
    load_word_pools, 
    create_audio_file, 
    load_vocabulary_from_file, 
    save_word_pools_to_file,
    filter_words_by_category,
    validate_word_entry,
    cleanup_audio_file,
    DEFAULT_CATEGORIES,
    DEFAULT_VOCABULARY_FILE,
    DIFFICULTY_LEVELS,
    LEVEL_DESCRIPTIONS,
    SPEED_OPTIONS,
    SPEED_LABELS
)

# Phonetic transcriptions for vocabulary words
PHONETICS = {
    # General
    "serendipity": "/ˌsɛrənˈdɪpɪti/",
    "eloquent": "/ˈɛləkwənt/",
    "resilient": "/rɪˈzɪliənt/",
    "pragmatic": "/prægˈmætɪk/",
    "ubiquitous": "/juˈbɪkwɪtəs/",
    "meticulous": "/məˈtɪkjələs/",
    "ephemeral": "/ɪˈfɛmərəl/",
    "versatile": "/ˈvɜrsətaɪl/",
    "ambiguous": "/æmˈbɪgjuəs/",
    "innovative": "/ˈɪnəˌveɪtɪv/",
    "tenacious": "/təˈneɪʃəs/",
    "profound": "/prəˈfaʊnd/",
    "subtle": "/ˈsʌtəl/",
    "coherent": "/koʊˈhɪrənt/",
    "diligent": "/ˈdɪlɪdʒənt/",
    "intricate": "/ˈɪntrɪkət/",
    "benevolent": "/bəˈnɛvələnt/",
    "authentic": "/ɔˈθɛntɪk/",
    "efficient": "/ɪˈfɪʃənt/",
    "contemplative": "/kənˈtɛmplətɪv/",
    
    # Science
    "hypothesis": "/haɪˈpɑθəsɪs/",
    "catalyst": "/ˈkætəlɪst/",
    "molecule": "/ˈmɑləˌkjul/",
    "ecosystem": "/ˈikoʊˌsɪstəm/",
    "photosynthesis": "/ˌfoʊtoʊˈsɪnθəsɪs/",
    "chromosome": "/ˈkroʊməˌsoʊm/",
    "quantum": "/ˈkwɑntəm/",
    "biodiversity": "/ˌbaɪoʊdaɪˈvɜrsəti/",
    "metabolism": "/məˈtæbəˌlɪzəm/",
    "neuron": "/ˈnʊrɑn/",
    "osmosis": "/ɑzˈmoʊsɪs/",
    "mitosis": "/maɪˈtoʊsɪs/",
    "genome": "/ˈdʒinoʊm/",
    "thermodynamics": "/ˌθɜrmoʊdaɪˈnæmɪks/",
    "evolution": "/ˌɛvəˈluʃən/",
    "isotope": "/ˈaɪsəˌtoʊp/",
    "enzyme": "/ˈɛnzaɪm/",
    "gravity": "/ˈgrævəti/",
    "radiation": "/ˌreɪdiˈeɪʃən/",
    "symbiosis": "/ˌsɪmbaɪˈoʊsɪs/",
    
    # Business
    "entrepreneur": "/ˌɑntrəprəˈnɜr/",
    "revenue": "/ˈrɛvəˌnu/",
    "stakeholder": "/ˈsteɪkˌhoʊldər/",
    "portfolio": "/pɔrtˈfoʊlioʊ/",
    "synergy": "/ˈsɪnərdʒi/",
    "leverage": "/ˈlɛvərɪdʒ/",
    "equity": "/ˈɛkwəti/",
    "margin": "/ˈmɑrdʒən/",
    "franchise": "/ˈfrænˌtʃaɪz/",
    "diversification": "/daɪˌvɜrsəfəˈkeɪʃən/",
    "acquisition": "/ˌækwəˈzɪʃən/",
    "liability": "/ˌlaɪəˈbɪləti/",
    "liquidate": "/ˈlɪkwəˌdeɪt/",
    "compliance": "/kəmˈplaɪəns/",
    "benchmark": "/ˈbɛnʧˌmɑrk/",
    "scalable": "/ˈskeɪləbəl/",
    "subsidiary": "/səbˈsɪdiˌɛri/",
    "turnover": "/ˈtɜrnˌoʊvər/",
    "valuation": "/ˌvæljuˈeɪʃən/",
    
    # Add more categories as needed...
}

# Difficulty levels for words
DIFFICULTY_LEVELS = {
    # General - Easy to Hard
    "efficient": "⭐",
    "authentic": "⭐",
    "versatile": "⭐⭐",
    "pragmatic": "⭐⭐",
    "resilient": "⭐⭐",
    "innovative": "⭐⭐",
    "profound": "⭐⭐",
    "coherent": "⭐⭐",
    "diligent": "⭐⭐",
    "benevolent": "⭐⭐⭐",
    "eloquent": "⭐⭐⭐",
    "meticulous": "⭐⭐⭐",
    "ubiquitous": "⭐⭐⭐",
    "ephemeral": "⭐⭐⭐",
    "ambiguous": "⭐⭐⭐",
    "tenacious": "⭐⭐⭐",
    "subtle": "⭐⭐⭐",
    "intricate": "⭐⭐⭐",
    "contemplative": "⭐⭐⭐",
    "serendipity": "⭐⭐⭐",
    
    # Science
    "gravity": "⭐",
    "molecule": "⭐",
    "ecosystem": "⭐⭐",
    "evolution": "⭐⭐",
    "catalyst": "⭐⭐",
    "enzyme": "⭐⭐",
    "neuron": "⭐⭐",
    "genome": "⭐⭐⭐",
    "hypothesis": "⭐⭐⭐",
    "photosynthesis": "⭐⭐⭐",
    "chromosome": "⭐⭐⭐",
    "quantum": "⭐⭐⭐",
    "biodiversity": "⭐⭐⭐",
    "metabolism": "⭐⭐⭐",
    "osmosis": "⭐⭐⭐",
    "mitosis": "⭐⭐⭐",
    "thermodynamics": "⭐⭐⭐",
    "isotope": "⭐⭐⭐",
    "radiation": "⭐⭐⭐",
    "symbiosis": "⭐⭐⭐",
}

def get_phonetic(word):
    """Get phonetic transcription for a word"""
    return PHONETICS.get(word.lower(), "")

def get_difficulty(word):
    """Get difficulty level for a word"""
    return DIFFICULTY_LEVELS.get(word.lower(), "⭐⭐")

def generate_quiz_question(words, correct_word):
    """Generate a multiple choice quiz question"""
    options = [correct_word]
    other_words = [w for w in words if w['word'] != correct_word['word']]
    
    # Add 3 random wrong options
    wrong_options = random.sample(other_words, min(3, len(other_words)))
    for word in wrong_options:
        options.append(word)
    
    random.shuffle(options)
    return options

# Configure the app
st.set_page_config(
    page_title="Vocabulary Builder - Advanced 1",
    page_icon="📚",
    layout="wide"
)

# Custom CSS to increase base font size by 30%
st.markdown("""
<style>
    .main .block-container {
        font-size: 1.3em;
    }
    
    .stSelectbox > div > div {
        font-size: 1.3em;
    }
    
    .stRadio > div {
        font-size: 1.3em;
    }
    
    .stButton > button {
        font-size: 1.3em;
    }
    
    .stMarkdown {
        font-size: 1.3em;
    }
    
    .stSubheader {
        font-size: 1.69em;
    }
    
    .stHeader {
        font-size: 2.08em;
    }
    
    .stTitle {
        font-size: 2.6em;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Vocabulary Builder - Advanced 1")
st.header("Enhanced Learning with Phonetics & Quizzes")
st.subheader("Perfect for intermediate ESL learners")

# Level Selection
st.markdown("### 🎯 Select Your Learning Level")
level_col1, level_col2, level_col3 = st.columns(3)

with level_col1:
    if st.button("📚 **Level 1: Beginner**\n\nBasic vocabulary", key="adv1_level1"):
        st.session_state.selected_level = 1

with level_col2:
    if st.button("📖 **Level 2: Intermediate**\n\nChallenging words", key="adv1_level2"):
        st.session_state.selected_level = 2

with level_col3:
    if st.button("� **Level 3: Advanced**\n\nSophisticated vocabulary", key="adv1_level3"):
        st.session_state.selected_level = 3

# Initialize session state
if 'selected_level' not in st.session_state:
    st.session_state.selected_level = 2  # Default to intermediate for Advanced 1 app

# Display current level
current_level = st.session_state.selected_level
st.info(f"🎯 **Current Level: {current_level}** - {LEVEL_DESCRIPTIONS[current_level]}")

st.sidebar.title("�🎯 Advanced Navigation")

# Configuration
word_file = DEFAULT_VOCABULARY_FILE
category_list = DEFAULT_CATEGORIES

# Load sample vocabulary button
col1, col2 = st.columns(2)
with col1:
    if st.button(f"📚 Load Level {current_level} Vocabulary (160 words)", help=f"Load 20 words for each category at Level {current_level}"):
        word_pools = load_word_pools(current_level)
        if word_pools:
            success = save_word_pools_to_file(word_pools, word_file)
            if success:
                st.success(f"✅ Successfully loaded Level {current_level} vocabulary with 160 words across all categories!")
                st.info("Navigate to other sections to explore the features.")
            else:
                st.error("❌ Error loading sample vocabulary.")
        else:
            st.error(f"❌ Could not load Level {current_level} word pools from JSON file.")

with col2:
    # Statistics display
    all_words = load_vocabulary_from_file(word_file)
    if all_words:
        st.metric("📊 Total Words", len(all_words))

# Main navigation
select = st.sidebar.radio("Select Learning Mode", [
    "📖 Study Mode", 
    "🎯 Quiz Mode", 
    "➕ Add Word", 
    "📊 Progress"
])

if select == "📖 Study Mode":
    st.subheader("📖 Enhanced Study Mode")
    
    # Category and speed selection
    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox("Select a Category", category_list)
    with col2:
        selected_speed = st.selectbox(
            "🔊 Voice Speed:",
            options=SPEED_OPTIONS,
            format_func=lambda x: SPEED_LABELS[x]
        )
    
    # Filter selection
    difficulty_filter = st.radio(
        "Filter by Difficulty:",
        ["All Levels", "⭐ Easy", "⭐⭐ Medium", "⭐⭐⭐ Hard"],
        horizontal=True
    )
    
    if selected_category:
        all_words = load_vocabulary_from_file(word_file)
        filtered_words = filter_words_by_category(all_words, selected_category)
        
        # Apply difficulty filter
        if difficulty_filter != "All Levels":
            target_level = difficulty_filter
            filtered_words = [w for w in filtered_words if get_difficulty(w['word']) == target_level]
        
        if filtered_words:
            st.info(f"📚 Showing {len(filtered_words)} words from {selected_category}")
            
            for entry in filtered_words:
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        phonetic = get_phonetic(entry['word'])
                        difficulty = get_difficulty(entry['word'])
                        
                        st.markdown(
                            f"""
                            <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; margin: 10px 0; background-color: #f9f9f9;">
                                <h4 style="color: #4CAF50; margin-bottom: 5px; font-size: 1.8em;">📚 {entry['word']} {difficulty}</h4>
                                <p style="color: #666; font-style: italic; margin-bottom: 10px; font-size: 1.5em;">{phonetic}</p>
                                <p style="font-size: 1.69em;"><strong>Meaning:</strong> {entry['meaning']}</p>
                                <p style="font-size: 1.69em;"><strong>Example Phrase:</strong> {entry['phrase']}</p>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                    
                    with col2:
                        st.markdown("<br>", unsafe_allow_html=True)
                        
                        # Play buttons
                        if st.button(f"🔊 Word", key=f"word_{entry['word']}"):
                            audio_file = create_audio_file(entry['word'], f"word_{entry['word']}", is_phrase=False, speed=selected_speed)
                            if audio_file and os.path.exists(audio_file):
                                with open(audio_file, 'rb') as audio:
                                    st.audio(audio.read(), format='audio/wav')
                                cleanup_audio_file(audio_file)
                            else:
                                st.error("Audio generation failed")
                        
                        if entry['phrase'] and st.button(f"🔊 Phrase", key=f"phrase_{entry['word']}"):
                            audio_file = create_audio_file(entry['phrase'], f"phrase_{entry['word']}", is_phrase=True, speed=selected_speed)
                            if audio_file and os.path.exists(audio_file):
                                with open(audio_file, 'rb') as audio:
                                    st.audio(audio.read(), format='audio/wav')
                                cleanup_audio_file(audio_file)
                            else:
                                st.error("Audio generation failed")
        else:
            st.info("No words found for the selected category and difficulty level.")

elif select == "🎯 Quiz Mode":
    st.subheader("🎯 Interactive Quiz Mode")
    
    # Initialize session state for quiz
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_total' not in st.session_state:
        st.session_state.quiz_total = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = None
    
    # Quiz settings
    col1, col2 = st.columns(2)
    with col1:
        quiz_category = st.selectbox("Quiz Category", category_list)
    with col2:
        quiz_type = st.selectbox("Quiz Type", ["Meaning → Word", "Word → Meaning"])
    
    # Load words for quiz
    all_words = load_vocabulary_from_file(word_file)
    quiz_words = filter_words_by_category(all_words, quiz_category)
    
    if quiz_words and len(quiz_words) >= 4:
        # Score display
        if st.session_state.quiz_total > 0:
            accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
            st.metric("Quiz Accuracy", f"{accuracy:.1f}%", f"{st.session_state.quiz_score}/{st.session_state.quiz_total}")
        
        # Generate new question button
        if st.button("🎲 New Question") or st.session_state.current_question is None:
            correct_word = random.choice(quiz_words)
            options = generate_quiz_question(quiz_words, correct_word)
            st.session_state.current_question = {
                'correct': correct_word,
                'options': options,
                'answered': False
            }
        
        # Display current question
        if st.session_state.current_question:
            question = st.session_state.current_question
            correct_word = question['correct']
            
            if quiz_type == "Meaning → Word":
                st.markdown(f"### What word has this meaning?")
                st.info(f"**Meaning:** {correct_word['meaning']}")
                if correct_word['phrase']:
                    st.info(f"**Example:** {correct_word['phrase']}")
                
                # Multiple choice options
                option_labels = [opt['word'] for opt in question['options']]
            else:  # Word → Meaning
                phonetic = get_phonetic(correct_word['word'])
                st.markdown(f"### What is the meaning of: **{correct_word['word']}** {phonetic}")
                
                # Multiple choice options
                option_labels = [opt['meaning'] for opt in question['options']]
            
            # Radio button for answer selection
            if not question['answered']:
                selected_answer = st.radio("Choose your answer:", option_labels, key="quiz_answer")
                
                if st.button("✅ Submit Answer"):
                    # Check if answer is correct
                    if quiz_type == "Meaning → Word":
                        is_correct = selected_answer == correct_word['word']
                    else:
                        is_correct = selected_answer == correct_word['meaning']
                    
                    # Update score
                    st.session_state.quiz_total += 1
                    if is_correct:
                        st.session_state.quiz_score += 1
                        st.success("🎉 Correct! Well done!")
                    else:
                        st.error(f"❌ Incorrect. The correct answer was: **{correct_word['word'] if quiz_type == 'Meaning → Word' else correct_word['meaning']}**")
                    
                    # Mark as answered
                    st.session_state.current_question['answered'] = True
                    
                    # Show word details
                    phonetic = get_phonetic(correct_word['word'])
                    difficulty = get_difficulty(correct_word['word'])
                    st.markdown(f"**{correct_word['word']}** {phonetic} {difficulty}")
                    st.write(f"**Meaning:** {correct_word['meaning']}")
                    if correct_word['phrase']:
                        st.write(f"**Example:** {correct_word['phrase']}")
    else:
        st.warning("Need at least 4 words in the selected category to run quiz mode. Please load sample vocabulary first.")

elif select == "➕ Add Word":
    st.subheader("➕ Add New Word with Enhanced Features")
    
    col1, col2 = st.columns(2)
    with col1:
        word = st.text_input("Enter the word:")
        meaning = st.text_area("Enter the meaning:")
    with col2:
        phrase = st.text_input("Enter an example phrase:")
        category = st.selectbox("Select Category", category_list)
        phonetic_input = st.text_input("Phonetic transcription (optional):", placeholder="e.g., /ˈɛksəmpl/")
        difficulty_level = st.selectbox("Difficulty Level", ["⭐ Easy", "⭐⭐ Medium", "⭐⭐⭐ Hard"])
    
    if st.button("➕ Add Word"):
        is_valid, error_msg = validate_word_entry(word, meaning, phrase, category.lower())
        
        if is_valid:
            st.success(f"Word '{word}' added successfully!")
            # Note: In a full implementation, you'd also save the phonetic and difficulty data
            with open(word_file, "a", encoding='utf-8') as f:
                f.write(f"{word} | {meaning} | {phrase} | {category.lower()}\n")
        else:
            st.error(error_msg)

elif select == "📊 Progress":
    st.subheader("📊 Learning Progress & Statistics")
    
    all_words = load_vocabulary_from_file(word_file)
    
    if all_words:
        # Overall statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Words", len(all_words))
        with col2:
            if st.session_state.quiz_total > 0:
                accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
                st.metric("Quiz Accuracy", f"{accuracy:.1f}%")
            else:
                st.metric("Quiz Accuracy", "No quizzes yet")
        with col3:
            st.metric("Quizzes Taken", st.session_state.quiz_total)
        with col4:
            st.metric("Correct Answers", st.session_state.quiz_score)
        
        # Category breakdown
        st.markdown("### 📈 Words by Category")
        category_stats = {}
        for word in all_words:
            cat = word.get('category', 'Unknown').title()
            category_stats[cat] = category_stats.get(cat, 0) + 1
        
        # Display as columns
        cols = st.columns(len(category_stats))
        for i, (category, count) in enumerate(category_stats.items()):
            with cols[i]:
                st.metric(category, count)
        
        # Difficulty distribution (if available)
        st.markdown("### ⭐ Difficulty Distribution")
        difficulty_stats = {"⭐ Easy": 0, "⭐⭐ Medium": 0, "⭐⭐⭐ Hard": 0}
        for word in all_words:
            diff = get_difficulty(word['word'])
            if diff in difficulty_stats:
                difficulty_stats[diff] += 1
        
        diff_cols = st.columns(3)
        for i, (level, count) in enumerate(difficulty_stats.items()):
            with diff_cols[i]:
                st.metric(level, count)
        
        # Reset progress button
        if st.button("🔄 Reset Quiz Progress"):
            st.session_state.quiz_score = 0
            st.session_state.quiz_total = 0
            st.success("Quiz progress reset!")
    else:
        st.info("Load vocabulary words to see progress statistics.")

# Footer
st.markdown("---")
st.markdown("**Advanced 1 Features:** Phonetic transcription, difficulty levels, interactive quizzes, progress tracking")