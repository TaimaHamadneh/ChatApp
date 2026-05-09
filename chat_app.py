import streamlit as st
import random
import time


def generate_mock_response(user_message: str) -> str:
    msg_lower = user_message.lower().strip()

    # Simple rule‑based responses
    if any(greet in msg_lower for greet in ["hello", "hi", "hey", "greetings"]):
        return "Hi! How can I help you?"
    elif "how are you" in msg_lower:
        return "I'm just a piece of code, but I'm functioning perfectly! Thanks for asking."
    elif "bye" in msg_lower or "goodbye" in msg_lower:
        return "Bye! Have a nice day."
    elif "name" in msg_lower:
        return "I'm your local assistant – You can call me whatever you like!"
    elif "help" in msg_lower:
        return "You can ask me anything. I'll reply with simple rule‑based responses!"
    elif "weather" in msg_lower:
        return "I don't have access to live data, but I hope it's sunny where you are "
    else:
        replies = [
            f"You said: '{user_message[:40]}'",
            "Okay, tell me more.",
            "I understand.",
            "Thanks for your message.",
            "Interesting! Can you elaborate?",
        ]
        return random.choice(replies)


def main():
    st.set_page_config(page_title="Local Chat")
    st.title("💬 Local Chat Assistant")
    st.caption("Simple local chat app with basic responses.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Type your message here..."):

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking locally..."):
                time.sleep(0.5) 
                reply = generate_mock_response(prompt)
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()