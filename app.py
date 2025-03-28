from flask import Flask,render_template,send_file,request,redirect,url_for,make_response,abort,Response
from flask_turnstile import Turnstile

import json
from  urllib.parse import unquote
import requests
import pybase64,time
import threading,time
import secrets

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode




pri_key=b'0\x82\x02[\x02\x01\x00\x02\x81\x81\x00\xbb\x89\x98\x91B\xc2\xee\xde\x0b\xc2\xee\xc6h\x04]_\xe6\xd7\xa8\x93B\xe7(\xd5\xea\x01!\xa6\x04\xc6\x95\xbf\xect\x89\x1b\xfc\xb7\xac\x0f_\x9d\xab\xa0\xfc:\xf8\xb3\xb2\xf9\xc6\xdcd\x10\xed9cJ\x8e\x7f\xcc/\xb9Y\xa8\xbc\x9c\x8e@\xe5L\xf2\xea\xb2r\xb8\x95\xe9\x18G\x87\xfe:\xccM\xc9D\x1b[\xad\x95\x9a\x976\x82\x07\xb8}\x1c\xd4\xff\xa8\xf6\xe4\xe5\\\xe1ot\x03)\x03\xc7+\x18$\xe7\x07\xa9\xfe\xcd3z\x00(\x17\xe6#\x02\x03\x01\x00\x01\x02\x81\x80FM\xd4`\xacf\xf8vLqt\xe2\xf3N\xa3\x94\x96\xad\x058\xc3\x8du\xfd\x0f\x7f\x02\x16\xc3V\x91\x00\x04\x8cAt8\xfe\xc0%yBY\xfb}c<%\xdd\xb4\x0e\x8dC\x84&\xf2k\x1b!\xa5\x9e-\xcb\xed@\xd5!4\xb4\x9d\x9cw\xfd\xb9\x1a:S\xfbg*\xa6f\xb9\xb3\xf6\x15\x8a\xa3\x89!\xc15\x97\xac\xbb\xd0\xc2S\x0c\xb0\xc8}\xa6f\x8eY\x89\xc0\xdf.n\xe8\x18\x15\xec1\xe7\x9f\xe1.\xfb\x08\x0e.\r +a\x02A\x00\xd3V>\xe3\xbb%\xcd\x14K\x8e\xeb\x95\x8b@\x9a\xf4j\xber\x86\x96\'5pQ$\xc1S\xb0\xfb0{\x13\x06=\xdd\xf1\xbd\x05Bby\xf6\xc1\xb8<J\xd8\xb8 \xf1\xa7\xe0Z\xf3\xcb,EV 8\x99\x82\x03\x02A\x00\xe3+\xc0\xfc\r\xedK8\xe7\x03\x8fo\xe0\x19\xe1\xc9|\xfb\x98\x00\x1dn\x00\xach\x96\x11\xbc\x1b\xb2\xa0:\xd0\x08\nD7w^&p\x86\x90\x85\x98\xd0\xa8\x08\x16\xfe\xba.[\xadB\xc1\xa6\x1es\x15\xd6\xe3\xe1a\x02@m3{{\xa1\x10\x7fO\xa5[LP\x11\x8ch\x853C\x05Z\x95\xeb\xdc\xa9\x14\xc4\xb1@\xd5\x8av\x1a\xa2Q\xefU\xe7\xbb\x8c$)Nl:\xdd@\nL\xc1\x98\x04F\x82\x9f|\xa9\xd7N\\\x9ay\xa4\x98\x91\x02@He\xabM(\xcb\x15\x0b\xffc}\x14\xf4`\x8b:\x81`U"\xc4>Hl\xa9\xb0\x19\xda\xcf \xf0;\x8e\x0c\xe1\xe8\xb7\x9c\x8d\x1e\xc7\x01\xbb\x918\x10W\\\xac\xa7e\x82\\\xa9,\xfb6\x0b\xc25\x95\x94nA\x02@\x07\xc8 ,\x96\x1b\xef\xf5\x03\xcb\xf3\xca\xe6Aq;"\x06$\x8f\x15X\xc8Z\xd5\xba\x05\x90\xb5We\xf7\xe9\xaf\xe8M\xedh\xfa\x83\xd4Y,\xa3\xde\xbam\x9fvd\t\xd3\x9b\xd7\xc1J7\x82"\xd9\xea2\x8c\\'

