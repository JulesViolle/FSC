




from flask import Flask,render_template,send_file,request,redirect,url_for,make_response
import json
from  urllib.parse import unquote
import requests
import pybase64,time,threading

g=""" <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        

        html, body {
          width: 100%;
          height: 100%;
          margin: 0;
        }

        * {
          font-family: "Press Start 2P", cursive;
          box-sizing: border-box;
        }

        #app {
          padding: 1rem;
          background: black;
          display: flex;
          height: 100%;
          justify-content: center;
          align-items: center;
          color: #54FE55;
          text-shadow: 0px 0px 10px;
          font-size: 6rem;
          flex-direction: column;
        }
        #app .txt {
          font-size: 1.8rem;
        }

        @keyframes blink {
          0% {
            opacity: 0;
          }
          49% {
            opacity: 0;
          }
          50% {
            opacity: 1;
          }
          100% {
            opacity: 1;
          }
        }
        .blink {
          animation-name: blink;
          animation-duration: 1s;
          animation-iteration-count: infinite;
        }
            @font-face {
            font-family: 'Press Start 2P';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK3nYivN04w.woff2) format('woff2');
            unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
          }
          /* cyrillic */
          @font-face {
            font-family: 'Press Start 2P';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK3nRivN04w.woff2) format('woff2');
            unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
          }
          /* greek */
          @font-face {
            font-family: 'Press Start 2P';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK3nWivN04w.woff2) format('woff2');
            unicode-range: U+0370-03FF;
          }
          /* latin-ext */
          @font-face {
            font-family: 'Press Start 2P';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK3nbivN04w.woff2) format('woff2');
            unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
          }
          /* latin */
          @font-face {
            font-family: 'Press Start 2P';
            font-style: normal;
            font-weight: 400;
            src: url(https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK3nVivM.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
          }
    
    </style>
    <title>Waiting</title>
    <div id="app">
        <div></div>
        <div class="txt">
           Site Is Being Updated!<span class="blink">_</span>
        </div>
     </div>
        
    
    
</head>
<body>
    
</body>
</html>"""








app=Flask(__name__)
users_id=[]


def clear_cookie():
    global users_id
    while True:
        time.sleep(300)
        users_id.clear()

#threading.Thread(target=clear_cookie).join


@app.route('/')
def index():
    global users_id
    
    userid=request.cookies.get("userID") 
   
    if userid==None or userid=='':
            
            return render_template('./index.html')
    else:
        req=requests.post("https://fsc3302.pythonanywhere.com/sadkaidaojd536/token",data={'Token':userid,"Data":"chk"}).json()['message']
        if req==True:
            userid=json.loads(str(pybase64.b64decode(request.cookies.get("userID")).decode()))
        
            return login(userid['user'],userid['pass'])
        else:
            return render_template('./index.html')
        
@app.route('/536')
def P_536():
    return render_template('./536.html')

@app.route('/css/<path:path>')
def css(path):
    
    return send_file(f'templates/{path}')

@app.route('/images/<path:path>')
def image(path):
    
    return send_file(f'templates/images/{path}')





admins=[['FSC','UNKN0WN'],['fsc3301@1033','unkn0wn.404.us3r']]
@app.route('/login/',methods=['GET','POST'])
def login(User='None',Pass='None'):
            global users_id
        
            
            try:
                if any([User=='None',Pass=='None']):
                    Username=''.join(request.form['User'].split()).upper()
                    Password=''.join(request.form['Pass'].split())
                    
                    f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'User':Username,'Pass':Password}).json()
                    print(f)
                else:
                    f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'User':User,'Pass':Pass}).json()
                    
                    
            except:
                
                try:
                    token=request.args.get('T')
                
                    f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'T':token}).json()
                except:
                    
                    response=make_response(render_template('./index.html'))
                    return response
           
            if f['message']=='NF' :
            
                response=make_response(redirect('/'))
                return response

            else :
                
                    if f['message']=='ban':
                            return render_template('./ban/ban.html')
                    elif f['message']=='admin':
                                
                            
                            response=make_response(render_template('./admin/index.html',token=f['token']))
                            
                                

                    elif  f['message']=='flag' :
                            
                            if sorted(str(f['level']))==['1','2','3','4']:
                                    
                                    response=make_response(render_template('./Done/finish.html'))
                            
                            else:  
                                    response=make_response(render_template('./Done/finish.html'))
                                    #return render_template('./flag/index.html',token=f['token'],score=f['score'])  
                                
                                
                                
                    else:
                        response=make_response(render_template("./login/login.html",data=f['token']))
                    if all([User=='None',Pass=='None']):
                        id=pybase64.b64encode(('{'+f'"user":"{Username}","pass":"{Password}"'+'}').encode())

                        response.set_cookie("userID",id)
                        
                        req=requests.post("https://fsc3302.pythonanywhere.com/sadkaidaojd536/token",data={'Token':id.decode(),"Data":"add"})
                        return response
                    else:
                        return response
        
