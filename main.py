import streamlit as st

from components.bubble import bubble

# result = llm_chain.predict(human_input=player + ": " + input("> "))

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        "Hello, how are you?",
        "I'm good, how about you?",
        "I'm good too, thanks for asking!",
        "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available.",
    ]


for i, msg in enumerate(st.session_state.messages):
    if i % 2 == 0:
        bubble(
            msg,
            role="user",
            src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
        )
    else:
        bubble(
            msg,
            role="bot",
            src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
        )


with st.form(key="input", clear_on_submit=True):
    input_ = st.text_input("How do you want to play?", value="", key="player_input")
    st.form_submit_button(
        label="Make your mark on the universe.",
        on_click=lambda *args, **kwargs: st.session_state["messages"].append(
            st.session_state.player_input
        ),
    )
