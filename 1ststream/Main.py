import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('ブレグレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('DataFrame')

df = pd.DataFrame({
    '1列目' : [1,2,3,4], 
    '2列目' : [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0), width=300,height=300) #dataframeでは大きさを指定できる

st.table(df.style.highlight_max(axis=0)) #静的なデータを作りたいときはtable

#マークダウン
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df) #折れ線グラフ

st.area_chart(df)

st.bar_chart(df)

#新宿の緯度経度
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

#マップ表示
st.map(df)

st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください', 
    list(range(1,11))
)

'あなたの好きな数字は',option,'です'

if st.checkbox('Show Image'):
    img = Image.open('dog.jpg')
    st.image(img,caption='dog',use_column_width=True)

st.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味:',text

condition=st.sidebar.slider('あなたの今の調子は?',0,100,50)
'コンディション',condition

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expan=st.expander('問い合わせ')
expan.write('問い合わせ内容を書く')