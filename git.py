# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# # pip install -r : 라이브러리 일괄 설치


# st.title("🧮국세청 근로소득 데이터 분석")
# # 데이터 불러오기

# file_path = "./data/근로소득.csv" # 불러올 데이터 지정

# # 경로 찾기 - ./폴더명/
# # path = "a.jpg"
# # path = "../images/a.jpg"

# try :
#     # 자료 읽기
#     df = pd.read_csv(file_path) # df라는 곳에 보낸다
#     st.success("데이터 로딩을 성공했습니다.")

#     #데이터 미리 보기
#     st.subheader("데이터 확인하기")
#     st.dataframe(df.head()) # 표 상단 5줄 보여주기

#     # 데이터 분석 그래프 그리기
#     st.subheader("📈📉항목별 분포 그래프")

#     # 분석하고 싶은 열 이름 선택
#     # 급여나 인원 같은 숫자 데이터가 있는 칸을 골라야 한다.
#     column_names = df.columns.tolist()
#     selected_col = st.selectbox("분석할 항목을 선택하세요 : ", column_names)

#     # 그래프 그리기(seaborn 사용)
#     if selected_col:
#         # 1. fig, ax (콤마) / 2. figsize (오타 수정)
#         fig, ax = plt.subplots(figsize=(10, 5)) 
        
#         sns.histplot(df[selected_col], ax=ax, color="#9932CC")
        
#         ax.set_title(f"[{selected_col}] 분포 확인") 
#         ax.set_xlabel(selected_col) 
#         ax.set_ylabel("빈도수") 
        
#         # 3. pit -> plt 오타 수정 (혹은 위처럼 ax를 써도 됩니다)
#         # plt.xlabel(selected_col) 
        
#         # 4. 함수 호출 형태로 수정
#         st.pyplot(fig) 
#     # --- [수정된 부분 끝] ---




# except FileNotFoundError :
#     st.error(f"'{file_path}'파일을 찾을 수 없습니다, 파일명이 정확한지 확인해주세요.")
# except Exception as e:
#     st.error(f"에러가 발생했습니다: {e}")


# # st.title("2026년 1월 16일")
# # st.header("2014년 1월 16일")
# # st.subheader("12주년")
# # st.text("지하1층")

# # st.title("Weather : 💠")
# # st.markdown("this is markdown **bold**")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글 폰트 깨짐 방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

st.title("🧮국세청 근로소득 데이터 분석")

file_path = "./data/근로소득.csv"

try:
    # [수정 포인트 1] encoding='cp949' 추가
    # 한글 엑셀파일(CSV)을 읽을 때는 이 옵션이 거의 필수입니다.
    df = pd.read_csv(file_path, encoding='cp949') 
    
    st.success("데이터 로딩을 성공했습니다.")

    st.subheader("데이터 확인하기")
    st.dataframe(df.head())

    st.subheader("📈📉항목별 분포 그래프")

    # 숫자 데이터만 골라내기 (그래프 그릴 때 오류 방지)
    # numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    column_names = df.columns.tolist()
    
    selected_col = st.selectbox("분석할 항목을 선택하세요 : ", column_names)

    if selected_col:
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # 데이터가 숫자인지 확인하고 그리기 (안전장치)
        try:
            sns.histplot(df[selected_col], ax=ax, color="#9932CC")
            ax.set_title(f"[{selected_col}] 분포 확인")
            ax.set_xlabel(selected_col)
            ax.set_ylabel("빈도수")
            st.pyplot(fig)
        except ValueError:
            st.warning("이 항목은 히스토그램으로 그릴 수 없는 데이터(문자 등)입니다.")

except FileNotFoundError:
    st.error(f"'{file_path}'파일을 찾을 수 없습니다. data 폴더 안에 파일이 있는지 확인해주세요.")
    
except Exception as e:
    # [수정 포인트 2] 에러의 정체를 화면에 출력
    st.error(f"에러가 발생했습니다: {e}")
