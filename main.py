import streamlit as st

st.set_page_config(page_title='streamlit 실습', page_icon='💻',layout='wide')

st.sidebar.title('📆강의 일정')
st.sidebar.caption('날씨를 클릭하면 그날의 실습/과제 화면으로 이동합니다.')

selected_day=st.sidebar.radio('날짜를 선택하세요.', ['1일차: 7월 6일(월)', '2일차: 7월 7일(화)', '3일차: 7월 8일(수)', '4일차: 7월 9일(목)', '5일차: 7월 10일(금)'])

st.title(selected_day)
st.divider()

tab_practice, tab_assignmemt1, tab_assignment2=st.tabs(['실습', '과제1', '과제2'])

if selected_day=='1일차: 7월 6일(월)':
    with tab_practice:
        st.header('1일차 실습예제')

    with tab_assignmemt1:
        st.header('1일차 실습과제1')
    
    with tab_assignment2:
        st.header('1일차 실습과제2')

elif selected_day=='2일차: 7월 7일(화)':
    with tab_practice:
        st.header('2일차 실습예제')

    with tab_assignmemt1:
        st.header('2일차 실습과제1')
    
    with tab_assignment2:
        st.header('2일차 실습과제2')

elif selected_day=='3일차: 7월 8일(수)':
    with tab_practice:
        st.header('3일차 실습예제')

    with tab_assignmemt1:
        st.header('3일차 실습과제1')
    
    with tab_assignment2:
        st.header('3일차 실습과제2')    
    
elif selected_day=='4일차: 7월 9일(목)':
    with tab_practice:
        st.header('4일차 실습예제')

    with tab_assignmemt1:
        st.header('4일차 실습과제1')

elif selected_day=='5일차: 7월 10일(금)':
    with tab_practice:
        st.header('5일차 실습예제')

    with tab_assignmemt1:
        st.header('5일차 실습과제1')
    
    with tab_assignment2:
        st.header('5일차 실습과제2')