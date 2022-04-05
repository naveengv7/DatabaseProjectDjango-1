from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def administrator(request):

    form = '<!DOCTYPE html>' + \
           '<html>' + \
           '<body>' + \
           '<h1>Administrator:</h1>' + \
           '<h3> Choose the following Functions to perform: </h3>' + \
           '<form action="f1/" method="post">' + \
           '<p> F1. Create a list of professors sorted by: <p>' + \
           '<INPUT TYPE=radio NAME="sort_method" VALUE="name" > Name</LABEL><BR>' + \
           '<INPUT TYPE=radio NAME="sort_method" VALUE="dept_name"> Department</LABEL><BR>' + \
           '<INPUT TYPE=radio NAME="sort_method" VALUE="salary"> Salary</LABEL>' + \
           '<p>        </p>' + \
           '<input type="submit" value = "List of professors sorted">' + \
           '</form>' + \
           '<form action="f2/" method="post">' + \
           '<p> F2. Create a table of min/max/average salaries by department: <p>' + \
           '<input type-"text" id="dept_name" name="dept_name"><br><br>' + \
           '<input type="submit" value = "View salaries of instructors">' + \
           '</form>' + \
           '<form action="f3/" method="post">' + \
           '<p> F3. Create a table of professor name, dept, and total number of students taught by the professor in a given semester <p>' + \
           '<input type-"text" id="semester_ip" name="semester_ip"><br><br>' + \
           '<input type="submit" value = "View professors">' + \
           '</form>' + \
           '</body>' + \
           '</html>'

    return HttpResponse(form)

@csrf_exempt
def f1(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1",
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    sort = request.POST['sort_method']
    query = "select * from instructor"
    query += " order by " + sort
    query += ";"
    mycursor.execute(query)

    data = '<h1>Sorted results :</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>ID</th> <th>Name</th> <th>dept_name</th> <th>Salary</th> </tr>'
    for (ID, name, dept_name, salary) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(ID) + '</th>' + \
             '<th>' + str(name) + '</th>' + \
             '<th>' + str(dept_name) + '</th>' + \
             '<th>' + str(salary) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@csrf_exempt
def f2(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1",
        auth_plugin="mysql_native_password",
        database="university",
    )
    mycursor = mydb.cursor()
    dept = request.POST['dept_name']
    query = "select MAX(salary), MIN(salary), AVG(salary)" + \
            " from instructor " + \
            "where instructor.dept_name = \"" + dept + "\";"
    mycursor.execute(query)

    data = '<h1>Results:</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>Max</th> <th>Min</th> <th>Average</th></tr>'
    for (max, min, avg) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(max) + '</th>' + \
             '<th>' + str(min) + '</th>' + \
             '<th>' + str(avg) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@csrf_exempt
def f3(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1",
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    semester = request.POST['semester_ip']
    query = "select I.name, I.dept_name, COUNT(S.name) "
    query += "from instructor I, student S, teaches TC, takes TK "
    query += "where I.ID = TC.id AND TC.course_id = TK.course_id AND TK.id = S.ID "
    if semester != "":
        query += "and TK.semester = " + semester
        query += ";"
    mycursor.execute(query)

    data = '<h1>Results:</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>Name</th> <th>Dept</th> <th>Number of Students</th> </tr>'
    for (name, dept, count) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(name) + '</th>' + \
             '<th>' + str(dept) + '</th>' + \
             '<th>' + str(count) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

