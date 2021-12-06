const { data } = require('./freader');

const partone = () => {
    let count = 0;
    for (let i = 0; i < data.length - 1; i++) {
    	if (data[i + 1] > data[i]) {
    		count++;
    	}
    }
    console.log(count);
}

partone()

const parttwo = () => {
    let count = 0;
    for (let i = 0; i < data.length - 3; i++) {
        let a = data[i];
        let b = data[i + 1];
        let c = data[i + 2];
        let d = data[i + 3];

        let current_window_sum = a + b + c;
        let next_window_sum = b + c + d;

        if (next_window_sum > current_window_sum) {
            count++;
        }
    }

    console.log(count);
}

parttwo()