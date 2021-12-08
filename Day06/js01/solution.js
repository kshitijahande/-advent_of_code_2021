const { data } = require('./input.js');

// Part 1
const partone = () => {
    const state = [...data];
    const days = Array(9).fill(0)
    for (let day of state) {
        days[day]++;
    }

    for (let i = 0; i < 80; i++) {
        let six_fish = 0;
	    let eight_fish = 0;
        for (let day = 0; day < days.length; day++) {
            let count = days[day];
            if (day === 0) {
                six_fish = count;
                eight_fish = count;
            } else {
                days[day - 1] = count;
            }
        }
        days[6] += six_fish;
        days[8] = eight_fish;
    }
    const total = days.reduce((a, b) => a + b);
    console.log("partone result", total)
};

// Part 2
const parttwo = () => {
    const state = [...data];
    const days = Array(9).fill(0)
    for (let day of state) {
        days[day]++;
    }

    for (let i = 0; i < 256; i++) {
        let six_fish = 0;
	    let eight_fish = 0;
        for (let day = 0; day < days.length; day++) {
            let count = days[day];
            if (day === 0) {
                six_fish = count;
                eight_fish = count;
            } else {
                days[day - 1] = count;
            }
        }
        days[6] += six_fish;
        days[8] = eight_fish;
    }
    const total = days.reduce((a, b) => a + b);
    console.log("parttwo result", total)
}

partone();
parttwo();