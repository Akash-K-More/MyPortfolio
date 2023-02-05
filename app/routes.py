from flask import Flask, render_template, send_file, redirect, request
import os
import db
import telegram


from app import app



b_id = ''
p_id = 'P1001'

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about",methods = ["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/download_cv", methods = ["POST","GET"])
def download_cv():
    path = os.getcwd()
    path += "/app/static/Akash-K-More-Resume.pdf"
    return send_file(path, as_attachment=True)

@app.route("/projects",methods = ["POST","GET"])
def projects():
    global p_id
    if request.method == "POST":
        project_id = request.form.get("project_id")
        p_id = project_id
    dict_project = {}

    fname = p_id+'.txt'
    with open(fname, 'r') as f1:
        title = f1.readline()
        lang = f1.readline()
        desc = f1.readline()
        img_path = f1.readline()
        file_path = f1.readline()
        dict_project['title'] = title
        dict_project['lang'] = lang
        dict_project['desc'] = desc
        dict_project['img_path'] = img_path
        dict_project['file_path'] = file_path

    comments = db.read_comments(p_id)
    return render_template("projects.html", dict_project=dict_project, comments=comments)

@app.route("/add_pcomment", methods = ["POST", "GET"])
def add_pcomment():
    uname = request.form.get("uname")
    comment = request.form.get("comment")
    db.add_comment(p_id, uname, comment)
    return redirect("/projects")

@app.route("/service",methods = ["POST","GET"])
def service():
    return render_template("service.html")

@app.route("/service/send_text",methods = ["POST","GET"])
def service_send_text():
    if request.method == "POST":
        employer_name = request.form.get("cname")
        employer_email = request.form.get("cemail")
        job_name = request.form.get("workname")
        job_location = request.form.get("clocation")
        job_desc = request.form.get("workdesc")
        msg = employer_name + employer_email + job_name + job_location + job_desc

        telegram.bot_sendtext(msg)

        # print(employer_name, employer_email, job_name, job_location, job_desc)
    
    return redirect("/service")

@app.route("/blog",methods = ["POST","GET"])
def blog():
    return render_template("blog.html")

@app.route("/blog_single",methods = ["POST","GET"])
def blog_single():
    global b_id
    if request.method == "POST":
        blog_id = request.form.get("blog_id")
        b_id = blog_id

    blog_param = {}
    fname = 'B' + b_id + '.txt'
    with open(fname, 'r') as f1:
        title = f1.readline()
        desc = f1.readline()
        img_path = f1.readline()
        blog_param['title'] = title
        blog_param['desc'] = desc
        blog_param['img_path'] = img_path
    comments = db.read_comments(b_id)
    return render_template("single-post.html", blog_param=blog_param, comments=comments)


@app.route("/add_comment", methods = ["POST", "GET"])
def add_comment():
    uname = request.form.get("uname")
    comment = request.form.get("comment")
    db.add_comment(b_id, uname, comment)
    return redirect("/blog_single")

@app.route("/contact",methods = ["POST","GET"])
def contact():
    return render_template("index.html")


