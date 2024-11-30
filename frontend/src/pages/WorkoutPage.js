import React, { useEffect, useState } from "react";
import axios from "axios";

function WorkoutPage() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/workouts").then((response) => {
      setWorkouts(response.data);
    });
  }, []);

  return (
    <div className="workout-page">
      <h1>Weekly Workouts</h1>
      {workouts.map((workout, index) => (
        <div key={index} className="workout">
          <h2>
            {workout.day} - {workout.type}
          </h2>
          <ul>
            {workout.exercises.map((exercise, idx) => (
              <li key={idx}>{exercise}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default WorkoutPage;
