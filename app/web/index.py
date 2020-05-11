from flask import Blueprint, redirect, url_for, request, render_template, session, flash
import db
from verify_code import generate_captcha_image_url

index = Blueprint('index', __name__, template_folder='../../templates')


@index.route('/test')
def test():
    # return render_template('show_user_info_v2.html', Title=title)
    return render_template('test.html')


@index.route('/connect_us')
def connect_us():
    # return render_template('connect_us.html')
    return render_template('love.html')


# return verify code
@index.route('/captcha/')
def graph_captcha():
    resp, captcha_text = generate_captcha_image_url()
    session['verify'] = captcha_text
    return resp


@index.route('/')
def first():
    return render_template('login_v2.html')


@index.route('/login')
def login():
    return render_template('login_v2.html')


@index.route('/user_login', methods=['POST'])
def user_login():
    verify_text = request.form.get('verify_text')
    captcha_text = session['verify']
    if verify_text.lower() != captcha_text.lower():
        print(verify_text.lower())
        print(captcha_text.lower())
        flash(u'验证码错误')
        return login()
        # return redirect(url_for('/'))

    # print(request.form)
    name = request.form.get('name')
    password = request.form.get('password')
    sql = f"""
    select * from user where ( account='{name}' or email='{name}' ) and password='{password}'
    """
    # print(sql)
    res = db.query_data(sql)
    # print(res)
    if not res:
        flash(u'账号或密码错误')
        return login()
    details = res[0]
    return redirect(url_for('user_info.show_user', username=details['account']))


@index.route('/register')
def register(is_wrong_verify_code=False):
    # flash(u'验证码错误')
    return render_template('register_v2.html', is_wrong_verify_code=is_wrong_verify_code)


@index.route('/CheckCodeServlet', methods=['POST'])
def check_code_servlet():
    key_value = request.get_data("keyValue")
    # key_value = request.__getattribute__("keyValue")
    print(key_value)


@index.route('/do_register_user', methods=['POST'])
def do_register_user():
    verify_text = request.form.get('verify_text')
    captcha_text = session['verify']
    if verify_text.lower() != captcha_text.lower():
        flash(u'验证码错误')
        return register()

    # print(request.form)
    account = request.form.get('account')
    password = request.form.get('password')
    email = request.form.get('email')

    # check the account is available
    sql = f"""
    select * from user where account='{account}'
    """
    res = db.query_data(sql)
    if res:
        flash(u'账号已存在')
        return register()

    # check the email is available
    sql = f"""
    select * from user where email='{email}'
    """
    res = db.query_data(sql)
    if res:
        flash(u'邮箱已存在')
        return register()

    # else insert in to database
    sql = f'''
        insert into user (account, password, email)
        value ('{account}', '{password}', '{email}')
    '''
    # print(sql)
    db.insert_or_updata_data(sql)
    db.new_database(account)
    return render_template('login_v2.html')
