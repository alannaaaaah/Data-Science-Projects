/* global use, db */

// Select the database to use.
use('yelp');

//  Top common business categories
db.business.createIndex({ categories: "text" });

db.business.aggregate([
    { $project: { categories: { $split: ["$categories", ", "] } } }, // Split categories into an array
    { $unwind: "$categories" }, // Unwind the array
    { $group: { _id: "$categories", count: { $sum: 1 } } }, // Count occurrences of each category
    { $sort: { count: -1 } } // Sort by count
  ]);