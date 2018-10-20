const neo4j = require('neo4j-driver').v1;
const fs = require('fs');
const fetch = require("node-fetch");
const root = 'house'

const MAX_DEPTH = 1;
let currentDepth = 0;
const driver = neo4j.driver("bolt://localhost:7687", neo4j.auth.basic('neo4j', 'bluecakes'));
const session = driver.session();

// function main() {
//   session.run(`
//     MATCH (n)
//     WHERE n.text = "house"
//     RETURN n`
//   ).then(result => {
//     const singleRecord = result.records[0];
//     const node = singleRecord.get(0);
  
//     console.log(node.properties);
//     session.close();
//     driver.close();
//   })
// }


main()