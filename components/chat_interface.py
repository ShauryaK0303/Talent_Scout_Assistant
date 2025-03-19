import streamlit as st
from utils.llm_utils import get_llm_response, is_conversation_end
from utils.data_utils import sanitize_input, extract_candidate_info, save_candidate_data
from utils.prompts_utils import SYSTEM_PROMPT
from config import END_KEYWORDS

def initialize_chat_state():
    """Initialize the chat state in the Streamlit session."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "Hello! I'm TalentScout's Hiring Assistant. I'm here to help with the initial screening for technical positions. Let's start with your full name, please."}
        ]
        
    
    if "conversation_ended" not in st.session_state:
        st.session_state.conversation_ended = False
    
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = None

def display_chat_messages():
    for message in st.session_state.messages:
        if message["role"] != "system": 
            with st.chat_message(message["role"]):
                st.write(message["content"])

def handle_user_input():
    if st.session_state.conversation_ended:
        st.info("The conversation has ended. Refresh the page to start a new conversation.")
        return
    
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        user_input = sanitize_input(user_input)
        
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.write(user_input)
        
        if is_conversation_end(user_input, END_KEYWORDS):
            end_conversation()
            return
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_llm_response(st.session_state.messages)
                st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        
        st.session_state.candidate_info = extract_candidate_info(st.session_state.messages)

def end_conversation():
    """End the conversation and save candidate data."""
    st.session_state.conversation_ended = True
    
    if st.session_state.candidate_info:
        filename = save_candidate_data(st.session_state.candidate_info)
        
        with st.chat_message("assistant"):
            st.write("Thank you for your time! The screening process is now complete. "
                     "Your information has been saved, and our recruitment team will review it. "
                     "We'll be in touch with you soon regarding the next steps.")
        
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Thank you for your time! The screening process is now complete. "
                       "Your information has been saved, and our recruitment team will review it. "
                       "We'll be in touch with you soon regarding the next steps."
        })