const { data } = require('./freader.js');

// Brute force, can be optimised using Memozation
const fuelCostFromPosition = (position) => {
    let distance = 0;
    for (let other_position of data) {
        distance += Math.abs(position - other_position);
    }
    return distance;
};

// Part 1
const partone = () => {
    let min_position = -1;
    let min_distance = Number.MAX_SAFE_INTEGER;
    for (let position of data) {
        let distance = fuelCostFromPosition(position);
        if (distance < min_distance) {
            min_position = position;
            min_distance = distance;
        }
    }
    console.log("partone result", min_distance)
};

partone();