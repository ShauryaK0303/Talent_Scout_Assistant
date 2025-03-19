import streamlit as st
from components.chat_interface import initialize_chat_state, display_chat_messages, handle_user_input
from config import APP_TITLE
from config import APP_DESCRIPTION

def main():
    # Set page configuration
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="👨‍💼",
        layout="wide"
    )
    
    st.header(APP_TITLE)
    st.markdown(APP_DESCRIPTION)
    
    st.divider()
    
    initialize_chat_state()
    

    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    main()