USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///Users/dharness/dev/wordmapper/words_lower.csv' as line

MERGE (word:Word { text: line.text })