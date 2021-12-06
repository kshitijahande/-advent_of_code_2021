const path = require('path');
const fs = require('fs');

const data = fs
	.readFileSync(path.join(__dirname, '../input.txt'), 'utf8')
	.toString()
	.trim()
	.split('\n')
	.map((num) => parseInt(num, 10));

module.exports = {
	data,
};