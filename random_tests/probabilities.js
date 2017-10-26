'use strict';


function calculateProbabilities(rounds, dices) {

  function computeShots(n, shots) {
    if(n === 1) {
      return shots;
    }

    const shot = Array.from(Array(dices)).map(
      (_) => Math.floor(Math.random() * 6) + 1);

    const total = shot.reduce((a, b) => a + b);

    const newShots = shots.has(total) ?
    shots.set(total, [shot, ...shots.get(total)]) : shots.set(total, [shot]);

    return computeShots(n - 1, newShots);
  }

  const shots = computeShots(rounds, new Map());

  const probabilities = new Map();
  shots.forEach((value, key) => probabilities.set(key, value.length / rounds));

  return probabilities;
}

if(require.main === module) {
  const rounds = parseInt(process.argv[2]);
  const dices = parseInt(process.argv[3]);
  const probabilities = calculateProbabilities(rounds, dices);
  console.log(probabilities);
}
