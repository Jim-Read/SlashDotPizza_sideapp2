CREATE TABLE "users" (
  "user_id" int PRIMARY KEY,
  "user_name" varchar,
  "email" varchar,
  "brag" varchar,
  "user_image" varchar,
  "location_id" int,
  "fav_pizza_id" int,
  "fav_friends_id" int
);

CREATE TABLE "pizza" (
  "pizza_id" int PRIMARY KEY,
  "pizza_name" varchar,
  "description" text,
  "price" numeric,
  "location" int,
  "pizza_image" varchar,
  "pizza_rating_id" int,
  "comment_id" int
);

CREATE TABLE "comments" (
  "comment_id" int PRIMARY KEY,
  "likes_id" int,
  "comment" varchar
);

CREATE TABLE "likes" (
  "likes_id" int PRIMARY KEY,
  "likes" boolean
);

CREATE TABLE "fav_pizza" (
  "fav_pizza_id" int PRIMARY KEY,
  "pizza_id" int
);

CREATE TABLE "fav_friends" (
  "fav_friends_id" int PRIMARY KEY,
  "user_id" int,
  "user_name" varchar
);

CREATE TABLE "locations" (
  "location_id" int PRIMARY KEY,
  "location" varchar
);

CREATE TABLE "pizza_rating" (
  "pizza_rating_id" int PRIMARY KEY,
  "user_rating" numeric
);

CREATE TABLE "user_login_password" (
  "user" int PRIMARY KEY,
  "user_id" int,
  "password" varchar
);


ALTER TABLE "users" ADD FOREIGN KEY ("location_id") REFERENCES "locations" ("location_id");

ALTER TABLE "users" ADD FOREIGN KEY ("fav_pizza_id") REFERENCES "fav_pizza" ("fav_pizza_id");

ALTER TABLE "users" ADD FOREIGN KEY ("fav_friends_id") REFERENCES "fav_friends" ("fav_friends_id");

ALTER TABLE "pizza" ADD FOREIGN KEY ("pizza_rating_id") REFERENCES "pizza_rating" ("pizza_rating_id");

ALTER TABLE "pizza" ADD FOREIGN KEY ("comment_id") REFERENCES "comments" ("comment_id");

ALTER TABLE "comments" ADD FOREIGN KEY ("likes_id") REFERENCES "likes" ("likes_id");

ALTER TABLE "user_login_password" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");
