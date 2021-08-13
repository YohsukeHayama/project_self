#%%
import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title('streamlitサンプル')

st.write('DataFrame')

#%%
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a", "c", "s"]
)


if st.checkbox('画像表示'):

    img = Image.open('calll.jpg')
    st.image(img, caption="temp", use_column_width=True)


option = st.selectbox(
	'あなたが好きな数字',
	list(range(1,11))
)
st.write(option)

expander =  st.beta_expander('問い合わせ')
expander.write('内容')

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

# st.table(df.style.highlight_max(axis=0))
# st.area_chart(df)
# st.bar_chart(df)

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
# # %%


# df2 = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df2)
# %%
