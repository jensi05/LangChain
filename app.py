import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("✈️ AI Travel Planner")

from_city = st.text_input("From City")
to_city = st.text_input("Destination City")
days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
travel_style = st.selectbox("Travel Style", ["Solo", "Family", "Couple", "Friends"])

if st.button("Generate Travel Plan"):
    with st.spinner("🔄 Planning your amazing trip... Please wait!"):
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.7
        )

        prompt = PromptTemplate(
            input_variables=["from_city", "to_city", "days", "budget", "travel_style"],
            template="""
You are a professional travel planner.

Create a {days}-day travel plan.

From: {from_city}
Destination: {to_city}
Budget: {budget}
Travel Style: {travel_style}

Include:
- Day wise plan
- Famous places
- Local food suggestions
- Travel tips
"""
        )

        chain = prompt | llm

        response = chain.invoke({
            "from_city": from_city,
            "to_city": to_city,
            "days": days,
            "budget": budget,
            "travel_style": travel_style
        })

    st.subheader("🧳 Your AI Travel Plan")
    st.write(response.content)
    st.balloons()
