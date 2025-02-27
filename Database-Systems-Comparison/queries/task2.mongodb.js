/* global use, db */

// Select the database to use.
use('yelp');

// Create index on business_id
db.review.createIndex({ business_id: 1 });
db.business.createIndex({ business_id: 1 });

//  Most reviewed business
db.review.aggregate([
    { $group: { _id: "$business_id", review_count: { $sum: 1 } } }, // Count reviews for each business
    { $sort: { review_count: -1 } }, // Sort by review count
    { $limit: 10 }, // Limit to top 10
    {
      $lookup: {
        from: "business", // Join with the business collection
        localField: "_id",
        foreignField: "business_id",
        as: "business_info"
      }
    },
    { $unwind: "$business_info" }, // Flatten the business_info array
    {
      $project: {
        business_name: "$business_info.name",
        city: "$business_info.city",
        state: "$business_info.state",
        stars: "$business_info.stars",
        review_count: 1
      }
    }
  ]);
  
  