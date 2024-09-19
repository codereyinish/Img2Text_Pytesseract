# magic command from jupyter notebook, writes whatever content insdie the cell to the .py file
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io #pyhton built-in module to deal with input/output Memory Streams
import time
from image_processing import getTextFromImage
html_temp = """
            <div style="background-color:{};padding:1px">

            </div>
            """

textContent = None
#SIDEBAR

with st.sidebar:
  st.title(":smile: Text from Image")
  st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
  st.markdown("""
    # How does it work?
    Simply upload your images and get the extracted the Text content.
    """)
  st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
# #CAMERA UPLOAD --LATER
# img_file_buffer = st.camera_input("Take a picture")
# #opening Image file for Image Processing tasks via OpenCV
# if img_file_buffer is not None:
#   bytes_data = img_file_buffer.getvalue()
#   cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8),cv2.IMREAD_COLOR)
#   #check image type
#   st.write(type(cv2_img))

# FILE_UPLOAD
st.title("📷 Image Upload and Processing")
img_file = st.file_uploader("Upload Image file", accept_multiple_files=False)
print(img_file)

cv2_img = None
if img_file is not None:
    file_details = {"fileName": img_file.name, "FileType": img_file.type, "FileSize": f"{img_file.size/1024:.2f} KB"}
    try:
        if img_file.type == "image/heic":
            from pillow_heif import register_heif_opener
            register_heif_opener()
            image = Image.open(img_file)
            image = image.convert('RGB')
            buf = io.BytesIO()
            image.save(buf, format='JPEG')
            jpeg_bytes = buf.getvalue()
        else:
            jpeg_bytes = img_file.read()

        cv2_img = cv2.imdecode(np.frombuffer(jpeg_bytes, np.uint8), cv2.IMREAD_COLOR) #cv2_img is in np array format
        # st.write(type(cv2_img))
        # st.image(cv2_img, channels="BGR", caption="Uploaded Image")
        # st.write("Image shape: ", cv2_img.shape)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("Please upload an image file")



st.markdown("""
<style>
.big-gap {
    margin-bottom: 2em;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-gap"></p>', unsafe_allow_html=True)


#OUTPUTS::
# Custom CSS for the blinking effect
st.markdown("""
<style>
@keyframes blink {
    0% { opacity: 0; }
    50% { opacity: 1; }
    100% { opacity: 0; }
}
.blinking {
    animation: blink 1.5s linear infinite;
}
</style>
""", unsafe_allow_html=True)

# Function to create a blinking loading message
def blinking_loading_message(message):
    return f'<p class="blinking">{message}</p>'

if cv2_img is not None:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Image Column")
        image_placeholder = st.empty()
        loading_message = st.empty()
        loading_message.text("Loading image...")
        time.sleep(1)  # Reduced sleep time
        image_placeholder.image(cv2_img)
        loading_message.empty()

    try:
        textContent = getTextFromImage(cv2_img)
    except Exception as e:
        st.error(f"An error occurred while extracting text: {str(e)}")
else:
    st.info("Please upload an image to see the content")

# Column 2: Text content with blinking loading sign
if textContent is not None:
  with col2:
    st.subheader("Text Content Column")

    # Placeholder for text content
    text_placeholder = st.empty()

    # Blinking loading message
    loading_message = st.markdown(blinking_loading_message("Loading text content..."), unsafe_allow_html=True)

    # # Simulate text content loading
    # time.sleep(3)  # Simulate longer delay for text content

    text_placeholder.text(textContent)
    st.write(len(textContent))
    loading_message.empty()





