﻿from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    db_sess = db_session.create_session()
    add_user(db_sess, "Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")
    add_user(db_sess, "Butler", "Christopher", 19, "deputy captain", "research engineer", "module_2", "butler_deputy@mars.org")
    add_user(db_sess, "Edwards", "Charles", 24, "head guard", "security", "module_3", "edwards_security@mars.org")
    add_user(db_sess, "Sparks", "Joseph", 23, "chef", "cook", "module_4", "sparks_cook_great@mars.org")
    add_user(db_sess, "Cannon", "Logan", 20, "lead", "software engineer", "module_5", "cannon_back_coder@mars.org")

    # app.run()


def add_user(db_sess, surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
