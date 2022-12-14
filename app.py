




from flask import Flask,render_template,send_file,request
import json
from  urllib.parse import unquote
import requests
import db

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/css/<path:path>')
def css(path):

    return send_file(f'templates/{path}')

@app.route('/images/<path:path>')
def image(path):

    return send_file(f'templates/images/{path}')



def ban_ch(user):
    if db.st(user)=='free':
        return True
    else:
        return False

admins=[['FSC','UNKN0WN'],['fsc3301@1033','unkn0wn.404.us3r']]
@app.route('/login/',methods=['GET','POST'])
def login():


        Username=request.form['User'].upper()
        Password=request.form['Pass']

        f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'User':Username,'Pass':Password}).json()



        if f['message']=='NF' :
            response=json.dumps({
                        "message":"Login Failed , Account Not Found",
                        "Username:":Username,
                        "Password:":Password})
            return response


        else :

                if f['message']=='ban':
                        return render_template('./ban/ban.html')
                elif f['message']=='admin':



                            return render_template('./admin/index.html',token=f['token'])

                elif  f['message']=='flag' :



                            return render_template('./flag/index.html',token=f['token'],score=f['score'])



                else:
                    return render_template("./login/login.html",data=f['token'])


@app.route('/video',methods=['GET','POST'])
def video():
    return send_file("templates/login/video/one-eye.mp4")

@app.route('/email/',methods=['GET','POST'])
def email():

    email=unquote(request.form['email'])
    token=unquote(request.form['token'])

    full_resalt=requests.post('https://fsc3301.pythonanywhere.com/email/',data={'email':email,'token':token})

    return render_template('./index.html')

upd={
    True:False,
    False:True
}

up=True


@app.route('/admin/',methods=['GET','POST'])
def admin():

    work=request.form['w']
    token=unquote(request.form['token'])

    tokens=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'token','token':token}).json()['message']

    if tokens==True:
        if work=='up':
            global up,upd
            up=upd[up]


        if work =='add':


            return render_template('admin/add/index.html',token=token)
        elif work=='ban':
            return render_template('admin/ban/index.html',token=token)
        elif work=='add_user':


            User=request.form['user']

            Pass=request.form['pass']
            u_token=request.form['maintoken']
            level=request.form['level']

            if len(User)<3 or len(Pass)<3:
                return {'message':'Failed'}
            else:

                    x= requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'add_user','token':token,'User':User,'Pass':Pass,'email':'NULL','u_token':u_token,'level':str(level) }).json()['message']
                    if x=='DONE':
                                return {'message':'DONE'}
                    elif x=='AE' :
                                return {'message':'This Account Already Exists'}
                    else:
                        return {'message':'Failed'}


        elif work=='ban_user':

            try:
                    User=request.form['user']


                    if User.upper()=='FSC':
                        return {'message':'Access Denied'}
                    else:
                        x=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'ban_user','token':token,'User':User}).json()['message']

                        if x=='DONE':

                            return {'message':'DONE'}
                        else:
                            return {'message':'Failed'}
            except:
                    return {'message':'Failed'}

        elif work=='free_user':
            try:
                    User=request.form['user']
                    if User.upper()=='FSC':
                        return {'message':"Access Denied"}
                    else:
                        x=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'free_user','token':token,'User':User}).json()['message']

                        if x == 'DONE':

                            return {'message':'DONE'}
                        else:
                            raise TypeError
            except:
                    return {'message':'Failed'}
        else:
            if work=='log' and ([token=='=fsc@*#Y*EHI3301' or token=='(unkn0wn)*@#(UJE.404))']):
                try:

                    log=requests.get('https://fsc3301.pythonanywhere.com/admin',data={'w':'log','token':token})
                    return json.dumps(log.json())

                except:
                    return {'message':'Failed'}
            elif work=='del' and token=='=fsc@*#Y*EHI3301':
                User=request.form['user']

                x=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'del','token':token,'user':User}).json()

                if x['message']==True:
                    return {'message':'Done'}
                elif x['message']=='AF':
                    return {'message':'Account Not Found'}
                elif x['message']=='AD':
                    return {'message':'Access Denied'}
                else:
                    return {'message':'Failed'}
            else:return {'message':'Access Denied'}








@app.route('/flag/',methods=['GET','POST'])
def flag():
    fg=unquote(request.form['flag'])
    token=request.form['token']
    tokens=requests.post('https://fsc3301.pythonanywhere.com/flag/',data={'token':token}).json()['message']
    def red(token):
        return redirect(url_for('login', T=token),code=307)
    if tokens == 'None' or tokens not in ['AF','AL']:
           
       
            levels=str(tokens)
            levels= levels if levels!=None else ''
            
            if fg=='FSC{Thus_The_World_Was_Created}':
                if '1' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'1'}).json()['message']:
                        red(token)
                else:
                    
                    raise TypeError
                
            elif fg=='FSC{Every_Death_Is_Just_A_New_Beginning}':
                if '2' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'2'}).json()['message']:
                        red(token)
                else:
                    raise TypeError
            elif fg=='FSC{GODHASNOPLANFORUS}' or fg=='FSC{GOD_HAS_NO_PLAN_FOR_US}':
                if '3' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'3'}).json()['message']:
                        red(token)
                else:
                    raise TypeError
            elif fg=='FSC{WR_FSC}' or fg=='FSC{wr_fsc}':
                if '4' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'4'}).json()['message']:
                        red(token)
                else:
                    raise TypeError
            else:
                return {'message':'Wrong Flag'}

        
        

    else:
        return {'message':'Account Not Found'}
chall={
    '1':'templates/flags/level1/level1.txt',
    '2':'templates/flags/level2/level2.rar',
    '3':'templates/flags/level3/Mos.txt',
    '4':'templates/flags/level4/erdos.txt',
}
  
   
@app.route('/challenge/<path:path>/<string:t>',methods=['GET','POST'])
def challenge(path,t):
    global chall
    path=unquote(path)
    token=unquote(t)
    print(path,token)
    tokens=requests.post('https://fsc3301.pythonanywhere.com/flag/',data={'token':token}).json()['message']
    print(tokens)
    level=str(path)
    if tokens=='None' or tokens == 'None' or tokens not in ['AF','AL']:
        print(chall[level])
        try:
            return send_file(chall[level], as_attachment=True)
        except KeyError:
            return {'message':"Challenge Not Found"}
    else:
        return {'message':'Account Not Found'}

@app.route('/js/<path:path>',methods=['GET','POST'])
def js(path):
   
    print(path)
    return render_template(f'{path}')



@app.route('/js/<path:path>',methods=['GET','POST'])
def js(path):


    return render_template(f'{path}')







if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,threaded=True)



