const express = require("express");
const fs = require("fs");
const path = require("path");

const router = express.Router();

// Path to the JSON file
const WORKOUTS_FILE = path.join(__dirname, "../data/workouts.json");

// Get all workouts
router.get("/", (req, res) => {
  fs.readFile(WORKOUTS_FILE, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading workouts file:", err);
      return res.status(500).json({ message: "Failed to load workouts" });
    }

    const workouts = JSON.parse(data);
    res.json(workouts);
  });
});

// Add a new workout (optional, if needed)
router.post("/", (req, res) => {
  fs.readFile(WORKOUTS_FILE, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading workouts file:", err);
      return res.status(500).json({ message: "Failed to load workouts" });
    }

    const workouts = JSON.parse(data);
    const newWorkout = req.body;

    workouts.push(newWorkout);

    fs.writeFile(WORKOUTS_FILE, JSON.stringify(workouts, null, 2), (writeErr) => {
      if (writeErr) {
        console.error("Error writing to workouts file:", writeErr);
        return res.status(500).json({ message: "Failed to save workout" });
      }

      res.status(201).json(newWorkout);
    });
  });
});

module.exports = router;
