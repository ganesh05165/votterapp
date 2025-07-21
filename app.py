
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Voting App", layout="centered")

st.title("🗳 Votting ")
st.subheader("votting for class represnative")


if "votes" not in st.session_state:
    st.session_state.votes = {
        "Ram Kadav": 0,
        "Rajan Vicare": 0,
        "Jagan Pawar": 0,
        "Nota":0,
    }


if "voters" not in st.session_state:
    st.session_state.voters = set()


username = st.text_input("Enter your name to vote:")
candidate = st.selectbox("Choose a candidate", list(st.session_state.votes.keys()))

if st.button("Vote"):
    if not username:
        st.warning("⚠ Please enter your name before voting.")
    elif username in st.session_state.voters:
        st.error("❌ You have already voted!")
    else:
        st.session_state.votes[candidate] += 1
        st.session_state.voters.add(username)
        st.success(f"✅ {username}, your vote for {candidate} has been recorded!")

        df = pd.DataFrame([[username]], columns=["Name"])
        file_exists = os.path.exists("voters.csv")
        df.to_csv("voters.csv", mode='a', header=not file_exists, index=False)

st.markdown(" 📊 Current Vote Count")
for name, count in st.session_state.votes.items():
    st.write(f"{name}: {count} votes")