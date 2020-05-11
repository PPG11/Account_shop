from flask import Blueprint, redirect, url_for, request, render_template, flash
import db

user_info = Blueprint('user_info', __name__, url_prefix='/user_info')


@user_info.route('/<username>')
def show_user(username):
    sql = "select * from " + username
    details = db.query_data(sql)
    # print(details)
    return render_template('show_user_info_v2.html', username=username, datas=details)


@user_info.route('/add_new/<username>', methods=['POST'])
def add_new(username):
    print('hahaha')
    content = request.form.get('content')
    tag = get_tag(content)
    sql = f'''
        insert into {username} (tag, info)
        value ('{tag}', '{content}')
    '''
    db.insert_or_updata_data(sql)
    flash(u'添加成功')
    return redirect(url_for('user_info.show_user', username=username))


@user_info.route('/add_info/<username>')
def add_info(username):
    return render_template('add_info.html', username=username)


# @user_info.route('/delete_info', method=['GET'])
@user_info.route('/delete_info', methods=['POST'])
def delete_info():
    username = request.form.get('username')
    tag = request.form.get('tag')
    sql = f'''DELETE FROM {username} WHERE tag = "{tag}"'''
    # print(sql)
    db.insert_or_updata_data(sql)
    flash(u'删除成功')
    return {'res': 'success'}


# function used in this package
def get_tag(content):
    """
    get the tag from the content
    :param content: string
    :return: tag
    """
    import re
    pattern = re.compile(r'[A-Z0-9]+')
    # content = content.scrip()
    m = pattern.match(content)
    tag = m[0]
    return tag
