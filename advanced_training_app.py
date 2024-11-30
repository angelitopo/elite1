import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Training Data
training_data = [
    {"day": "Day 1", "type": "Football + Upper Body Strength", "exercises": [
        "Warm-up jog and dynamic stretching (10 mins)",
        "Dribbling drills (15 mins)",
        "Passing exercises (15 mins)",
        "Shooting practice (20 mins)",
        "Bench Press: 4 sets x 8 reps",
        "Overhead Press: 3 sets x 10 reps",
        "Dumbbell Rows: 4 sets x 8 reps",
        "Core Circuit: Planks, Russian Twists, Leg Raises"
    ]},
    {"day": "Day 2", "type": "Football + Upper Body Strength", "exercises": [
        "Warm-up jog and dynamic stretching (10 mins)",
        "Tactical small-sided games (30 mins)",
        "Upper body gym: Bench press variations",
        "Incline Push-Ups",
        "Pull-Ups",
        "Core Circuit"
    ]},
    {"day": "Day 3", "type": "Lower Body Strength", "exercises": [
        "Squats: 5 sets x 5 reps",
        "Deadlifts: 4 sets x 6 reps",
        "Lunges: 3 sets x 12 reps per leg",
        "Hamstring Curls",
        "Calf Raises",
        "Glute Bridges"
    ]},
    {"day": "Day 4", "type": "Football-Only Training", "exercises": [
        "Tactical positioning drills",
        "Small-sided games",
        "Agility ladder exercises",
        "Passing and shooting practice"
    ]},
    {"day": "Day 5", "type": "Explosive Leg Work", "exercises": [
        "Plyometric Exercises: Box Jumps (4x10)",
        "Broad Jumps: 3 sets x 8 reps",
        "Sprint Intervals: 6 x 50 meters",
        "Medicine Ball Slams"
    ]},
    {"day": "Day 6", "type": "Upper Body Strength (Football-Specific) + Core", "exercises": [
        "Pull-Ups: 4 sets x Max reps",
        "Push-Ups Variations: 3 sets x 15 reps",
        "TRX Suspension Training",
        "Core Focus: Stability Ball Exercises, Side Planks, Mountain Climbers"
    ]},
    {"day": "Day 7", "type": "Rest Day", "exercises": [
        "Light yoga or stretching",
        "Hydration and nutrition focus"
    ]}
]

# Convert training data to a DataFrame
df_schedule = pd.DataFrame(training_data)

# Initialize performance log
if "performance_log" not in st.session_state:
    st.session_state.performance_log = []

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Today's Workout", "Performance Input", "Analytics"])

# Get today's workout dynamically based on day
today_index = (datetime.now().weekday() % 7)  # Rotate over the 7 days
today = df_schedule.iloc[today_index]

# Today's Workout
if menu == "Today's Workout":
    st.title("Today's Workout")
    st.subheader(f"Day: {today['day']} - {today['type']}")
    st.write("### Exercises")
    for exercise in today["exercises"]:
        st.write(f"- {exercise}")
    st.info("Stay consistent and record your performance in the next tab!")

# Performance Input
elif menu == "Performance Input":
    st.title("Performance Input")
    day = st.selectbox("Select Day", df_schedule["day"])
    exercises = df_schedule[df_schedule["day"] == day]["exercises"].values[0]
    st.write("### Record Your Performance")
    performance_log = []
    for i, exercise in enumerate(exercises):
        value = st.number_input(f"{exercise} (Reps/Time/etc.)", min_value=0, key=f"exercise_{i}")
        if value > 0:
            performance_log.append({"day": day, "exercise": exercise, "value": value})
    if st.button("Save"):
        st.session_state.performance_log.extend(performance_log)
        st.success("Performance logged!")

# Analytics
elif menu == "Analytics":
    st.title("Performance Analytics")
    st.write("### Visualize Your Progress")
    if st.session_state.performance_log:
        df_log = pd.DataFrame(st.session_state.performance_log)
        # Aggregate data for visualization
        fig = px.line(df_log, x="exercise", y="value", color="day", title="Performance Trends")
        st.plotly_chart(fig)
        st.write("### Raw Data")
        st.dataframe(df_log)
    else:
        st.warning("No performance data available. Record some in the 'Performance Input' tab!")

# Footer
st.sidebar.success("Navigate through the app!")
