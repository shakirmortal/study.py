        import streamlit as st
        import subprocess
        import sys
        @st.cache_resource
        def install_transformers():
            subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])
        install_transformers()
    # ...

 # Rest of your import statements below
 from transformers import GPTNeoForCausalLM, GPT2Tokenizer
 # ...

# Load the fine-tuned model and tokenizer
model_name = "./study"  # Update this path if necessary
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate study plan
def generate_study_plan(subject):
    prompt = f"Create a detailed study plan for a beginner in {subject}, including topics to cover, recommended resources, and study methods tailored for visual learners."
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate response with sampling enabled
    outputs = model.generate(
        **inputs,
        max_length=300,
        temperature=0.7,
        top_k=50,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit App Interface
st.title("🎓 Personalized Study Plan Generator")

# Get user input for subject
subject = st.text_input("Enter the subject:", "Physics")

# Generate the study plan when button is clicked
if st.button("Generate Study Plan"):
    study_plan = generate_study_plan(subject)
    st.markdown(study_plan)

