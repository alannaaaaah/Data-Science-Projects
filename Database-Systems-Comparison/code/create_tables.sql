
DROP TABLE IF EXISTS business CASCADE;
CREATE TABLE business (
	business_id VARCHAR(22) PRIMARY KEY,
	name TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	postal_code TEXT,
	latitude float,
	longitude float,
	stars float, 
	review_count int,
	is_open int,
	attributes TEXT, 
	categories TEXT,
	hours TEXT
);
COPY business (business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories,hours)
FROM '../data/yelp_academic_dataset_business.csv'                
DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS public.user CASCADE;
CREATE TABLE public.user (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    review_count INT,
    yelping_since VARCHAR(255),
    useful INT,
    funny INT,
    cool INT,
    elite VARCHAR(255),
    friends TEXT,
    fans INT,
    average_stars FLOAT,
    compliment_hot INT,
    compliment_more INT,
    compliment_profile INT,
    compliment_cute INT,
    compliment_list INT,
    compliment_note INT,
    compliment_plain INT,
    compliment_cool INT,
    compliment_funny INT,
    compliment_writer INT,
    compliment_photos INT
);
COPY public.user (yelping_since,compliment_list,compliment_plain,elite,compliment_cool,compliment_note,cool,review_count,compliment_photos,compliment_hot,name,user_id,compliment_more,compliment_cute,compliment_funny,average_stars,funny,useful,friends,compliment_profile,compliment_writer,fans)
FROM '../data/yelp_academic_dataset_user.csv'                
DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS checkin;
CREATE TABLE checkin (
    business_id VARCHAR(22) REFERENCES business(business_id) ON DELETE CASCADE ON UPDATE CASCADE,
    date TEXT
);
COPY checkin (business_id, date)
FROM '../data/yelp_academic_dataset_checkin.csv'                
DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS review;
CREATE TABLE review (
	review_id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES public.user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    business_id TEXT REFERENCES business(business_id) ON DELETE CASCADE ON UPDATE CASCADE,
    stars FLOAT,
    useful INT,
    funny INT,
    cool INT,
    text TEXT,
    date TEXT
);
COPY review (review_id, date, cool, text, useful, business_id, funny, user_id, stars)
FROM '../data/yelp_academic_dataset_review.csv'                
DELIMITER ',' CSV HEADER;
-- NOTE: one review has user_id (=tquAg8GqbhN5k6Hkd23M0A) not existing in the user table, just skip when importing


DROP TABLE IF EXISTS tip;
CREATE TABLE tip (
	business_id VARCHAR(22) REFERENCES business(business_id) ON DELETE CASCADE ON UPDATE CASCADE,
	user_id VARCHAR(22) REFERENCES public.user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	text TEXT,
	date TIMESTAMP,
	compliment_count INT
);
COPY tip (business_id, user_id, text, date, compliment_count)
FROM '../data/yelp_academic_dataset_tip.csv'                
DELIMITER ',' CSV HEADER;