pub_key=b'0\x81\x9f0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x81\x8d\x000\x81\x89\x02\x81\x81\x00\xbb\x89\x98\x91B\xc2\xee\xde\x0b\xc2\xee\xc6h\x04]_\xe6\xd7\xa8\x93B\xe7(\xd5\xea\x01!\xa6\x04\xc6\x95\xbf\xect\x89\x1b\xfc\xb7\xac\x0f_\x9d\xab\xa0\xfc:\xf8\xb3\xb2\xf9\xc6\xdcd\x10\xed9cJ\x8e\x7f\xcc/\xb9Y\xa8\xbc\x9c\x8e@\xe5L\xf2\xea\xb2r\xb8\x95\xe9\x18G\x87\xfe:\xccM\xc9D\x1b[\xad\x95\x9a\x976\x82\x07\xb8}\x1c\xd4\xff\xa8\xf6\xe4\xe5\\\xe1ot\x03)\x03\xc7+\x18$\xe7\x07\xa9\xfe\xcd3z\x00(\x17\xe6#\x02\x03\x01\x00\x01'

enc_fund = PKCS1_OAEP.new(RSA.import_key(pub_key))
dec_func = PKCS1_OAEP.new(RSA.import_key(pri_key))



error_503= """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
            /* cyrillic-ext */
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


            html, body {
              width: 100%;
              height: 100%;
              margin: 0;
            }

            * {
              font-family: cursive;
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
            </style>
            <title>503</title>
            <div id="app">
                <div>503</div>
                <div class="txt">
                   Server Unavailable<span class="blink">_</span>
                </div>
             </div>



        </head>
        <body>

        </body>
        </html>
        """










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
TURNSTILE_ENABLED = True
TURNSTILE_SITE_KEY = "0x4AAAAAAALlVPrBCGi_rKKF"
TURNSTILE_SECRET_KEY = "0x4AAAAAAALlVH0EuAFTC3tN-W3dZzvNOGI"
app.config.from_object(__name__)

turnstile = Turnstile(app=app)

users_id=[]






#zeno project



@app.route('/zeno',defaults={'path': ''})
@app.route('/zeno/<path:path>')
def zeno(path):
    try:
        if not path:
            
            returnsend_file(f"./templates/action-zeno/zeno-download.bat",as_attachment=True)
        
        return send_file(f"./templates/action-zeno/{path}",as_attachment=True)
    except Exeptions as e:
        print(e)
        return E_404()













@app.route('/loaderio-7dc47f6d7753312dff8be7c900cbb39b.txt')
def loader():
    return send_file("./loaderio-7dc47f6d7753312dff8be7c900cbb39b.txt")



musics={
    1:r"./templates/audio/Apokalypse.mp3",
    0:r"./templates/audio/God.mp3",
}
@app.route('/FdasfaasdsDSDGod/music/',methods=['GET','POST'])
def music_Finished():
    #secretsGenerator = secrets.SystemRandom()
    #music = secretsGenerator.randint(0,1)
    
    return make_response(send_file(r"./templates/audio/God.mp3"))
    #return make_response(send_file(musics[music]))






ch_g=False
ch={
    True:False,
    False:True
}
@app.route("/fsc/update/KDIjasdasoijdnfs3306")
def chall():
    global ch_g,ch
    ch_g=ch[ch_g]
    return {"Message":"Done"}




mainpage="index.html"

@app.route('/')
def index():
    global users_id
    try:
        if request.args.get('ReturnUrl')=="login":
            response=make_response(render_template(f'./{mainpage}'))
            return response
        
        userid=request.cookies.get("userID")

        if userid==None or userid=='':

                return render_template(f'./{mainpage}')
        else:
                try:
                    

                    
                    

                    userid=dec_func.decrypt(b64decode(request.cookies.get("userID").encode('utf-8')))
                    
                    userid=json.loads(b64decode(userid))
                    
                    response=make_response(login(userid['user'],userid['pass'],cookie=True))
                    return response
                except:
                   return render_template(f'./{mainpage}')
    except:
        return E_404()

@app.route('/536')
def P_536():
    try:
        return render_template('./536.html')
    except:
        return E_404()
@app.route('/css/<path:path>')
def css(path):
    try:
        return send_file(f'templates/{path}')
    except:
        return E_404()
@app.route('/images/<path:path>')
def image(path):
    try:
        return send_file(f'templates/images/{path}')
    except:
        return E_404()


    

