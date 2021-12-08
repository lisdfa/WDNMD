from ctypes import py_object
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
    page_title="失物招领系统",
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
    ("首页", "失物管理", "用户管理","学生管理","失物论坛")
)
if sidebar == "失物管理":
    st.title("失物管理")
    # 项目选择框
    project_name = st.selectbox(
        "请选择失物",
        ["文具", "首饰", "电子产品", "其他"]
    )
    if project_name:
        # 表单
        with st.form(project_name):
            project_info_1 = st.text_input("丢失地点 形如 （A教 位置1）", "A教 位置1")
            project_info_2 = st.text_input("丢失时间", "Time")
            project_info_3 = st.text_input("形状特征", "Shape")
            project_info_4 = st.text_input("备注信息", "message")
            submitted = st.form_submit_button("提交")
            if submitted:
                with open('lostiformation.vsc.txt', 'a') as f:
                    f.write("\n")
                    f.write(project_info_1)
                    f.write(",")
                    f.write(project_info_2)
                    f.write(",")
                    f.write(project_info_3)
                    f.write(",")
                    f.write(project_info_4)
                # 进度条
                bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    bar.progress(i)
                st.write("丢失地点%s, 丢失时间%s, 丢失特征%s, 备注信息%s," % (
                    project_info_1, project_info_2, project_info_3, project_info_4))
                st.success("提交成功")

elif sidebar == "用户管理":
    st.title("用户管理")
    # 将页面分为左半边和右半边
    left, right = st.beta_columns(2)
    # 左半边页面展示部分
    with left:
        st.header("查看、更新用户信息")
        user_name = st.text_input(
            "请输入您自己个儿的用户名",
            "xxx"
        )
        if user_name:
            with st.form(user_name):
                phone_num = st.text_input("手机号", "+86")
                role = st.multiselect(
                    "用户角色",
                    ["student", "teacher", "administrator"],
                    ["student"]
                )
                user_group = st.multiselect(
                    "请选择用户组",
                    ["vip", "vpp(very poor people)"],
                    ["vip"]
                )
                submitted = st.form_submit_button("提交")
                if submitted:
                    # 这里添加真实的业务逻辑
                    u = "".join(phone_num)
                    s = "".join(role)
                    v = "".join(user_group)
                    k = "".join(user_name)
                    num = 0
                    with open("cheakandupdate.txt", "rt", encoding='utf-8') as f:
                        for i in f:
                            l_line = i.split(",")
                            st.write(l_line)
                            if k == l_line[0]:
                                num == 1
                                l_line[0] = k + ','
                                l_line[1] = u + ','
                                l_line[2] = s + ','
                                l_line[3] = v + '\n'
                                with open("new1.txt", 'a', encoding='utf-8') as wwstream:
                                    wwstream.writelines(l_line)
                            else:
                                with open("new1.txt", 'a', encoding='utf-8') as f:
                                    f.write(l_line[0]+','+l_line[1] +
                                            ','+l_line[2]+','+l_line[3])
                    with open('new1.txt', 'r', encoding='utf-8') as f1:
                        with open('cheakandupdate.txt', 'w', encoding='utf-8') as f2:
                            f2.write(f1.read())
                            st.write("用户名:%s, 手机号:%s, 用户角色:%s, 用户组:%s" %
                                     (user_name, u, s, v))
                    if num == 1:
                        st.success("修改成功！")
                    else:
                        st.error("修改失败，无此用户")
                    with open("new1.txt", 'a+', encoding='utf-8') as test:
                        test.truncate(0)

else:
    st.balloons()
    st.title("欢迎登录失物招领平台")
    st.write("老师客户端")
    st.write("您的失物都在我这儿")

    def laod_data():
        df = pd.read_csv("lostiformation.vsc.txt")
        df = df[['LOST', 'PLACE', 'TIME', 'SHAPE', 'ANYOTHERS']]
        df.columns = ['失物', '丢失地点', '丢失时间', '形状特征', '备注消息']
        return df

    df = laod_data()
    st.table(df.head())

    event_list = df["丢失地点"].unique()

    丢失地点 = st.sidebar.selectbox(
        "你想查看什么地点",
        event_list
    )

    county_list = df["丢失时间"].unique()

    丢失时间 = st.sidebar.selectbox(
        "什么时间段",
        county_list
    )

    part_df = df[(df["丢失地点"] == 丢失地点) & (df['丢失时间'] == 丢失时间)]
    st.write(f"根据你的筛选，数据包含{len(part_df)}行")

    df = pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [30.725526, 103.950056], columns=['lat', 'lon'])
    st.map(df)
