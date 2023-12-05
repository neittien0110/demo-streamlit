#-------------------------------------------------------------------------
# Dữ liệu sử dụng trong file my_data.csv
#      DateTime, Value
#      01/11/2023; 6
#      02/11/2023; 7
#      03/11/2023; 1
#      04/11/2023; 8
#      05/11/2023; 5
#      07/11/2023; 3
#      08/11/2023; 8
#      09/11/2023; 9
#      10/11/2023; 1
#      11/11/2023; 13
#-----------------------------------------------------------------------
import streamlit as st
import pandas as pd

st.write("Chao cac ban")

df = pd.read_csv("my_data.csv",
                 sep=";", 
                 header=None,#=None Có khai báo header ở tham số names tiếp theo. Ví dụ names=['DateTime', 'Value']
                             #=0, tên cột nằm ở dòng đầu tiên của file csv. Có thể thay bằng 2, 3, 4, etc.
                 names=['DateTime', 'Value']  #Đặt tên cho các cột dữ liệu, độ ưu tiên cao hơn so với thông số header=0
                 )
# Tên cột dữ liệu đầu tiên
print (df.columns[0])

# Vẽ đồ thị trên web
st.line_chart(df, x='DateTime', y='Value', color=None, width=1000, height=500, use_container_width=True)
