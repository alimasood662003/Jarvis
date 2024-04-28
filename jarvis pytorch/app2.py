import streamlit as st
from chat import get_response, bot_name  # Ensure these functions are defined

def main():
    st.title("Chat with Jarvis")
    st.sidebar.title("About")
    st.sidebar.info("This is a simple Streamlit chatbot application designed to showcase conversational AI.")

    if 'history' not in st.session_state:
        st.session_state.history = []

    def process_message():
        user_message = st.session_state.input
        if user_message:
            # User message
            st.session_state.history.append({"role": "user", "content": user_message})
            # Bot response
            bot_response = get_response(user_message)
            st.session_state.history.append({"role": "bot","content": f"{bot_response}"})
            # Clear input for next message
            st.session_state.input = ""

    user_input = st.text_input("Type your message:", key="input", on_change=process_message)

    # Create a chat window
    with st.container():
        for message in st.session_state.history:  # Display messages from oldest to newest
            if message["role"] == "user":
                st.container().markdown(f"**You**: {message['content']}", unsafe_allow_html=True)
            else:
                st.container().markdown(f"**{bot_name}**: {message['content']}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
