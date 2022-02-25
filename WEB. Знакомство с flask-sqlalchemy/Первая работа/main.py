from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Job
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    data_users = [
        ["Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org"],
        ["Butler", "Christopher", 19, "deputy captain", "research engineer", "module_2", "butler_deputy@mars.org"],
        ["Edwards", "Charles", 24, "head guard", "security", "module_3", "edwards_security@mars.org"],
        ["Sparks", "Joseph", 23, "chef", "cook", "module_4", "sparks_cook_great@mars.org"],
        ["Cannon", "Logan", 20, "lead", "software engineer", "module_5", "cannon_back_coder@mars.org"]
    ]

    data_jobs = [
        [1, "deployment of residential modules 1 and 2", 15, "2, 3", dt.datetime.now(), False]
    ]

    db_sess = db_session.create_session()

    for user in data_users:
        add_user(db_sess, *user)

    for job in data_jobs:
        add_job(db_sess, *job)

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


def add_job(db_sess, team_leader, need_job, work_size, collaborators, start_date, is_finished):
    job = Job()
    job.team_leader = team_leader
    job.job = need_job
    job.work_size = work_size
    job.collaborators = collaborators
    job.start_date = start_date
    job.is_finished = is_finished

    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
