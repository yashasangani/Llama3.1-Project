import streamlit as st
from groq import Groq

# Get the groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# define a function to get model response
def get_response(query):
    stream = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content": query
            }
        ],
        model = "llama-3.1-70b-versatile",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=True
    )
    # Showing the model response
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

# Streamlit application
if __name__ == "__main__":
    st.set_page_config(
        page_title="Llama3.1 Yasha", 
        page_icon="💬"
    )
    st.title("Llama3.1 with Groq 😎 - Yasha Sangani")
    st.subheader("Model used - llama-3.1-70b-versatile")
    st.subheader("Please ask a question below and press ctrl + Enter to get response")
    query = st.text_area("Please enter your query : ")
    if query:
        st.subheader("Model Response :")
        st.write_stream(get_response(query))