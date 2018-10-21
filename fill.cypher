USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///Users/dharness/dev/wordmapper/word.csv' as line

CREATE (word:Word { text: lower(line.text) })