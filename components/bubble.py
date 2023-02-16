from pprint import pformat

import streamlit as st


class bubble:
    @staticmethod
    def user(
        message,
        src="https://jeremyafisher.com/images/prof.jpg",
    ):
        return bubble_(message, "user", src)

    @staticmethod
    def bot(message):
        return bubble_(
            message,
            "bot",
            src="https://jeremyafisher.com/images/dm.jpg",
        )


def bubble_(message, role, src):
    assert role in ["user", "bot"]
    avatar = f'<img class="avatar" src="{src}"/>'
    body = f"""
    <html>
        <head>
            <style>
                .bubble-container {{
                    display: flex;
                    justify-content: {"left" if role == "bot" else "right"};
                    align-items: flex-end;
                }}

                .bubble {{
                    border-radius: 10px;
                    padding: 10px;
                    color: white;
                    font-family: "Source Sans Pro", sans-serif;
                }}

                .bubble-user {{
                    background-color: rgb(37, 99, 235);
                    border-bottom-right-radius: 0px;
                }}

                .bubble-bot {{
                    background-color: grey;
                    border-bottom-left-radius: 0px;
                }}

                .avatar {{
                    width: 35px;
                    height: 35px;
                    border-radius: 50%;
                    margin-left: 5px;
                    margin-right: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="bubble-container">
                {avatar if role == "bot" else ""}
                <span class="bubble bubble-{role}">{message}</span>
                {avatar if role == "user" else ""}
            </div>
        </body>
    </html>
    """
    return st.components.v1.html(
        body,
        width=700,
        height=50 + (15 * pformat(message).count("\n")),
    )
