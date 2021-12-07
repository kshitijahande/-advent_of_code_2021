const { data } = require('./freader');

// Part-1 -- Brute Force solution
const partone = () => {
    let count = {}
    for (let row of data) {
        for (let i = 0; i < row.length; i++) {
            if (!count[i]) count[i] = [0, 0];
            count[i][row[i]]++;
        }
    }

    let gamma = [], epsilon = [];
    for (let counts of Object.values(count)) {
        if (counts[0] > counts[1]) {
            gamma.push(0);
            epsilon.push(1);
        } else {
            gamma.push(1);
            epsilon.push(0);
        }
    }

    let gamma_rate = parseInt(gamma.join(''), 2);
    let epsilon_rate = parseInt(epsilon.join(''), 2);

    console.log("partone ->", gamma_rate * epsilon_rate);
}


// Part-2 -- Brute Force solution
const parttwo = () => {
    let oxy = [...data]
    let co2 = [...data]
    
    let bit = 0;
    while (oxy.length > 1) {
        let { max } = getMinsMaxes(oxy);
        oxy = oxy.filter((num) => {
            return max[bit] === null ? num[bit] === '1' : num[bit] === max[bit];
        });
    
        bit++;
    }
    
    const oxy_rating = parseInt(oxy[0], 2);
    
    bit = 0;
    while (co2.length > 1) {
        let { min } = getMinsMaxes(co2);
        co2 = co2.filter((num) => {
            return min[bit] === null ? num[bit] === '0' : num[bit] === min[bit];
        });
        bit++;
    }
    
    const co2_rating = parseInt(co2[0], 2);
    
    console.log("parttwo ->", oxy_rating * co2_rating);
}

function getMinsMaxes(lines) {
    let count = {};

    for (let line of lines) {
        for (let i = 0; i < line.length; i++) {
            if (!count[i]) count[i] = [0, 0];
            count[i][line[i]]++;
        }
    }

    let mins = [];
    let maxs = [];
    for (let counts of Object.values(count)) {
        if (counts[0] === counts[1]) {
            maxs.push(null);
            mins.push(null);
        } else if (counts[0] > counts[1]) {
            maxs.push('0');
            mins.push('1');
        } else {
            maxs.push('1');
            mins.push('0');
        }
    }

    return {
        min: mins,
        max: maxs,
    };
}

partone();
parttwo();