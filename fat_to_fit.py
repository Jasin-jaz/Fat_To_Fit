import datetime
from flask import Flask, render_template, request, session, redirect
import random
from Dbconnection import Db

app = Flask(__name__)
app.secret_key="abc"

@app.route('/')
def LOGIN():
    return render_template('LOGIN.html')

    # LOGIN
@app.route('/login1',methods=['post'])
def login1():
    username=request.form['textfield1']
    password=request.form['textfield2']
    db=Db()
    c="select * from login where username='"+username+"' and password='"+password+"'"
    qry=db.selectOne(c)
    if qry is not None:
        lid=qry['id']
        liu=qry['username']
        if qry['utype'] == 'admin':
            return '''<script>alert('login successfully');window.location="/admin"</script>'''
        elif qry['utype'] =='gym instructor':
            session['lid']="lin"
            session['login_id']=lid
            session['liuu']=liu
            return '''<script>alert('login successfully');window.location="/gym_home"</script>'''
        elif qry['utype'] =='physician':
            session['lid']="lin"
            session['login_id']=lid
            session['liuu'] = liu
            return '''<script>alert('login successfully');window.location="/physician_home"</script>'''
        elif qry['utype'] =='user':
            session['lid']="lin"
            session['login_id']=lid
            session['liuu'] = liu
            return '''<script>alert('login successfully');window.location="/user_home"</script>'''
        else:
            return '''<script>alert('Invalid username');window.location="/"</script>'''
    else:
        return '''<script>alert('Invalid username or password');window.location="/"</script>'''

@app.route('/logout')
def logout():
    session['lin']=""
    return redirect('/')


    # ADMIN HOME
@app.route('/admin')
def admin_home():
    return render_template('ADMIN/adminindex.html')

    # GYM INSTRUCTOR HOME
@app.route('/gym_home')
def gym_home():
    db=Db()
    l=db.selectOne("select * from login where id='"+str(session['login_id'])+"'")
    session['u']=l['utype']
    q=db.selectOne("select * from gym_instructor where id='"+str(session['login_id'])+"'")
    session['i']=q['id']
    session['p']=q['pic']
    session['n']=q['name']
    session['e']=q['email']
    session['m']=q['phone']
    return render_template('GYM_INSTRUCTOR/gymindex.html')

    # PHYSICIAN HOME
@app.route('/physician_home')
def physician_home():
    db=Db()
    l=db.selectOne("select * from login where id='"+str(session['login_id'])+"'")
    session['u']=l['utype']
    q=db.selectOne("select * from physician where id='"+str(session['login_id'])+"'")
    session['i']=q['id']
    session['p']=q['pic']
    session['n']=q['name']
    session['e']=q['email']
    session['m']=q['phone']
    return render_template('PHYSICIAN/physician_INDEX.html')

     # USER HOME
@app.route('/user_home')
def user_home():
    db=Db()
    l=db.selectOne("select * from login where id='"+str(session['login_id'])+"'")
    session['u']=l['utype']
    q=db.selectOne("select * from user where user_id='"+str(session['login_id'])+"'")
    session['i']=q['user_id']
    session['p']=q['pic']
    session['n']=q['name']
    session['e']=q['email']
    session['m']=q['phone']
    session['b']=q['batch_id']
    return render_template('USER/USER_INDEX.html')    


#=========================================================================================================================


    # ADMIN    

    # EMPLOYEE MANAGEMENT
@app.route('/addemp',methods=['get','post'])
def add_emp():
    if request.method=="POST":
        name = request.form['textfield']
        house=request.form['textfield7']
        place = request.form['textfield5']
        post = request.form['textfield6']
        pin = request.form['textfield2']
        phone = request.form['textfield3']
        email = request.form['textfield4']
        pic = request.files['fileField']
        utype =request.form['select']
        password =random.randint(0000,9999)
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\"+date+".jpg")
        path = "/static/image/" + date + ".jpg"
        db = Db()
        if utype == 'gym instructor':
            res = db.insert("insert into login values('', '"+email+"', '"+str(password)+"', '"+utype+"')")
            db.insert("insert into gym_instructor values ('" + str(res) + "', '" + name + "', '" + house + "', '" + place + "', '" + post + "', '" + pin + "', '" + phone + "', '" + path + "', '" + email + "')")
        elif utype == 'physician':
            res = db.insert("insert into login values('', '"+email+"', '"+str(password)+"', '"+utype+"')")
            db.insert("insert into physician values ('" + str(res) + "', '" + name + "', '" + house + "', '" + place + "', '" + post + "', '" + pin + "', '" + phone + "', '" + path + "', '" + email + "')")
        return '''<script>alert('successfull');window.location="/addemp"</script>'''
    else:
        return render_template('ADMIN/ADD_EMP.html')

