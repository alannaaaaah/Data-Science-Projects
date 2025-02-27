/* global use, db */

// Select the database to use.
use('yelp');

//  Top common business categories
db.tip.find({}).limit(10);
