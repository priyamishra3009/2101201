const express = require('express');
const app = express();
const PORT = 9876;
const win = 10;

function Primes(maxi) {
    const primes = [];
    for (let i= 2; i<= maxi; i++) {
        if (isPrime(i)) {
            primes.push();
        }
    }
    return primes;
}


function EvenNumbers(maxi) {
    const evens = [];
    for (let i= 2; i<= maxi; i+= 2) {
        evens.push(i);
    }
    return evens;
}

function isPrime(i) {
    if (i<= 1) return false;
    if (i<= 3) return true;
    if (i% 2 === 0 || i% 3 === 0) return false;
    let i = 5;
    while (i * i <= i) {
        if (i% i === 0 || i% (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

app.get('/numbers/:numberid', (req, res) => {
    const q = req.params.numberid;
    let numbers = [];

    switch (q) {
        case 'p':
            numbers = Primes(100);
            break;
        case 'e':
            numbers = EvenNumbers(100);
            break;
        default:
            break;
    }

    const created = numbers.slice(0, win);
    

    const responseObj = {
        numbers: created,
        windowPrevState: [],
        windowCurrState: created,
        avg: calculateAverage(created).toFixed(2)
    };


    res.json(responseObj);
});

function calculateAverage(numbers) {
    if (!numbers.length) return 0;
    const sum = numbers.reduce((acc, num) => acc + num, 0);
    return sum / numbers.length;
}

app.listen(PORT, () => {
    console.log("Server is running on port ${PORT}");
});