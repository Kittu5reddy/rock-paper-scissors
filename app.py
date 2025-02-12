import random
from PIL import Image
import streamlit as st

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        st.session_state["user_score"] += 1
        return "You Win!"
    else:
        st.session_state["computer_score"] += 1
        return "Computer Wins!"

# Initialize session state for scores
if "user_score" not in st.session_state:
    st.session_state["user_score"] = 0
if "computer_score" not in st.session_state:
    st.session_state["computer_score"] = 0

st.title("Rock Paper Scissors")

# Load and resize images
img_rock = Image.open("rock.jpeg").resize((200, 150))  
img_paper = Image.open("p.jpg").resize((200, 150))
img_scissor = Image.open("sc.webp").resize((200, 150))

img1, img2, img3 = st.columns(3)
with img1:
    st.image(img_rock)
with img2:
    st.image(img_paper)
with img3:
    st.image(img_scissor)

# Game choices
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

col1, col2, col3 = st.columns(3)
with col1:
    pressed=st.button("Rock")
    if pressed:
        result = get_winner("Rock", computer_choice)
        st.session_state["last_result"] = result
        st.session_state["computer_last_choice"] = computer_choice

with col2:
    pressed=st.button("paper")
    if pressed:
        result = get_winner("Paper", computer_choice)
        st.session_state["last_result"] = result
        st.session_state["computer_last_choice"] = computer_choice

with col3:
    pressed=st.button("Scissors")
    if pressed:
        result = get_winner("Scissors", computer_choice)
        st.session_state["last_result"] = result
        st.session_state["computer_last_choice"] = computer_choice

# Display Scores
st.subheader("Scores:")
res1,res2=st.columns(2)
with res1:
    st.title(f"**You:** {st.session_state['user_score']}")
with res2:
    st.title(f"**Computer:** {st.session_state['computer_score']}")

# Reset button
if st.button("Reset Scores 🔄"):
    st.session_state["user_score"] = 0
    st.session_state["computer_score"] = 0
    st.session_state["last_result"] = "Scores have been reset!"
    st.session_state["computer_last_choice"] = None

# Show last round result
if "last_result" in st.session_state:
    st.subheader("Last Round Result:")
    if st.session_state["computer_last_choice"]:
        st.write(f"Computer chose: **{st.session_state['computer_last_choice']}**")
    st.write(f"**{st.session_state['last_result']}**")