@app.route('/selectemployeeview')
def select_employee_view():
    return render_template('ADMIN/SELECT_EMPLOYEE_VIEW.html')

from flask import request

@app.route('/viewemployee', methods=['post'])
def view_employee():
    employee_type = request.form.get('employeeType')

    if employee_type == 'gyminstructor':
        return viewgyminstructor()
    elif employee_type == 'physician':
        return view_physician()
    else:
        # Handle invalid selection, redirect to an error page, or provide an error message
        return render_template('ADMIN/SELECT_EMPLOYEE_VIEW.html', message='Invalid employee type selection')



    # ADMIN - PHYSICIAN MANAGEMENT
@app.route('/viewphysician')
def view_physician():
    db = Db()
    result = db.select("select * from physician ")
    return render_template('ADMIN/VIEW_PHYSICIAN.html', data=result)

@app.route('/editphysician/<pid>',methods=['get','post'])
def editphysician(pid):
    if request.method=='POST':
        name = request.form['textfield']
        house = request.form['textfield7']
        place = request.form['textfield5']
        post = request.form['textfield2']
        pin = request.form['textfield6']
        phone = request.form['textfield3']
        email = request.form['textfield4']
        pic = request.files['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\" + date + ".jpg")
        path = "/static/image/" + date + ".jpg"
        db = Db()
        db.update("update physician set name='"+name+"',housename='"+house+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+phone+"',email='"+email+"',pic='"+path+"' where id='"+pid+"'")
        return '''<script>alert('successfull');window.location="/viewphysician"</script>'''
    else:
          db=Db()
          result=db.selectOne("select * from physician where id='"+pid+"' ")
          return render_template("ADMIN/UPDATE_PHYSICIAN.html",data=result)

@app.route('/deletephysician/<pid>',methods=['get','post'])
def deletephysician(pid):
    db = Db()
    db.delete("delete from physician where id = '"+pid+"'")
    return '''<script>alert('deleted successfully');window.location="/viewphysician"</script>'''


    # ADMIN - GYM INSTRUCTOR MANAGEMENT
@app.route('/viewgyminstructor')
def viewgyminstructor():
    db=Db()
    result=db.select("select * from gym_instructor")
    return render_template('ADMIN/VIEW_GYM_INSTRUCTOR.html',data=result)

@app.route('/editgym/<eid>',methods = ['get','post'])
def editgym(eid):
    if request.method == 'POST':
        name = request.form['textfield']
        house = request.form['textfield7']
        place = request.form['textfield5']
        post = request.form['textfield6']
        pin = request.form['textfield2']
        phone = request.form['textfield3']
        email = request.form['textfield4']
        pic = request.files['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\" + date + ".jpg")
        path = "/static/image/" + date + ".jpg"
        db = Db()
        db.update("update gym_instructor set name = '"+name+"',housename='"+house+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+phone+"',email='"+email+"',pic='"+path+"' where id = '"+eid+"'")
        return '''<script>alert('successfull');window.location="/viewgyminstructor"</script>'''
    else:
        db=Db()
        result=db.selectOne("select * from gym_instructor where id='"+str(eid)+"' ")
        return render_template("ADMIN/UPDATE_GYM_INSTRUCTOR.html",data=result)

@app.route('/deletegym/<eid>', methods=['get', 'post'])
def deletegym(eid):
        db = Db()
        db.delete("delete from gym_instructor where id = '" + eid + "'")
        return '''<script>alert('deleted successfully');window.location="/viewgyminstructor"</script>'''


     # VIEW USER
@app.route('/view_user')
def view_user():
    db = Db()
    result = db.select("select * from user ")
    return render_template('ADMIN/USER_VIEW.html', data=result)

@app.route('/edituser/<uid>',methods = ['get','post'])
def edituser(uid):
    if request.method == 'POST':
        name = request.form['textfield1']
        house = request.form['textfield2']
        place = request.form['textfield3']
        post = request.form['textfield4']
        pin = request.form['textfield5']
        phone = request.form['textfield6']
        email = request.form['textfield7']
        pic = request.files['fileField']
        batch = request.form['textfield8']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\" + date + ".jpg")
        path = "/static/image/" + date + ".jpg"
        db = Db()
        db.update("update user set name = '"+name+"',hname='"+house+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+phone+"',email='"+email+"',pic='"+path+"',batch_id='"+batch+"' where user_id = '"+uid+"'")
        return '''<script>alert('successfull');window.location="/view_user"</script>'''
    else:
        db=Db()
        result=db.selectOne("select * from user where user_id='"+str(uid)+"' ")
        return render_template("ADMIN/UPDATE_USER.html",data=result)

@app.route('/deleteuser/<uid>', methods=['get', 'post'])
def deleteuser(uid):
        db = Db()
        db.delete("delete from user where user_id = '"+uid+"'")
        return '''<script>alert('deleted successfully');window.location="/view_user"</script>'''



      # BATCH MANAGEMENT
@app.route('/addbatch',methods=['get','post'])
def add_batch():
     if request.method=="POST":
         batchname=request.form['textfield']
         time=request.form['textfield1']
         db=Db()
         db.insert("insert into batch values('','"+batchname+"','"+time+"')")
         return '''<script>alert('successfull');window.location="/addbatch"</script>'''
     else:
         return render_template('ADMIN/ADD_BATCH.html')

@app.route('/view_batchadmin')
def view_batchadmin():
       db = Db()
       result = db.select("select * from batch")
       return render_template('ADMIN/VIEW_BATCHadmin.html', data=result)

@app.route('/deletebatch/<bbid>', methods=['get', 'post'])
def deletebatch(bbid):
        db = Db()
        result=db.delete("delete from batch where id='"+str(bbid)+"'")
        return '''<script>alert('deleted successfully');window.location="/view_batchadmin"</script>'''



      # REQUIREMENTS MANAGEMENT
@app.route('/add_req',methods=['get','post'])
def add_req():
    if request.method == "POST":
        req = request.form['textfield1']
        pic = request.files['fileField']
        inf = request.form['textfield2']
        amt = request.form['textfield3']
        date = request.form['textfield4']
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\" + req + ".jpg")
        path = "/static/image/" + req + ".jpg"
        db=Db()
        db.insert("insert into requirements values('','"+req+"','"+path+"','"+inf+"','"+amt+"','"+date+"')")
        return '''<script>alert('successfull');window.location="/add_req"</script>'''
    else:
        return render_template('ADMIN/ADD_REQUIREMENTS.html')

@app.route('/view_req')
def view_req():
    db = Db()
    result = db.select("select * from requirements ")
    return render_template('ADMIN/VIEW_REQUIRENMENTS.html', data=result)

@app.route('/deletereq/<rid>',methods=['get','post'])
def deletereq(rid):
    db = Db()
    db.delete("delete from requirements where req_id = '"+rid+"'")
    return '''<script>alert('deleted successfully');window.location="/view_req"</script>'''



     # VIEW COMPLAINT
@app.route('/view_complaint',methods=['get','post'])
def view_complaint():
    if request.method=='POST':
        t=request.form['S']
        if t=='USER':
            db = Db()
            result = db.select("select * from complaints,user where complaints.SENDER_ID=user.user_id and complaints.TYPE='USER'")
            return render_template('ADMIN/VIEW_COMPLAINTS.html', data=result,d=t)
        if t=='GYM INSTRUCTOR':
            db = Db()
            result = db.select("select * from complaints,gym_instructor where complaints.SENDER_ID=gym_instructor.id and complaints.TYPE='GYM INSTRUCTOR'")
            return render_template('ADMIN/VIEW_COMPLAINTS.html', data=result,d=t)
        if t=='PHYSICIAN':
            db = Db()
            result = db.select("select * from complaints,physician where complaints.SENDER_ID=physician.id and complaints.TYPE='PHYSICIAN'")
            return render_template('ADMIN/VIEW_COMPLAINTS.html', data=result,d=t)
    db = Db()
    result = db.select("select * from complaints,user where complaints.SENDER_ID=user.user_id")
    return render_template('ADMIN/VIEW_COMPLAINTS.html',data=result,d='USER')


     # SEND REPLY
@app.route('/send_reply/<cid>')
def send_reply(cid):
    db=Db()
    qry=db.selectOne("select * from complaints where COMPLAINT_ID='"+cid+"'")
    return render_template('ADMIN/SEND_REPLY.html',data=qry)

@app.route('/send_reply1/<cid>',methods=['post'])
def send_reply1(cid):
    reply=request.form['textfield2']
    db=Db()
    result=db.update("update complaints set REPLY='"+reply+"',REPLY_DATE=curdate() where COMPLAINT_ID='"+cid+"'")
    return '''<script>alert('successfull');window.location="/view_complaint"</script>'''


     # VIEW_FEEDBACK
@app.route('/view_feedback')
def view_feedback():
    db = Db()
    result = db.select("select * from feedback,user where feedback.user_id=user.user_id")
    return render_template('ADMIN/VIEW_FEEDBACK.html', data=result)


     # VIEW ATTEDENCE 
@app.route('/view_attendence')
def view_attendence():
    db=Db()
    result=db.select("select * from attendence")
    return render_template('ADMIN/VIEW_ATTENTENCE.html',data=result)

     #ALLOCATE GYM INSTRUCTOR TO USERS
@app.route('/allocgymins')
def allocgymins():
    db=Db()
    result=db.select("select * from user")
    return render_template('ADMIN/ALLOCATE_INSTRUCTOR.html',data=result)

@app.route('/newalloc/<uid>')
def newalloc(uid):
    db=Db()
    result=db.select("select * from gym_instructor")
    return render_template('ADMIN/new_VIEW_GYM_INSTRUCTOR.html',data=result,uid=uid)

@app.route('/newinsert/<gym_id>/<user_id>')
def newinsert(gym_id,user_id):
   db=Db()
   db.insert("insert into alloc_gym_ins VALUES ('','"+user_id+"','"+gym_id+"')")
   return '''<script>alert('successfull');window.location="/allocgymins"</script>'''


#=========================================================================================================================


       #GYM INSTRUCTOR
    #ADD ATTENDENCE
@app.route('/add_attendence',methods=['get','post'])
def add_attendence():
    if request.method=='POST':
       batch=request.form['select']
       username=request.form['u']
       attendence=request.form['CheckboxGroup1']
       db=Db()
       db.insert("insert into attendence values('','" +username+ "',curdate(),TIME_FORMAT(CURTIME(), '%h:%i %p'), '"+batch+"','"+attendence+"')")
       return '''<script>alert('successfull');window.location="/add_attendence"</script>'''
    else:
        db=Db()
        result=db.select("select * from batch")
        return render_template('GYM_INSTRUCTOR/add_attendence.html',data=result)

@app.route('/attuserview/<bid>')
def attuserview(bid):
    db = Db()
    result = db.select("select * from user,alloc_gym_ins where alloc_gym_ins.user_id=user.user_id and gym_id='"+str(session['login_id'])+"' AND batch_id='"+bid+"'")
    return render_template("GYM_INSTRUCTOR/ajaxattendence.html",data=result)

@app.route('/inst_view_attendence')
def inst_view_attendence():
    db=Db()
    result=db.select("select * from attendence")
    return render_template('GYM_INSTRUCTOR/VIEW_ATTENDANCE.html',data=result)

@app.route('/view_requirements')
def view_requirements():
    db = Db()
    result = db.select("select * from requirements ")
    return render_template('GYM_INSTRUCTOR/VIEW_REQUIREMENTS.html', data=result)


    # ADD DIET PLANS
@app.route('/add_diet_details',methods=['get','post'])
def add_diet_details():
    if request.method=='POST':
        diet=request.form['textarea']
        user=request.form['select']
        batch=request.form['select2']
        start=request.form['textfield2']
        end=request.form['textfield4']
        db=Db()
        db.insert("insert into diet_details values('','"+batch+"','"+user+"','"+diet+"','"+start+"','"+end+"','pending')")
        return '''<script>alert('successfull');window.location="/add_diet_details"</script>'''
    else:
        db=Db()
        result=db.select("select * from user ")
        query=db.select("select * from batch ")
        return render_template('GYM_INSTRUCTOR/ADD_DIET_DETAILS.html',a=result,b=query)

@app.route('/view_diets')
def view_diets():
    db = Db()
    result = db.select("select * from diet_details")
    return render_template('GYM_INSTRUCTOR/VIEW_DIETS.html', data=result)

@app.route('/view_medicine')
def view_medicine():
    db = Db()
    result = db.select("select * from medicine")
    return render_template('GYM_INSTRUCTOR/VIEW_MEDICINE _DETAILS.html', data=result)

@app.route('/view_user1')
def view_user1():
    db = Db()
    result = db.select("select * from user left outer join alloc_gym_ins on alloc_gym_ins.user_id=user.user_id left outer join  completion on alloc_gym_ins.id=completion.ALLOCID  where gym_id='"+str(session['login_id'])+"'")
    return render_template('GYM_INSTRUCTOR/VIEW_ALLOC_USER.html', data=result)

@app.route('/gview_user')
def gview_user():
    db = Db()
    result = db.select("select * from user")
    return render_template('GYM_INSTRUCTOR/VIEW_USERS.html', data=result)

@app.route('/completion/<allocid>')
def completion(allocid):
        db=Db()
        db.insert("insert into completion VALUES('','"+allocid+"',curdate(),'0000-00-00','pending')")
        return redirect('/view_user1')

@app.route('/ucompletion/<allocid>')
def ucompletion(allocid):
    db=Db()
    db.update("update completion set ENDING_DATE=curdate(),STATUS='COMPLETED' where ALLOCID='"+allocid+"'")
    return redirect('/view_user1')

@app.route('/dcomletion/<allocid>')
def dcomletion(allocid):
    db=Db()
    db.update("update completion set ENDING_DATE=curdate(),STATUS='DROPPED' where ALLOCID='"+allocid+"'")
    return redirect('/view_user1')

@app.route('/view_completion')
def view_completion():
    db=Db()
    result = db.select("SELECT completion.STARTING_DATE, completion.ENDING_DATE, completion.STATUS, user.name AS user_name, gym_instructor.name AS instructor_name FROM completion JOIN alloc_gym_ins ON completion.ALLOCID = alloc_gym_ins.id JOIN user ON alloc_gym_ins.user_id = user.user_id JOIN gym_instructor ON alloc_gym_ins.gym_id = gym_instructor.id; ")
    return render_template('GYM_INSTRUCTOR/VIEW_COMPLETION.html', data=result)

@app.route('/view_batch')
def view_batch():
    db=Db()
    result= db.select("select * from batch")
    return render_template('GYM_INSTRUCTOR/VIEW_BATCH.html', data=result)


    # SEND COMPLAINT 
@app.route('/sendcmplts',methods=['get','post'])
def sendcmplts():
    if request.method=='POST':
        id=session['login_id']
        COMPLAINTS=request.form['textarea']
        db=Db()
        db.insert("insert into complaints VALUES ('','"+str(id)+"','"+COMPLAINTS+"',curdate(),'pending','pending',' GYM INSTRUCTOR')")
        return '''<script>alert('successfull');window.location="/sendcmplts"</script>'''
    else:
        return render_template('GYM_INSTRUCTOR/send_compliants.html')

@app.route('/view_reply')
def view_reply():
    db = Db()
    results = db.select("SELECT COMPLAINT_ID, SENDER_ID, COMPLAINTS, DATE, REPLY, REPLY_DATE FROM complaints WHERE SENDER_ID = '"+str(session['login_id'])+"'")
    return render_template('GYM_INSTRUCTOR/view_reply.html', data=results)




#=========================================================================================================================


     # USER

     # USER REGISTRTION
@app.route('/userreg',methods=['get','post'])
def userreg():
    if request.method=='POST':
        name = request.form['textfield']
        house = request.form['textfield7']
        place = request.form['textfield5']
        post = request.form['textfield2']
        pin = request.form['textfield6']
        phone = request.form['textfield3']
        email = request.form['textfield10']
        pic = request.files['fileField']
        password=request.form['textfield9']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        pic.save("C:\\Users\\Jasin\\OneDrive\\Documents\\Mini project\\fat_to_fit\\static\\image\\" + date + ".jpg")
        path = "/static/image/" + date + ".jpg"
        db = Db()
        q=db.selectOne("select * from login where username='"+email+"'")
        if q is None:
            q1=db.insert("insert into login VALUES ('','" + email + "','" + password + "','user')")
            db.insert(
                "insert into USER values ('"+str(q1)+"','" + name + "','" + house + "','" + place + "','" + post + "','" + pin + "','" + phone + "','" + str(
                    path) + "','" + email + "','pending')")
            return '''<script>alert('successfull');window.location="/"</script>'''
        else:
            return '''<script>alert('already exist');window.location="/userreg"</script>'''
    else:
        return render_template('USER/USER_REGISTRATION.html')


     # ENTER MEASURE AND FIND BMI 
@app.route('/add_measure', methods=['GET', 'POST'])
def add_measure():
    if request.method == 'POST':
        uid = session['login_id']
        h = float(request.form['height'])
        w = float(request.form['weight'])
        date = request.form['measure_date']
        bmi = cal_bmi(h, w)
        db = Db()
        db.insert("INSERT INTO measures VALUES ('', '{}', '{}', '{}', '{}', '{}')".format(uid, h, w, bmi, date))
        return '''<script>alert('Successfully added measure'); window.location="/add_measure"</script>'''
    else:
        return render_template('USER/ADD_MEASURE.html')
        
def cal_bmi(height, weight):
    if height > 0 and weight > 0:
        return weight / ((height / 100) ** 2)
    else:
        return None

@app.route('/view_measure')
def view_measure():
    db=Db()
    result = db.select("select * from measures where user_id = '"+str(session['i'])+"' ")
    return render_template('USER/VIEW_MEASURE.html', data=result)

@app.route('/del_measure/<mid>',methods=['get','post'])
def del_measure(mid):
    db=Db()
    db.delete("delete from measures where measure_id = '"+mid+"' and user_id = '"+str(session['i'])+"' ")
    return '''<script>alert('deleted successfully');window.location="/view_measure"</script>'''


    # BMI CALCULATOR
@app.route('/bmi_calc')
def bmi_calc():
    return render_template('USER/BMI_CALC.html', bmi=None, category=None)

@app.route('/calculate_bmi', methods=['post'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    
    # Convert height from centimeters to meters
    height_meters = height / 100.0
    
    if age < 18:
        bmi = calculate_bmi_value(weight, height_meters, age, is_child=True)
        category = get_bmi_category(bmi, is_child=True)
    else:
        bmi = calculate_bmi_value(weight, height_meters, age)
        category = get_bmi_category(bmi)
    
    return render_template('USER/BMI_CALC.html', bmi=bmi, category=category)

def calculate_bmi_value(weight, height, age, is_child=False):
    if is_child:
        # BMI calculation for children and teens
        return round((weight / (height ** 2)), 2)
    else:
        # BMI calculation for adults
        return round(weight / (height ** 2), 2)

def get_bmi_category(bmi, is_child=False):
    if is_child:
        return get_child_bmi_category(bmi)
    else:
        return get_adult_bmi_category(bmi)

def get_child_bmi_category(bmi):
    if bmi < 5:
        return 'Underweight'
    elif 5 <= bmi < 85:
        return 'Healthy weight'
    elif 85 <= bmi < 95:
        return 'Overweight'
    else:
        return 'Obese'

def get_adult_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'



@app.route('/view_allocated_instructor')
def view_allocated_instructor():
    db=Db()
    result = db.select("SELECT * FROM gym_instructor JOIN alloc_gym_ins WHERE alloc_gym_ins.gym_id = gym_instructor.id AND alloc_gym_ins.user_id = '"+str(session['i'])+"'")
    return render_template('USER/VIEW_ALLOCATED.html',data=result)

@app.route('/view_user_gym')
def view_user_gym():
    db=Db()
    result=db.select("select * from gym_instructor")
    return render_template('USER/VIEW_GYM_INSTRUCTOR.html',data=result)

    # MEDICINE (USER)
@app.route('/bookmed')
def bookmed():
    db=Db()
    result=db.select("select * from medicine ")
    return render_template('USER/BOOK_MED.html', data=result)

@app.route('/bookmed2/<b>', methods=['get', 'post'])
def bookmed2(b):
    if request.method == 'POST':
        quantity = request.form['textfield']
        db = Db()
        # Fetch MEDICINE_PRICE from the 'medicine' table
        medicine_price_query = db.selectOne("SELECT MEDICINE_PRICE FROM medicine WHERE mid = '" + b + "'")
        medicine_price = medicine_price_query['MEDICINE_PRICE'] if medicine_price_query else 0
        amount = int(quantity) * medicine_price
        q1 = db.insert("INSERT INTO `order` VALUES ('', '"+b+"','" + str(session['login_id']) + "', '" + quantity + "', '" + str(amount) + "', 'booked')")    
        return '''<script>alert('Successful');window.location="/bookmed"</script>'''
    else:
        return render_template('USER/BOOK_QUANTITY.html')


@app.route('/mycart',methods=['get','post'])
def mycart():
    db=Db()
    result=db.select("select * from medicine,`order` where medicine.mid=order.medid and order.user_id='"+str(session['login_id'])+"'")
    q1 = db.selectOne("select  sum(medicine.MEDICINE_PRICE*order.quantity) as c from medicine,`order` where order.medid=medicine.mid and order.user_id='" + str(session['login_id']) +"'")
    session['amnt']=q1['c']
    return render_template('USER/BOOKING.html', data=result,d=q1['c'])


@app.route('/uview_batch')
def uview_batch():
    db=Db()
    result= db.select("select * from batch")
    return render_template('USER/VIEW_BATCH.html', data=result)


@app.route('/uview_attendance')
def uview_attendance():
    db = Db()
    results = db.select("SELECT * FROM attendence WHERE username = '"+session['n']+"'")
    return render_template('USER/VIEW_ATTENDANCE.html', data=results)


@app.route('/uview_diets')
def uview_diets():
    db = Db()
    results = db.select("select * from diet_details where name = '"+session['n']+"'")
    return render_template('USER/VIEW_DIETS.html', data=results)

@app.route('/start_diet/<nm>')
def start_diet(nm):
        db = Db()
        db.update("UPDATE `diet_details` SET `status`='started' WHERE `name`= '"+nm+"'")
        return redirect('/uview_diets')

@app.route('/end_diet/<nm>')
def end_diet(nm):
        db = Db()
        db.update("UPDATE `diet_details` SET `status`='completed' WHERE `name`= '"+nm+"'")
        return redirect('/uview_diets')


@app.route('/uview_requirements')
def uview_requirements():
    db = Db()
    result = db.select("select * from requirements ")
    return render_template('USER/VIEW_REQUIREMENTS.html', data=result)


    # ASK DOUBTS AND VIEW REPLY (USER)
@app.route('/ask_doubt',methods=['get','post'])
def ask_doubts():
    if request.method=='POST':
        uid = session['login_id']
        USERNAME=session['liuu']
        DETAILS=request.form['textarea']
        db=Db()
        db.insert("insert into doubts VALUES ('','"+str(uid)+"','"+str(USERNAME)+"',curdate(),'"+DETAILS+"','pending','pending')")
        return '''<script>alert('successfull');window.location="/ask_doubt"</script>'''
    else:
        return render_template('USER/ADD_DOUBTS.html')

@app.route('/view_doubtreply')
def view_doubtreply():
    db = Db()
    results = db.select("SELECT DATE, DETAILS, REPLY, REPLY_DATE FROM doubts WHERE uid = '"+str(session['login_id'])+"'")
    return render_template('USER/VIEW_DOUBTSREPLY.html', data=results)


@app.route('/sndfeedback',methods=['get','post'])
def sndfeedback():
    if request.method=='POST':
        feedback=request.form['textarea']
        user_id = session['login_id']
        db=Db()
        db.insert("insert into feedback VALUES ('','"+str(user_id)+"','"+feedback+"',curdate())")
        return '''<script>alert('successfull');window.location="/sndfeedback"</script>'''
    else:
        return render_template('USER/SEND_FEEDBACK.html')


     # SEND COMPLAINTS AND VIEW REPLY (USER)
@app.route('/sendcmplnts',methods=['get','post'])
def sendcmplnts():
    if request.method=='POST':
        id=session['login_id']
        COMPLAINTS=request.form['textarea']
        db=Db()
        db.insert("insert into complaints VALUES ('','"+str(id)+"','"+COMPLAINTS+"',curdate(),'pending','pending',' USER')")
        return '''<script>alert('successfull');window.location="/sendcmplnts"</script>'''
    else:
        return render_template('USER/send_compliants.html')

@app.route('/uview_reply')
def uview_reply():
    db = Db()
    results = db.select("SELECT COMPLAINT_ID, SENDER_ID, COMPLAINTS, DATE, REPLY, REPLY_DATE FROM complaints WHERE SENDER_ID = '"+str(session['login_id'])+"'")
    return render_template('USER/VIEW_REPLY.html', data=results)



#=========================================================================================================================

     # PHYSICIAN

     # MEDICINES MANAGEMENT
@app.route('/addmed',methods=['get','post'])
def addmed():
    if request.method=='POST':
        MEDICINE_NAME=request.form['textfield']
        MEDICINE_DETAILS=request.form['textarea']
        MEDICINE_PRICE=request.form['textfield2']
        db = Db()
        db.insert( "insert into medicine VALUES('','" + MEDICINE_NAME + "','" + MEDICINE_DETAILS + "','" + MEDICINE_PRICE + "')")
        return '''<script>alert('successfull');window.location="/addmed"</script>'''
    else:
        return render_template('PHYSICIAN/ADD_MEDICINE.html')

@app.route('/viewmed')
def vieWmed():
    db = Db()
    result = db.select("select * from medicine")
    return render_template('PHYSICIAN/VIEW_MED.html', data=result)

@app.route('/deletemed/<mid>',methods=['get','post'])
def deletemed(mid):
    db = Db()
    db.delete("delete from medicine where mid = '"+mid+"'")
    return '''<script>alert('deleted successfully');window.location="/viewmed"</script>'''


@app.route('/view_bookmed')
def view_bookmed():
    db = Db()
    result = db.select("SELECT u.name AS username, u.pic AS pic, m.MEDICINE_NAME AS medicine, m.MEDICINE_PRICE AS medicineprice, o.id, o.quantity, o.status, o.amount  FROM `order` o  JOIN `user` u ON o.user_id = u.user_id JOIN `medicine` m ON o.medid = m.mid")
    return render_template('PHYSICIAN/VIEW_ORDERED_DETAILS.html', data=result)

@app.route('/approve/<apid>')
def approve(apid):
        db = Db()
        db.update("UPDATE `order` SET `status`='ordered' WHERE `id`= '"+apid+"'")
        return redirect('/view_bookmed')

@app.route('/viewuserp')
def viewuserp():
    db = Db()
    result = db.select("select * from USER ")
    return render_template('PHYSICIAN/VIEW_USER.html', data=result)


@app.route('/pview_diets')
def pview_diets():
    db = Db()
    result = db.select("select * from diet_details")
    return render_template('PHYSICIAN/VIEW_DIETS.html', data=result)

    # VIEWS DOUBTS AND SEND REPLY
@app.route('/view_doubtsp')
def view_doubtsp():
    db = Db()
    result = db.select("select * from doubts ")
    return render_template('PHYSICIAN/VIEW_DOUBTS.html', data=result)

@app.route('/prply/<ppid>',methods=['get','post'])
def prply(ppid):
    if request.method == 'POST':
        REPLY=request.form['textarea']
        db = Db()
        db.update("update doubts set REPLY='"+REPLY+"',REPLY_DATE=curdate() where id='"+ppid+"'")
        return '''<script>alert('successfull');window.location="/view_doubtsp"</script>'''
    else:
        return render_template('PHYSICIAN/SEND_REPLY.html')


@app.route('/sendcmplts_physician',methods=['get','post'])
def sendcmplts_physician():
    if request.method=='POST':
        id=session['login_id']
        COMPLAINTS=request.form['textarea']
        db=Db()
        db.insert("insert into complaints VALUES ('','"+str(id)+"','"+COMPLAINTS+"',curdate(),'pending','pending','PHYSICIAN')")
        return '''<script>alert('successfull');window.location="/sendcmplts_physician"</script>'''
    else:
        return render_template('PHYSICIAN/send_compliants.html')

@app.route('/pview_reply')
def pview_reply():
    db = Db()
    results = db.select("SELECT COMPLAINT_ID, SENDER_ID, COMPLAINTS, DATE, REPLY, REPLY_DATE FROM complaints WHERE SENDER_ID = '"+str(session['login_id'])+"'")
    return render_template('PHYSICIAN/view_reply.html', data=results)






if __name__ == '__main__':
    app.run(host="0.0.0.0")

