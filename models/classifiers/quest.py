import streamlit as st
from setfit import SetFitModel


@st.cache_data
def get_model():
    weights_fp = "models/classifiers/setfil_weights"
    return SetFitModel.from_pretrained(weights_fp)


def classifiy_is_quest_giving(dialog_turn):
    """Classify whether the dialog turn is quest giving."""
    (prob,) = get_model().predict_proba([dialog_turn])
    _, p_quest = prob
    print(f"Dialog turn: {dialog_turn}")
    print(f"Prediction: p_{{quest}}={p_quest}")
    if 0.15 < p_quest:
        return True
    return False