@app.route('/video',methods=['GET','POST'])
def video():
    return send_file("templates/login/video/one-eye.mp4")                    

@app.route('/email/',methods=['GET','POST'])
def email():
    try:
        email=unquote(request.form['email'])
        token=unquote(request.form['token'])
        print(email,token)
        full_resalt=requests.post('https://fsc3301.pythonanywhere.com/email/',data={'email':email,'token':token}).json()['message']
        
        return render_template('./index.html')
    except:
        return error_handler()

upd={
    True:False,
    False:True
}

up=True


@app.route('/admin/',methods=['GET','POST'])
def admin():
    try:
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
                print(User,Pass,u_token,level)
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

                        print({'w':'ban_user','token':token,'User':User})
                        if User.upper()=='FSC':
                            return {'message':'Access Denied'}
                        else:
                            x=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'ban_user','token':token,'User':User}).json()['message']
                            print(x)
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
                            print(x)
                            if x == 'DONE':

                                return {'message':'DONE'}
                            else:
                                raise TypeError
                except:
                        return {'message':'Failed'}
            else:
                if work=='log' and ([token=='=fsc@*#Y*EHI3301' or token=='(unkn0wn)*@#(UJE.404))']):
                    try:
                        log=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'log','token':token}).json()
                        return log
                    except:
                        return {'message':'Failed'}
                elif work=='del' and token=='=fsc@*#Y*EHI3301':
                    User=request.form['user']

                    x=requests.post('https://fsc3301.pythonanywhere.com/admin/',data={'w':'del','token':token,'user':User}).json()
                    
                    if x['message']==True:
                        return {'message':'Done'}
                    elif x['message']=='AF':
                        return error_handler()
                    else:
                        return {'message':'Failed'}
                else:return {'message':'Access Denied'}
    except:
        return error_handler()




@app.route('/flag/',methods=['GET','POST'])
def flag():
    fg=unquote(request.form['flag'])
    token=request.form['token']
    tokens=requests.post('https://fsc3301.pythonanywhere.com/flag/',data={'token':token}).json()['message']
    def red(token):
        return redirect(url_for('login', T=token),code=307)
    if tokens == 'None' or tokens not in ['AF','AL']:
        try:  
       
            levels=str(tokens)
            levels= levels if levels!=None else ''
            if sorted(levels)==['1','2','3','4']:
                return render_template('/Done/finish.html')
            if fg=='FSC{Thus_The_World_Was_Created}':
                if '1' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'1'}).json()['message']:
                        return red(token)
                else:
                    
                    raise TypeError
                
            elif fg=='FSC{Every_Death_Is_Just_A_New_Beginning}':
                if '2' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'2'}).json()['message']:
                        return red(token)
                else:
                    raise TypeError
            elif fg=='FSC{GODHASNOPLANFORUS}' or fg=='FSC{GOD_HAS_NO_PLAN_FOR_US}':
                if '3' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'3'}).json()['message']:
                        return red(token)
                else:
                    raise TypeError
            elif fg=='FSC{WR_FSC}' or fg=='FSC{wr_fsc}':
                if '4' not in levels:
                    if requests.post('https://fsc3301.pythonanywhere.com/add_level/',data={'token':token,'lv':'4'}).json()['message']:
                        return red(token)
                else:
                    raise TypeError
            else:
                return  red(token)
        except TypeError:
            return  red(token)
        
        

    else:
        return error_handler()
chall={
    '1':'./flags/level1/level1.txt',
    '2':'./flags/level2/level2.rar',
    '3':'./flags/level3/Mos.txt',
    '4':'./flags/level4/erdos.txt',
}
  
   
@app.route('/challenge/<path:path>/<string:t>',methods=['GET','POST'])
def challenge(path,t):
    global chall
    path=unquote(path)
    token=unquote(t)
    
    tokens=requests.post('https://fsc3301.pythonanywhere.com/flag/',data={'token':token}).json()['message']
    
    level=str(path)
    if tokens=='None' or tokens == 'None' or tokens not in ['AF','AL']:
        
        try:
            return send_file(chall[level], as_attachment=True)
        except KeyError:
            return {'message':"Challenge Not Found"}
    else:
        return error_handler()

@app.route('/js/<path:path>',methods=['GET','POST'])
def js(path):
   
    print(path)
    try:
        return render_template(f'{path}')
    except:
        return error_handler()
@app.errorhandler(404)
def E_404(x):
    return render_template('404/404.html')
@app.errorhandler(Exception)
def error_handler(error):
    return render_template('./ban/ban.html')
        
    
    
#@app.before_request
#def before_request_func():
    
    #response=make_response(g)
    #return response






