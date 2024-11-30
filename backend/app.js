const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const workoutRoutes = require("./routes/workoutRoutes");

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Routes
app.use("/api/workouts", workoutRoutes);

// Default route
app.get("/", (req, res) => {
  res.send("Welcome to Elite Football Trainer API");
});

module.exports = app;
