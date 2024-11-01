import json
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, usd, apologyStaff, login_requiredStaff, lookup

from flask import jsonify  # NEW
import datetime  # NEW
from flask import url_for


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///animal_rescue.db")

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")
    
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/", methods=["GET"])
@login_required
def index():
    """Show Index"""
    #return apology("Index")
    if request.method == "GET":

        # Redirect user to home page
        return render_template("index.html")



@app.route("/volunteerForm", methods=["GET", "POST"])
@login_required
def volunteerForm():
    """Show Volunteer Form(part 1)"""
    #return apology("volunteer Form")


    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        volunteerValues = list(result.values()) #Get only the values of the dict
        print(volunteerValues) # ['Mark', 'Smith', 'mark@smith.com']
        print (volunteerValues[0]) # Mark

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Volunteer) for that specific user
        db.execute("INSERT INTO volunteers (userid, firstname, lastname, phone, email, age, birth, address, city, postal, province, country, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, volunteerValues[0], volunteerValues[1], volunteerValues[2], volunteerValues[3], volunteerValues[4], volunteerValues[5], volunteerValues[6], volunteerValues[7], volunteerValues[8], volunteerValues[9], volunteerValues[10], date)



        if len(volunteerValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200


    else:

        # Redirect user to Volunteer Form(part 1)
        return render_template("volunteerForm.html")

@app.route("/volunteer")
#@login_required
def volunteer():
    """Show Volunteer.js"""
    #return apology("Volunteer.js")
    if request.method == "GET":

        # Redirect user to home page
        return render_template("volunteer.js")


@app.route("/fosterForm", methods=["GET", "POST"])
@login_required
def fosterForm():
    """Show Foster Form(part 1)"""
    #return apology("foster Form")

    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        fosterValues = list(result.values()) #Get only the values of the dict
        print(fosterValues) # ['Mark', 'Smith', 'mark@smith.com']
        print (fosterValues[0]) # Mark

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Foster) for that specific user
        db.execute("INSERT INTO fosterers (userid, firstname, lastname, phone, email, age, address, city, postal, province, country, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, fosterValues[0], fosterValues[1], fosterValues[2], fosterValues[3], fosterValues[4], fosterValues[5], fosterValues[6], fosterValues[7], fosterValues[8], fosterValues[9], date)


        if len(fosterValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200


    else: # GET

        # Redirect user to Foster Form(part 1)
        return render_template("fosterForm.html")

@app.route("/foster")
#@login_required
def foster():
    """Show foster.js"""
    #return apology("foster.js")
    if request.method == "GET":

        # Redirect user to foster.js
        return render_template("foster.js")

@app.route("/educateForm", methods=["GET", "POST"])
@login_required
def educateForm():
    """Show Educate Form(part 1)"""
    #return apology("educate Form")

    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        educateValues = list(result.values()) #Get only the values of the dict
        print(educateValues) # ['Mark', 'Smith', 'mark@smith.com']
        print(type(result))
        print (educateValues[0]) # Mark

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Educator) for that specific user
        db.execute("INSERT INTO educators (userid, firstname, lastname, email, date) VALUES (%s, %s, %s, %s, %s)",
                    userId, educateValues[0], educateValues[1], educateValues[2], date)


        if len(educateValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200


    else:  # GET
        # Redirect user to Educate Form(part 1)
        return render_template("educateForm.html")



@app.route("/educate")
def educate():
    """Show educate.js"""
    if request.method == "GET":

        # Redirect user to educate.js
        return render_template("educate.js")





@app.route("/adoptForm", methods=["GET", "POST"])
@login_required
def adoptForm():
    """Show Adopt Form(part 1)"""
    #return apology("Adopt Form")


    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        adoptValues = list(result.values()) #Get only the values of the dict
        print(adoptValues) # ['Mark', 'Smith', 'mark@smith.com']
        print (adoptValues[0]) # Mark

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Adopt) for that specific user
        db.execute("INSERT INTO adopters (userid, firstname, lastname, phone, email, age, address, city, postal, province, country, pettype, pname, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, adoptValues[0], adoptValues[1], adoptValues[2], adoptValues[3], adoptValues[4], adoptValues[5], adoptValues[6], adoptValues[7], adoptValues[8], adoptValues[9], adoptValues[10], adoptValues[11], date)



        if len(adoptValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200


    else:

        # Redirect user to Adopt Form(part 1)
        return render_template("adoptForm.html")

@app.route("/indexA")
#@login_required
def indexA():
    """Show index.js"""
    #return apology("index.js")
    if request.method == "GET":

        # Redirect user to index.js
        return render_template("index.js")






@app.route("/volunteerForm2", methods=["GET", "POST"])
@login_required
def volunteerForm2():
    """Show Volunteer Form(part 2)"""
    #return apology("volunteer Form 2")

    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        volunteerValues = list(result.values()) #Get only the values of the dict
        print(volunteerValues) # ['Mark', 'Smith', 'mark@smith.com']
        print (volunteerValues[0]) # Mark

        print ('------v1-------')
        print (volunteerValues[1])
        str1 = ', '.join(str(e) for e in volunteerValues[1])
        print (str1)

        #volunteerValues[3], volunteerValues[4], volunteerValues[5]
        print ('------v3-------')
        print (volunteerValues[3])
        str3 = ', '.join(str(e) for e in volunteerValues[3])
        print (str3)

        print ('------v4-------')
        print (volunteerValues[4])
        str4 = ', '.join(str(e) for e in volunteerValues[4])
        print (str4)

        print ('------v5-------')
        print (volunteerValues[5])
        str5 = ', '.join(str(e) for e in volunteerValues[5])
        print (str5)

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Volunteer 2) for that specific user
        db.execute("INSERT INTO volunteers2 (userid, whyvolunteer, enjoy, gaintext, daysweek, timesday, skills, exptext, currentocp, yearsocp, questions, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, volunteerValues[0], str1, volunteerValues[2], str3, str4, str5, volunteerValues[6], volunteerValues[7], volunteerValues[8], volunteerValues[9], date)


        if len(volunteerValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200

    else:

        # Redirect user to Volunteer Form(part 2)
        return render_template("volunteerForm2.html")

@app.route("/volunteer2")
#@login_required
def volunteer2():
    """Show volunteer2.js"""
    #return apology("volunteer2.js")
    if request.method == "GET":

        # Redirect user to volunteer2.js
        return render_template("volunteer2.js")


@app.route("/fosterForm2", methods=["GET", "POST"])
@login_required
def fosterForm2():
    """Show Foster Form(part 2)"""
    #return apology("foster Form 2")

    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        fosterValues = list(result.values()) #Get only the values of the dict
        print(fosterValues) # ['Mark', 'Smith', 'mark@smith.com']
        print(type(result))
        print (fosterValues[0]) # Mark

        print ('------f5-------')
        print (fosterValues[5])
        str5 = ', '.join(str(e) for e in fosterValues[5])
        print (str5)

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Foster 2) for that specific user
        db.execute("INSERT INTO fosterers2 (userid, petscurrently, minors, housetype, fencedyard, additionalexp, animaltype, questions, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, fosterValues[0], fosterValues[1], fosterValues[2], fosterValues[3], fosterValues[4], str5, fosterValues[6], date)


        if len(fosterValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200


    else: # GET

        # Redirect user to Foster Form(part 2)
        return render_template("fosterForm2.html")

@app.route("/foster2")
#@login_required
def foster2():
    """Show foster2.js"""
    #return apology("foster2.js")
    if request.method == "GET":

        # Redirect user to foster2.js
        return render_template("foster2.js")

@app.route("/educateForm2", methods=["GET"])
@login_required
def educateForm2():
    """Show Educate Form(part 2)"""
    #return apology("educate Form")
    if request.method == "GET":

        # Redirect user to educateForm2.html
        return render_template("educateForm2.html")

@app.route("/adoptForm2", methods=["GET", "POST"])
@login_required
def adoptForm2():
    """Show Adopt Form(part 2)"""
    #return apology("Adopt Form")


    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        adoptValues = list(result.values()) #Get only the values of the dict
        print(adoptValues) # ['Mark', 'Smith', 'mark@smith.com']
        print (adoptValues[0]) # Mark

        userId = session["user_id"]

        date = datetime.datetime.now()

        # Insert new request (Adopt) for that specific user
        db.execute("INSERT INTO adopters2 (userid, housetype, adults, minors, frequency, petsbefore, petscurrently, visit, whenadopt, questions, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    userId, adoptValues[0], adoptValues[1], adoptValues[2], adoptValues[3], adoptValues[4], adoptValues[5], adoptValues[6], adoptValues[7], adoptValues[8], date)



        if len(adoptValues) == 0:
            print('This dictionary is empty!')
            return jsonify({"result" : "failure", "error" : "401", "message" : "Empty Dictionary."}), 401
        else:
            print('This dictionary is not empty!')
            return jsonify({"result": "success"}), 200

    else:

        # Redirect user to Adopt Form(part 2)
        return render_template("adoptForm2.html")

@app.route("/indexA2")
#@login_required
def indexA2():
    """Show index2.js"""
    #return apology("index2.js")
    if request.method == "GET":

        # Redirect user to index2.js
        return render_template("index2.js")

@app.route("/resultsForm")
@login_required
def resultsForm():
    """Show Results Form"""
    #return apology("Results Form")
    if request.method == "GET":

        # Redirect user to Results Form
        return render_template("resultsForm.html")



@app.route("/adoptBirds")
@login_required
def adoptBirds():
    """Show Adopt Birds"""
    #return apology("Adopt Birds")
    if request.method == "GET":

        # Redirect user to Adopt Birds
        return render_template("adoptBirds.html")

@app.route("/adoptCanines")
@login_required
def adoptCanines():
    """Show Adopt Canines"""
    #return apology("Adopt Canines")
    if request.method == "GET":

        # Redirect user to Adopt Canines
        return render_template("adoptCanines.html")

@app.route("/adoptFelines")
@login_required
def adoptFelines():
    """Show Adopt Felines"""
    #return apology("Adopt Felines")
    if request.method == "GET":

        # Redirect user to Adopt Felines
        return render_template("adoptFelines.html")


@app.route("/adoptRodents")
@login_required
def adoptRodents():
    """Show Adopt Rodents"""
    #return apology("Adopt Rodents")
    if request.method == "GET":

        # Redirect user to Adopt Rodents
        return render_template("adoptRodents.html")


# Staff

@app.route("/staff/")
@login_requiredStaff
def staffIndex():
    """Show Index Staff"""
    #return apologyStaff("Index Staff")
    if request.method == "GET":
        userId = session["user_id"]

        # Get values from "users" and "transactions"
        staffName = db.execute("SELECT username FROM staff WHERE id = ?", userId)
        #educators (userId, firstName, lastName, email, date)
        #return jsonify(staffName)
        userName = staffName[0]["username"]  # Get the key pair of 'username'

        # Redirect user to Index Staff page
        return render_template("/staff/indexS.html", staffUsername=userName) #, from file = variableName


@app.route("/staff/newAdopter", methods=["GET", "POST"])
@login_requiredStaff
def staffnewAdopter():
    """Show New Adopter Staff"""
    #return apologyStaff("New Adopter Staff")
    if request.method == "GET":

        # Get values from "infoDB" table  (ORDER BY date DESC)
        infoDB = db.execute("SELECT users.username, adopters.userid, adopters.firstname, adopters.pname, adopters.date FROM adopters JOIN users ON users.id = adopters.userid")

        # Redirect user to home page
        return render_template("/staff/newAdopter.html", db=infoDB)

    else:
        #Getting 'userId' from form, and redirect to a new page, and send 'id' vale
        id = request.form.get("userid")
        print("From main page")
        print(id)

        return redirect(url_for('.staffInfoA', id=id))


@app.route("/staff/newEducator")
@login_requiredStaff
def staffnewEducator():
    """Show New Educator Staff"""
    #return apologyStaff("New Educator Staff")
    if request.method == "GET":

        # Get values from "infoDB" table  (ORDER BY date DESC)
        infoDB = db.execute("SELECT users.username, educators.firstname, educators.lastname, educators.email, educators.date FROM educators JOIN users ON users.id = educators.userid")
        return render_template("/staff/newEducator.html", db=infoDB)


@app.route("/staff/newFosterer", methods=["GET", "POST"])
@login_requiredStaff
def staffnewFosterer():
    """Show New Fosterer Staff"""
    #return apologyStaff("New Fosterer Staff")
    if request.method == "GET":

        # Get values from "infoDB" table  (ORDER BY date DESC)
        infoDB = db.execute("SELECT users.username, fosterers.userid, fosterers.firstname, fosterers.lastname, fosterers.date FROM fosterers JOIN users ON users.id = fosterers.userid")

        # Redirect user to home page
        return render_template("/staff/newFosterer.html", db=infoDB)

    else:
        #Getting 'userId' from form, and redirect to a new page, and send 'id' vale
        id = request.form.get("userid")
        print("From main page")
        print(id)

        return redirect(url_for('.staffInfoF', id=id))


@app.route("/staff/newVolunteer", methods=["GET", "POST"])
@login_requiredStaff
def staffnewVolunteer():
    """Show New Volunteer Staff"""
    #return apologyStaff("New Volunteer Staff")
    if request.method == "GET":

        # Get values from "infoDB" table  (ORDER BY date DESC)
        infoDB = db.execute("SELECT users.username, volunteers.userid, volunteers.firstname, volunteers.lastname, volunteers.date FROM volunteers JOIN users ON users.id = volunteers.userid")

        # Redirect user to home page
        return render_template("/staff/newVolunteer.html", db=infoDB)

    else:
        #Getting 'userId' from form, and redirect to a new page, and send 'id' vale
        id = request.form.get("userid")
        print("From main page")
        print(id)

        return redirect(url_for('.staffInfoV', id=id))




@app.route("/staff/infoF", methods=["GET", "POST"])
@login_requiredStaff
def staffInfoF():
    """Show More Info Staff (Foster)"""
    #return apologyStaff("More Info Staff (Foster)")

    id = request.args['id']
    print("From Second page")
    print(id)
    if request.method == "GET":

        # Get values from "users" and "transactions"
        clientName = db.execute("SELECT username FROM users WHERE id = ?", id)
        userName = clientName[0]["username"]  # Get the key pair of 'username'

        fosterersDB = db.execute("SELECT * FROM fosterers WHERE userid = ?", id)
        fosterers2DB = db.execute("SELECT * FROM fosterers2 WHERE userid = ?", id)

        # Redirect user to More Info (Foster) page
        return render_template("/staff/infoF.html", clientUsername=userName, db1=fosterersDB, db2=fosterers2DB)



@app.route("/staff/infoV", methods=["GET", "POST"])
@login_requiredStaff
def staffInfoV():
    """Show More Info Staff (Volunteer)"""
    #return apologyStaff("More Info Staff (Volunteer)")

    id = request.args['id']
    print("From Second page")
    print(id)
    if request.method == "GET":

        # Get values from "users" and "transactions"
        clientName = db.execute("SELECT username FROM users WHERE id = ?", id)
        userName = clientName[0]["username"]  # Get the key pair of 'username'

        volunteersDB = db.execute("SELECT * FROM volunteers WHERE userid = ?", id)
        volunteers2DB = db.execute("SELECT * FROM volunteers2 WHERE userid = ?", id)

        # Redirect user to More Info (Volunteer) page
        return render_template("/staff/infoV.html", clientUsername=userName, db1=volunteersDB, db2=volunteers2DB)


@app.route("/staff/infoA", methods=["GET", "POST"])
@login_requiredStaff
def staffInfoA():
    """Show More Info Staff (Adopter)"""
    #return apologyStaff("More Info Staff (Adopter)")

    id = request.args['id']
    print("From Second page")
    print(id)
    if request.method == "GET":

        # Get values from "users" and "transactions"
        clientName = db.execute("SELECT username FROM users WHERE id = ?", id)
        userName = clientName[0]["username"]  # Get the key pair of 'username'

        adoptersDB = db.execute("SELECT * FROM adopters WHERE userid = ?", id)
        adopters2DB = db.execute("SELECT * FROM adopters2 WHERE userid = ?", id)

        # Redirect user to More Info (Adopter) page
        return render_template("/staff/infoA.html", clientUsername=userName, db1=adoptersDB, db2=adopters2DB)



#Script indexA.js
@app.route("/staff/scriptStaff")
#@login_requiredStaff
def scriptStaff():
    """Show indexA.js"""
    #return apologyStaff("indexA.js")
    if request.method == "GET":

        # Redirect user to indexA.js
        return render_template("/staff/indexA.js")

@app.route("/staff/login", methods=["GET", "POST"])
def loginStaff():
    """Log user in (staff)"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apologyStaff("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apologyStaff("must provide password", 403)

        # Query database for username with error handling
        try:
            rowsS = db.execute("SELECT * FROM staff WHERE username = ?", request.form.get("username"))
        except Exception as e:
            db.session.rollback()  # Rollback the transaction on error
            print(f"Database error during staff login: {e}")
            return apologyStaff("Database error. Please try again.", 500)

        # Ensure username exists and password is correct
        if len(rowsS) != 1 or not check_password_hash(rowsS[0]["hash"], request.form.get("password")):
            return apologyStaff("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rowsS[0]["id"]

        # Redirect user to home page
        return redirect("/staff/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/staff/login.html")

@app.route("/staff/logout")
def logoutStaff():
    """Log user out (staff)"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/staff/")


@app.route("/staff/register", methods=["GET", "POST"])
def registerStaff():
    #
    """Register user (staff)"""
    if request.method == "POST":
        #username = request.form.get("username")
        #password = request.form.get("password")
        #confirmation = request.form.get("confirmation")

        if not request.form.get("username"):
            return apologyStaff("Must provide username", 400)

        if not request.form.get("password"):
            return apologyStaff("Must provide password", 400)

        if not request.form.get("confirmation"):
            return apologyStaff("Must provide confirmation", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apologyStaff("Passwords don't match", 400)
        
        date = datetime.datetime.now()

        # Insert new user
        try:
            newUser = db.execute("INSERT INTO staff (username, hash, date) VALUES (?, ?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")), date)
            
            # Remember the new user
            session["user_id"] = newUser
        except Exception as e:
            db.session.rollback()  # Rollback transaction on error
            print(f"Database error during staff registration: {e}")
            return apologyStaff("Username already exits", 400)

        return redirect("/staff/")

    else:  # GET
        return render_template("/staff/register.html")
    # return apologyStaff("TODO")












@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        try:
            rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        except Exception as e:
            db.session.rollback()  # Rollback the transaction if there's an error
            print(f"Database error during login: {e}")
            return apology("Database error. Please try again.", 500)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")





@app.route("/register", methods=["GET", "POST"])
def register():
    #
    """Register user"""
    if request.method == "POST":
        #username = request.form.get("username")
        #password = request.form.get("password")
        #confirmation = request.form.get("confirmation")

        if not request.form.get("username"):
            return apology("Must provide username", 400)

        if not request.form.get("password"):
            return apology("Must provide password", 400)

        if not request.form.get("confirmation"):
            return apology("Must provide confirmation", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match", 400)

        date = datetime.datetime.now()
        
        # Insert new user
        try:
            newUser = db.execute("INSERT INTO users (username, hash, date) VALUES (?, ?, ?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")), date)
            session["user_id"] = newUser  # Remember the new user
        except Exception as e:
            db.session.rollback()  # Rollback if there’s an error
            print(f"Database error during registration: {e}")
            return apology("Username already exits", 400)

        return redirect("/")

    else:  # GET
        return render_template("register.html")
    # return apology("TODO")



if __name__ == "__main__":
    app.run(debug=True)
