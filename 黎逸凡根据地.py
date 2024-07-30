'''我的主页'''
import streamlit as st
from PIL import Image
import time
import datetime

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区' , '写作推荐'])
"""
工作室名字：……
根据地用户：个人使用、只有几个人知道的秘密基地、分享后所有人可见……
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感：……
原创模块：……
原创模块一句话功能介绍：……
"""
def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3','rb' ) as f:
        mymp3 = f.read( )
    st.audio(mymp3,format='audio/mp3',start_time=0) 
    st.image('slogan.png')
    st.write("以下是一些适合您的阅读推荐：")
    st.write("1. 《百年孤独》 - 加西亚·马尔克斯")
    st.write("2. 《平凡的世界》 - 路遥")
    st.write("3. 《人类简史》 - 尤瓦尔·赫拉利")
    st.write("推荐的音乐风格和歌手：")
    st.write("1. 流行音乐：周杰伦、Taylor Swift")
    st.write("2. 古典音乐：贝多芬、莫扎特")
    st.write("适合您的运动项目和相关资源：")
    st.write("1. 跑步：专业跑鞋推荐")
    st.write("2. 瑜伽：线上瑜伽课程")
    pass 

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传照片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        try:
            img = Image. open(uploaded_file)
            st. image(img)
            st. image(img_change(img, 0,1,2))
            tab1, tab2, tab3, tab4 = st. tabs(["原图", "改色1","改色2","改色3"])
            with tab1:
                st. image(img)
            with tab2:
                st. image(img_change(img, 2 ,1, 0))
            with tab3:
                st.write('### :red[这是一张102的rgb]')
                st. image(img_change(img, 2,0,1))
            with tab4:
                st. image(img_change(img, 1,1,0))
                st.write('### :red[这是一张012的rgb]')
        except FileNotFoundError as fnfe:  
            st.error(f"文件未找到错误: {fnfe}")
        except IOError as ioe:
            st.error(f"输入输出错误: {ioe}")
        except Exception as e:  
            st.error(f"发生未知错误: {e.__class__.__name__}: {e}")


def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list =f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

                            
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            '''字典键值对遍历'''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + 'n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        
        st.write(f'#####：blue［{words_dict[word][1]}]')
    else:
        st.write(f"{word} 未在词典中")
        new_word = st.text_input("请输入要添加的单词")
        new_definition = st.text_input("请输入释义")
        if st.button("添加"):
            words_dict[new_word] = new_definition
            st.markdown("<h1 style='color: green;'>恭喜添加成功！</h1>", unsafe_allow_html=True)
            st.write(f"已成功添加 {new_word} 及其释义")
    if word == 'python' :
        st.code('''
            # 恭喜你触发彩蛋，这是一行python代码
            print('hello world')''')
    elif word == 'balloon':
        st.balloons ()
    elif word == 'snow':
        st.snow()
    


def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list =f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    st.text("主人留言")
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('💯'):
                st.text(i[1]+':'+i[2])
    st.text("客人留言")
    for i in messages_list:
        if i[1] == '编程猫':
            with st.chat_message('🔢'):
                st.text(i[1]+':'+i[2])
    '''新增留言内容'''
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name, new_message])
        with open('leave messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] +'\n'
            message =message[:-1]
            f.write(message)

def page_5():
    '''写作推荐'''
    pass

def img_change(img,rc,gc,bc) :
    '''图片处理'''
    width, height = img. size
    img_array = img. load()
    for x in range(width) :
        for y in range (height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x,y] = (r, g, b)
    return img
    
            

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '写作推荐':
    page_5()