admins=[['FSC','UNKN0WN'],['fsc3301@1033','unkn0wn.404.us3r']]
@app.route('/login/',methods=['GET','POST'])
def login(User='None',Pass='None',cookie=False):
            global users_id,challenge
            captcha=False

            try:
                
                
                if cookie==True:
                    captcha=True
                    
                    
                
                        


                    
                    
                else:
                    if turnstile.verify():
                        captcha=True
                    
                if captcha==True:
                    try:
                            if any([User=='None',Pass=='None']):
                                Username=''.join(request.form['User'].split()).upper()
                                Password=''.join(request.form['Pass'].split())

                                f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'User':Username,'Pass':Password}).json()
                                
                            else:
                                f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'User':User,'Pass':Pass}).json()


                    except:

                        try:
                                token=request.args.get('T')

                                f=requests.post('https://fsc3301.pythonanywhere.com/login/',data={'T':token}).json()
                        except:

                                #response=make_response(render_template(f'./{mainpage}'))
                                #return response
                            
                                response=make_response(redirect('/'))
                                return response
                        
                    if f['message']=='NF' :

                        response=make_response(redirect('/'))
                        return response

                    else :
                            if User=='None' and Pass=='None' :
                                
                                id=enc_fund.encrypt(pybase64.b64encode(('{'+f'"user":"{Username}","pass":"{Password}"'+'}').encode()))
                                response=make_response(redirect('/'))
                                response.set_cookie("userID",b64encode(id).decode())

                                
                            
                                return response
                            
                            
                            if f['message']=='ban':
                                    return render_template('./ban/ban.html')
                            elif f['message']=='admin':


                                    response=make_response(render_template('./admin/index.html',token=f['token']))
                                    return response


                            elif  f['message']=='flag' :
                                    
                                    if f['status']=="True":
                                        if sorted(str(f['level']))==['1','2','3','4','5']:

                                            response=make_response(render_template('./Done/finish.html'))
                                        else:

                                            return render_template('./flag/index.html',token=f['token'],score=f['score'])

                                    else:

                                            
                                            return render_template('./Done/finish.html')

                            else:
                                response=make_response(render_template("./login/login.html",data=f['token']))
                                return response    
                else:
                        return {"Error":"Captcha Failed"}


                
            except:
                return E_404()

@app.route('/flag/flag.html')
def flag_html():
    return render_template('./flag/index.html',score=0)

@app.route('/video',methods=['GET','POST'])
def video():
    try:
        return send_file("templates/login/video/one-eye.mp4")
    except:
        return E_404()
@app.route('/email/',methods=['GET','POST'])
def email():
    try:
        email=unquote(request.form['email'])
        token=unquote(request.form['token'])
        print(email,token)
        full_resalt=requests.post('https://fsc3301.pythonanywhere.com/email/',data={'email':email,'token':token}).json()['message']

        return render_template(f'./{mainpage}')
    except:
       return E_404()

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
                        log=requests.get('https://fsc3301.pythonanywhere.com/admin/',data={'w':'log','token':token}).json()
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
        return E_404()




@app.route('/flag/',methods=['GET','POST'])
def flag():
    try:
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
            return E_404()
    except:
       return E_404()
chall={
    '1':'./flags/level1/level1.txt',
    '2':'./flags/level2/level2.rar',
    '3':'./flags/level3/Mos.txt',
    '4':'./flags/level4/erdos.txt',
}


@app.route('/challenge/<path:path>/<string:t>',methods=['GET','POST'])
def challenge(path,t):
        global chall
        try:
            path=unquote(path)
            token=unquote(t)

            tokens=requests.post('https://fsc3301.pythonanywhere.com/flag/',data={'token':token}).json()

            level=str(path)

            if tokens['status']=="True" and tokens['message'] != '' and tokens['message'] not in ['AF','AL'] :

                try:
                    return send_file(chall[level], as_attachment=True)
                except KeyError:
                    return {'message':"Challenge Not Found"}
            else:
                return redirect('/')
        except:
            return E_404()


@app.route('/js/<path:path>',methods=['GET','POST'])
def js(path):

    print(path)
    try:
        return render_template(f'{path}')
    except:
        return E_404()








update='True'






up={
    'True':'False',
    'False':'True'
}







@app.errorhandler(404)
def E_404(error):
    return render_template('./404/404.html')


@app.errorhandler(Exception)
def error_handler(error):
    
    
    return error_503,503
    








        
        





def running():
    while True:

        requests.get('https://fsc3301.pythonanywhere.com')
        time.sleep(350)


threading.Thread(target=running).start()



@app.route("/favicon.ico")
def favicon_ico():
     return send_file("./templates/icon/fsc.ico")



@app.before_request
def before_request_func():
        global update
        try:
            print(request.remote_addr)
        except:
            response=make_response(g)
            return response




