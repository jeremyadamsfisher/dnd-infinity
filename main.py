import streamlit as st

from chains.dm import DungeonMaster
from chains.quest_name import generate_quest_name
from components.bubble import bubble
from game.avatar import avatars
from game.turn_manager import TurnManager
from models.classifiers.quest import classifiy_is_quest_giving

ss = st.session_state

st.title("Dungeons and Dragons ♾️")

initial_prompt = """\
You are in a tavern. You see a gathering of shady characters clustered \
around a few tables, sipping ales and glancing nervously at the entrance \
with anticipation. You have been summoned to this tavern by a mysterious \
patron named Steve. Steve is sitting alone at a corner table near the \
hearth, wearing a voluminous cloak with a hood pulled up. He motions for \
you to join him. How do you proceed?"""

if "messages" not in ss:
    ss["messages"] = [("bot", initial_prompt)]

if "dm" not in ss:
    ss["dm"] = DungeonMaster(initial_prompt)

if "turn_manager" not in ss:
    ss["turn_manager"] = TurnManager(["Spud", "Kale"])

if "quests" not in ss:
    ss["quests"] = []

st.sidebar.markdown("**Quests**:\n" + "\n".join(f"- {quest}" for quest in ss.quests))

for entity, message in ss.messages:
    if entity == "bot":
        bubble.bot(message)
    else:
        bubble.user(message, src=avatars[entity])

if player_or_players := ss.turn_manager.who_can_take_a_turn():
    with st.form(key="input", clear_on_submit=True):
        player = st.selectbox("Player", player_or_players, key="player")
        input_ = st.text_area("Do anything.", value="", key="player_input")

        def submit():
            if ss.player_input:
                st.session_state["messages"].append((ss.player, ss.player_input))
                ss.turn_manager.take_turn(ss.player, ss.player_input)

        def skip_turn():
            ss.turn_manager.take_turn(ss.player)

        col1, col2, *_ = st.columns(6)
        with col1:
            st.form_submit_button(label="Take turn 🧙‍♂️", on_click=submit)
        with col2:
            st.form_submit_button(label="Skip turn 😪", on_click=skip_turn)

else:
    with st.spinner("Thinking about what happens next..."):
        ai_result = st.session_state.dm.next_conversational_turn(
            ss.turn_manager.format_turn_for_llm()
        )
        if classifiy_is_quest_giving(ai_result):
            quest = generate_quest_name(ai_result)
            ss.quests.append(quest)
        st.session_state["messages"].append(("bot", ai_result))
        ss.turn_manager.reset()
        st.experimental_rerun()


# if st.sidebar.checkbox("Admin"):
#     if st.sidebar.button("Export"):
#         import csv
#         import datetime

#         now = datetime.datetime.now()
#         with open(f"./logs-{now}.csv", "w") as f:
#             csv_writer = csv.DictWriter(f, fieldnames=["entity", "message"])
#             csv_writer.writeheader()
#             for entity, message in ss.messages:
#                 csv_writer.writerow({"entity": entity, "message": message})
