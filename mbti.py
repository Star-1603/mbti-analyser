import streamlit as st
from langchain.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

key = os.getenv("key")
if not key:
    st.error("Please set your HuggingFace API key in the environment variable `key`.")
    st.stop()

# Initialize the LLM
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(
    endpoint_url=f"https://api-inference.huggingface.co/models/{repo_id}",
    api_key=key,
    max_new_tokens=1200,
    temperature=0.9,
)

# Main function
def main():
    # Page configuration
    st.set_page_config(page_title="MBTI Analysis", layout="wide")
    st.title("MBTI Analysis Chatbot")
    st.write("Answer a few questions to determine your MBTI type!")

    # Input and interaction
    with st.form("mbti_form"):
        prompt = st.text_area("Describe yourself in a few words or sentences:")
        prompt_template = (
    "Analyze the following description and determine the MBTI type "
    "(Introvert vs. Extrovert, Intuition vs. Sensing, Thinking vs. Feeling, Judging vs. Perceiving):\n\n"
    f"{prompt}")
        submitted = st.form_submit_button("Analyze")
        generated_text = llm(prompt_template)
        

    if submitted:
        if not prompt.strip():
            st.warning("Please provide a description before submitting.")
        else:
            try:
                # Generate response using LLM
                with st.spinner("Analyzing your personality..."):
                    response = generated_text

                    st.subheader("Analysis Result:")
                    st.write(response)

            except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# Run the app
if __name__ == "__main__":
    main()
    #changes made