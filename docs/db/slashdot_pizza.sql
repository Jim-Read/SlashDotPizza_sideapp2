CREATE TABLE users(
  user_id SERIAL UNIQUE PRIMARY KEY, 
  user_name varchar(20),
  user_password varchar(20),
  email varchar(25),
  brag varchar(100),
  user_image varchar(300),
  location text);


CREATE TABLE fav_pizza (
  fav_pizza_id SERIAL UNIQUE PRIMARY KEY,
  user_id int, 
  pizza_id int,
  CONSTRAINT userfk FOREIGN KEY (user_id) REFERENCES users (user_id),
  CONSTRAINT pizzafk FOREIGN KEY (pizza_id) REFERENCES pizzas (pizza_id));


CREATE TABLE fav_friends (
  fav_friends_id SERIAL UNIQUE PRIMARY KEY,
  user_id int,
  users_friend int,
  CONSTRAINT userfk1 FOREIGN KEY (user_id) REFERENCES users (user_id),
  CONSTRAINT userfk2 FOREIGN KEY (user_id) REFERENCES users (user_id));


CREATE TABLE pizzas (
  pizza_id SERIAL UNIQUE PRIMARY KEY, 
  pizza_name varchar(100),
  description text,
  price real,
  location text,
  pizza_image varchar);


CREATE TABLE comments (
  comment_id SERIAL UNIQUE PRIMARY KEY, 
  pizza_id int,
  user_id int,
  comment varchar(255),
  CONSTRAINT pizzafk FOREIGN KEY (pizza_id) REFERENCES pizzas (pizza_id),
  CONSTRAINT userfk FOREIGN KEY (user_id) REFERENCES users (user_id));


CREATE TABLE likes (
  likes_id SERIAL UNIQUE PRIMARY KEY,
  comment_id int,
  user_id int,
  likes boolean,
  CONSTRAINT commentfk FOREIGN KEY (comment_id) REFERENCES comments (comment_id),
  CONSTRAINT userfk FOREIGN KEY (user_id) REFERENCES users (user_id));


CREATE TABLE pizza_rating (
  pizza_rating_id SERIAL UNIQUE PRIMARY KEY,
  user_id int,
  pizza_id int,
  user_rating float,
  CONSTRAINT pizzafk FOREIGN KEY (pizza_id) REFERENCES pizzas (pizza_id),
  CONSTRAINT userfk FOREIGN KEY (user_id) REFERENCES users (user_id));
