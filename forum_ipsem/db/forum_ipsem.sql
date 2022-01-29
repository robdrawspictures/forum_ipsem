DROP TABLE posts;
DROP TABLE users;
DROP TABLE threads;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(20),
    avatar_id INT,
    account_banned BOOLEAN,
    admin_status BOOLEAN
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    creator VARCHAR(20)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_content TEXT,
    user_id INT REFERENCES users(id),
    thread_id INT REFERENCES threads(id)
);

