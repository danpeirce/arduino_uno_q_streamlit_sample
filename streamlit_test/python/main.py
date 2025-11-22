from arduino.app_bricks.streamlit_ui import st
from arduino.app_utils import *

st.header("Streamlit Example")
image = st.radio(
    "Radio Button Options",
    ["clear", "gradation", "logo"],
    captions = [
        "Clear LED Display",
        "Show LED Gradient",
        "Show Arduino Loco"
    ]
)

if image == "clear":
    Bridge.call("clear_led")
    st.write("All LEDs Off")
elif image == "gradation":
    Bridge.call("show_gradation")
    st.write("Gradient Displayed")
elif image == "logo":
    Bridge.call("show_logo")
    st.write("LED Logo Displayed")