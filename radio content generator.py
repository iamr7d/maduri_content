import os
import streamlit as st
from groq import Groq

# Set the environment variable for Groq API key
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Campus Radio Jockey Text Generator")

# Input fields for the user to provide context
show_name = st.text_input("Enter the type of content")
mood = st.selectbox("Select the mood for the commentary:", ["Funny", "Inspirational", "Casual", "Excited", "Professional"])
topic = st.text_input("Enter the content")

if st.button("Generate Script"):
    if topic and show_name and mood:
        # Create the prompt based on user inputs
        prompt = (f"Act as RJ Shruthi, the radio jockey at Digital University Kerala College FM. This is the type of {show_name}. "
                  f"Create a {mood.lower()} and engaging commentary about {topic}. "
                  f"Keep it brief, around 2-3 sentences, to entertain the students and make them smile!")

        # Send the prompt to the model for generation
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        
        # Extract and display the generated response
        response = chat_completion.choices[0].message.content
        st.write("Generated Radio Jockey Script:")
        st.write(response)
    else:
        st.write("Please fill out all the fields to generate a script.")
