import streamlit as st
import time
import numpy as np
import pandas as pd
import os
import hashlib

def md5(pwdStr):
    m = hashlib.md5()
    m.update(pwdStr.encode("utf8"))
    pwdSec = m.hexdigest()
    return pwdStr
# 设置网页标题，以及使用宽屏模式
st.set_page_config(
    page_title="失物招领系统登陆界面",
    layout="wide"

)

# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 左边导航栏
sidebar = st.sidebar.radio(
    "导航栏",
    ("登录","注册")
)
if sidebar == "注册":
    st.title("注册")
    # 项目选择框
    project_name = st.selectbox(
        "请选择注册端口",
        ["teacher", "student", "administrtor"]
    )
    if project_name:
        with st.form(project_name):
            project_user = st.text_input("请输入用户名","xxx")
            project_secreat = st.text_input("请输入密码","xxx")
            project_resuresecreat = st.text_input("请确认密码","xxx")
            submitted = st.form_submit_button("提交")
            if submitted:
                if project_secreat == project_resuresecreat:
                #在这里添加业务逻辑
                    s = ''.join(project_name)
                    with open("zhucebiao.csv", "rt", encoding='utf-8') as f:
                        for i in f:
                            l_line = i.split()
                            id_regist = l_line[0]
                            flag = 1
                            if id_regist == project_user:
                                flag = 0
                                # 进度条
                                bar = st.progress(0)
                                for i in range(100):
                                    time.sleep(0.01)
                                bar.progress(i)
                                st.write("请输入用户名:%s, 请输入密码:%s, 请确认密码:%s" %(project_user, project_secreat, project_resuresecreat))
                                st.success("已被注册！错误！")
                        if flag == 1:
                            with open("zhucebiao.csv", "a") as f:
                                pwdSec = md5(project_secreat)
                                f.write("\n"+project_user+","+pwdSec+","+s)
                                bar = st.progress(0)
                                for i in range(100):
                                    time.sleep(0.01)
                                bar.progress(i)
                                st.write("请输入用户名:%s, 请输入密码:%s, 请确认密码:%s" %(project_user, project_secreat, project_resuresecreat))
                                st.success("已注册成功，去登录吧！")
                else:
                    bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                    bar.progress(i)
                    st.write("正在把%s的密码%s 和确认密码%s 一个个抠出来检查" %
                    (project_user, project_secreat, project_resuresecreat))
                    st.success("确认密码与原密码不符合！你看看你的确认密码对不对lan你")



elif sidebar == "登录":
    st.balloons()
    st.title("您的失物正在来的路上")
    st.write("在此之前，请先登录")
    # 项目选择框
    project_loadname = st.selectbox(
        "请选择登录端口",
        ["techer", "student", "administrtor"]
    )
    count = 0
    if project_loadname:
        with st.form(project_loadname):
            project_user1 = st.text_input("请输入用户名", "xxx")
            project_secreat1 = st.text_input("请输入密码", "xxx")
            submitted = st.form_submit_button("提交")
            if submitted:
                    flag = 0
                    with open("zhucebiao.csv", "rt",encoding='utf-8') as f:
                        for i in f:
                            l_line = i.split(",")
                            if l_line[0] == project_user1:
                                flag = 1
                                pwdSec = md5(project_secreat1)
                                if pwdSec == l_line[1]:
                                    s = "".join(project_loadname)
                                    if s == l_line[2]:
                                        if s == "teacher":
                                            bar = st.progress(0)
                                            for i in range(100):
                                                time.sleep(0.01)
                                                bar.progress(i)
                                            st.write("李炸天正在确认用户名:%s, 曾三金正在偷偷换密码:%s, " % (project_user1, project_secreat1))
                                            st.success("成功登录teacher端")
                                            os.system("streamlit run ")
                                        if s == "student":
                                            bar = st.progress(0)
                                            for i in range(100):
                                                time.sleep(0.01)
                                                bar.progress(i)
                                            st.write("李炸天正在确认用户名:%s, 曾三金正在偷偷换密码:%s, " % (project_user1, project_secreat1))
                                            st.success("成功登录student端")
                                            os.system("streamlit run insidestudent.py")
                                        if s == "administrtor":
                                            bar = st.progress(0)
                                            for i in range(100):
                                                time.sleep(0.01)
                                                bar.progress(i)
                                            st.write("李炸天正在确认用户名:%s, 曾三金正在偷偷换密码:%s, " % (project_user1, project_secreat1))
                                            st.success("成功登录administrtor端")
                                            os.system("streamlit run insideadministrtor.py")
                                    else:
                                        bar = st.progress(0)
                                        for i in range(100):
                                            time.sleep(0.01)
                                            bar.progress(i)
                                        st.write("李炸天正在确认用户名:%s, 曾三金正在偷偷换密码:%s, " % (project_user1, project_secreat1))
                                        st.success("您未拥有%s端口" % s)
                                else:
                                    st.success("李康成说你的密码错误了")
                        if flag == 0:
                            bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.01)
                                bar.progress(i)
                            st.write("李炸天正在确认用户名:%s, 曾三金正在偷偷换密码:%s, " % (project_user1, project_secreat1))
                            st.success("没有找到你英俊的名字，要不点开左边小箭头注册一个？")
