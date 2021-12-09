const { data } = require('./freader');

const fuelCostFromPosition = (from, to) => {
	const range = Math.abs(from - to);
	return (range * (range + 1)) / 2;
}

// Part 2
const parttwo = () => {
    let min_position = -1;
    let min_distance = Number.MAX_SAFE_INTEGER;
    for (let position_a of data) {
        let distance = 0;
        for (let position_b of data) {
            distance += fuelCostFromPosition(position_a, position_b);
        }
        
        if (distance < min_distance) {
            min_position = position_a;
            min_distance = distance;
        }
    }
    console.log("parttwo result", min_distance)
};

parttwo();