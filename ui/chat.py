import streamlit as st


def render_messages():
    for idx, msg in enumerate(st.session_state.messages):
        avatar = "👤" if msg["role"] == "user" else "🤖"
        with st.chat_message(
            msg["role"], avatar=avatar
        ):
            if msg["role"] == "assistant":
                st.markdown(
                    msg["content"],
                    unsafe_allow_html=True,
                    help="AI response"
                )
            else:
                st.markdown(
                    f"<span style='color:#3174ad;font-weight:bold'>{msg['content']}</span>",
                    unsafe_allow_html=True,
                    help="Your message"
                )


def add_user_message(prompt):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": st.session_state.get("user_message_time"),
    })


def add_ai_message(answer):
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "timestamp": st.session_state.get("ai_message_time"),
    })