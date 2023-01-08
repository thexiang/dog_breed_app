import streamlit as st
import utils

st.set_page_config(
    page_title="Dog Breeds",
    page_icon="🐕",
)

utils.inject_css()

st.image("./images/miya.png")
st.write("# Dog Breed ! ")


st.markdown(
    """
     ## Data Sets

    - Dog Breeds Dataset Enrichments [link](https://data.world/nicolemark/dog-breeds-dataset-enrichments/workspace/file?filename=dog+breeds_enriched_20210503.csv)
    """
)