/* global use, db */

// Select the database to use.
use('yelp');

// business
// check if the index exists
indexName = "business_id_1"
if (db.business.getIndexes().some(index => index.name === indexName)) {
  db.business.dropIndex(indexName);
  print(`Dropped existing index: ${indexName}`); }
// create index
db.business.createIndex({ business_id: 1 }, { unique: true }); //-> enforce uniqueness
print("Created new index on business_id");

// user
indexName = "user_id_1"
if (db.user.getIndexes().some(index => index.name === indexName)) {
  db.user.dropIndex(indexName);
  print(`Dropped existing index: ${indexName}`); }
// create index
db.user.createIndex({ user_id: 1 }, { unique: true }); //-> enforce uniqueness
print("Created new index on user_id");

// review
indexName = "review_id_1"
if (db.review.getIndexes().some(index => index.name === indexName)) {
  db.review.dropIndex(indexName);
  print(`Dropped existing index: ${indexName}`); }
// create index
db.review.createIndex({ review_id: 1 }, { unique: true }); //-> enforce uniqueness
print("Created new index on review_id");

// checkin

// tip



  
