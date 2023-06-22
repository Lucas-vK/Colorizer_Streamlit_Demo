import colorizer_helper as ch
import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)


st.title("Image Colorization Demo")

comparison = "Compare colorized image to original"
examples = "Generate examples"
modes = [comparison, examples]

mode = st.sidebar.radio("", modes, horizontal = False)

if mode == comparison:
    if st.checkbox("Random Image", value = True):
        st.pyplot(ch.compare())
    else:
        st.number_input("Image - ID:", min_value = 0, max_value = ch.get_number_of_images(), key = "image_id")
        st.pyplot(ch.compare(st.session_state.image_id))

elif mode == examples:
    st.pyplot(ch.generate_examples(5, 8))

st.button("Reload")
