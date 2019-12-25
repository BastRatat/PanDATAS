"""
Author : Daniel, Bastien & Michael
Date : 15/12/2019
app main
"""

from flask import Flask, render_template, url_for

articles = {
    "title": "post",
    "author": "x",
    "date": "xx/xx/xxxx",
    "content": "x"
}

presentations = {
    "Daniel":   """
                    Highly-motivated & ambitious SWUFE MIB senior year
                    student with considerable 2 years track record &
                    experience in business development & marketing incl.
                    successful creation & execution of creative digital
                    media project for the Government of Queensland,
                    effective coordination & implementation of e-commerce
                    marketing strategy - paired with strong organizational
                    & functional skills. Recognized appointed TA of SWUFE
                    prof. Xu Yongan & laureate of Chinese Government
                    Scholarship for SWUFE MIB Programme & HNU Chinese
                    Language and Culture Programme, SWUFE International
                    Students Performance Scholarship. Enterprising,
                    knowledgeable & ingenious Visionary, bring change and
                    innovation via creative performance & solutions.
                """,
    "Bastien":  """ From France, Bastien landed in Chendgu in
                    2014 after his graduation from ISG Business School.
                    He spent his two first years in China studying mandarin and
                    preparing the Chartered Financial Analyst certification within the
                    double-top excellence programme of applied economics in SWUFE.
                    Fluent in chinese, english and french, Bastien and his brother
                    launched an education center in 2017. From January 2018 to
                    January 2020, he then was in charge of promoting France
                    education in the Consulate General of France in Chengdu.
                    Bastien's strong mathematical background combined with
                    analytical and econometrics skills brings valuable data-driven
                    insights.

                """,


    "Michael":  """ Curious, analytical and optimistic by nature with a strong background
                    in Computer Science: Bachelors in Computer Science from UCC, Ghana and in 2019,
                    M.Eng in Computer Science and Technology from UESTC, China.
                    He has an accumulated 2 years experience with minor Data Analytics tasks with
                    Google Analytics and Microsoft Excel. Recently, he has invested into training to
                    become a full-fledged Data Scientist first, through Le Wagon Chengdu and currently
                    studying Master of Data Science at ELU, Netherlands. He hopes to be ready for
                    the world of work by mid-2020.
                """
}

pages = ["Homepage", "About", "Data visualization",
         "Data sourcing", "Statistics"]

names = ["Daniel BISKUPSKI", "Bastien RATAT", "Michael O. MILLS"]

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", articles=articles, pages=pages)


@app.route('/about')
def about():
    return render_template("about.html", pages=pages, names=names, presentations=presentations)


@app.route('/data_visualization')
def data_visualization():
    return render_template("data_visualization.html", pages=pages)


@app.route('/data_sourcing')
def data_scraping():
    return render_template("data_sourcing.html", pages=pages)


@app.route('/statistics')
def statistics():
    return render_template("statistics.html", pages=pages)


if __name__ == '__main__':
    app.run(debug=True)
