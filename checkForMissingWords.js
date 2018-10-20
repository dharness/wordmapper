const fs = require('fs');
const axios = require("axios");

const txtBuff = fs.readFileSync('./words.csv');
let words = txtBuff.toString().split('\n');
words = words.map(w => w.toLowerCase().replace('-', ''))
words.shift(); // remove csv header
const wordSet = new Set(words);

const processResponse = (response, originalWord, percent) => {
  response.data.forEach(rhyme => {
    const formattedWord = rhyme.word.toLowerCase()
    if (formattedWord.indexOf(' ') >= 0) {return;}

    if (!wordSet.has(formattedWord)) {
      fs.writeFile('./missing.csv', `${formattedWord}\n`, {flag: 'a'}, (err) => {
        if (err) throw err;
        console.log(`${percent} %`);
      });
    }
  })
};

const main = () => {

  let i = 0;
  wordSet.forEach(word => {
    if(i++ > 1000) { return; }

    const url = `https://api.datamuse.com/words?rel_rhy=${word}`
    const percent = (i/wordSet.size) * 100;
    axios
      .get(url)
      .then((r) => processResponse(r, word, percent))
      .catch(e => console.log(e))
  })
}


main()