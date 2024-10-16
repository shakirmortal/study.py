import streamlit as st

# Example user profile and study plan generation logic with VAK learning styles
def personalize_study_plan(user_profile, subject):
    learning_style = user_profile.get('learning_style', 'visual')
    time_available = user_profile.get('time_available', 2)  # Default to 2 hours
    current_level = user_profile.get('current_level', 'beginner')

    # Simple logic to personalize a study plan based on learning style
    study_plan = f"### Study Plan for {subject}\n"
    study_plan += f"**Learning Style:** {learning_style.capitalize()}\n"
    study_plan += f"**Time Available:** {time_available} hours per day\n"
    study_plan += f"**Current Level:** {current_level.capitalize()}\n"
    study_plan += "\n#### Suggested Topics:\n- Basic concepts\n- Follow with examples and exercises."

    if learning_style == 'visual':
        study_plan += "\n\n**Visual Learner Recommendations:**\n- Watch instructional videos.\n- Use diagrams and flowcharts.\n- Create mind maps to connect ideas."
    elif learning_style == 'auditory':
        study_plan += "\n\n**Auditory Learner Recommendations:**\n- Listen to podcasts or lectures.\n- Discuss topics with peers.\n- Record yourself explaining concepts."
    elif learning_style == 'kinesthetic':
        study_plan += "\n\n**Kinesthetic Learner Recommendations:**\n- Use hands-on learning techniques.\n- Apply concepts in real-world projects.\n- Take frequent study breaks with physical activities."

    return study_plan

# Streamlit App Interface
st.title("🎓 Personalized Study Plan Generator")

# Get user input for subject
subject = st.text_input("Enter the subject:", "Mathematics")

# Create a user profile dictionary (replace with dynamic inputs if needed)
learning_style = st.selectbox("Select your learning style", ['visual', 'auditory', 'kinesthetic'])
study_hours = st.slider("How many hours can you study per day?", 1, 8, 2)

user_profile = {
    'learning_style': learning_style,
    'time_available': study_hours,
    'current_level': 'beginner'
}

# Generate the study plan
if st.button("Generate Study Plan"):
    study_plan = personalize_study_plan(user_profile, subject)
    st.markdown(study_plan)
