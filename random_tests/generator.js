'use strict';

function* myGenerator(totalValues) {
  for(let i = 0; i < totalValues; i++) {
    yield i;
  }
}

if(require.main === module) {
  const totalValues = parseInt(process.argv[2]);

  for(let i of myGenerator(totalValues)) {
    console.log(i);
  }
}
