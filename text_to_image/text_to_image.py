import base64
import time
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as component
from  PIL import Image
import numpy as np
import cv2
import spacy_streamlit as ss
from extra import js_1,js,js_for_img


pat = 'C:\\Users\\imran ullah\\OneDrive\\Desktop\\ayan-main\\sun flower.jpg'
pat = Image.open(pat)






choose = option_menu('Text to image ', ["Demo", "Example", "Warning!!!"],
                         icons=['arrow-down-right-circle', 'display-fill', 'exclamation-triangle'],
                         menu_icon="cast", default_index=0,
                         orientation='horizontal',
                         styles={       
        "container": {"padding": "5!important", "background-color": "#fa34xx"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#867"},
        "nav-link-selected": {"background-color": "#02tt21"},}
    )
if choose=='Demo':
    component.html(f"""
         <html>

         <link rel="stylesheet" type="text/css" href="C:\\Users\\imran ullah\\OneDrive\\Desktop\\ayan-main\\css1.css" crossorigin="anonymous">
         <script > {js}</script>
         <body>
           <h1>
             <a href="" class="typewrite" data-period="2000" data-type='[ "Hi, Im Si.", "I am Creative.", "I Love Design.", "I Love to Develop." ]'>
               <span class="wrap"></span>
             </a>
           </h1>
         </body>
         <html>
         """,height=100,width=700)
    promote = st.text_input(label="what's on Your Mind? ")
    my_bar = st.progress(0)
    for p_complt in range(100):
          time.sleep(0.1)
          my_bar.progress(p_complt + 1)
      
          
        


elif choose == 'Warning!!!':
    component.html(f"""
         <html>

         <link rel="stylesheet" type="text/css" href="C:\\Users\\imran ullah\\OneDrive\\Desktop\\ayan-main\\css1.css" crossorigin="anonymous">
         <script > {js}</script>
         <body>
           <h1>
             <a href="" class="typewrite" data-period="2000" data-type='[ "please be sure dont use this app for bad purpose please be sure dont use this app for bad purpose.please be sure dont use this app for bad purpose please be sure dont use this app for bad purpose.please be sure dont use this app for bad purpose please be sure dont use this app for bad purpose.", "dont use this app", "for bad purpose.", "I Love to Develop." ]'>
               <span class="wrap"></span>
             </a>
           </h1>
         </body>
         <html>
         """,height=700,width=700)
    

elif choose=='Example':
    c1,c3 = st.columns([0.5,0.5])
    with c1:
        st.image(pat,width=350,caption='sun flower ',output_format="auto")
    with c3:
        st.image(pat,width=350,caption='sun flowersun flower sun flower\nsun flowersun flower ',output_format="auto")


    