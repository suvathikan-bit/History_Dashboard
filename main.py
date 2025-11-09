import streamlit as st
import requests

st.write("suvathikan dashboard")
st.title("Era history")
st.subheader("Welcome! our era history")
st.markdown('''
    :red[Those] :orange[who] :green[do] :blue[not] :violet[remember]
    :gray[are] :rainbow[the] :blue-background[past] :red[condemned] :orange[to] :green[repeat] :blue[it]''')
option = st.sidebar.selectbox(
    "What is the era you want to know about ? ",
    ("Prehistory", "Classic Era", "Middle Age","Early Modern era","Modern Era","Future"),
)

##st.write("You selected the era:", option)
def prehistory():
    prehistory_resp = requests.get('https://maddie11.pythonanywhere.com/api/era/prehistory')
    pre = prehistory_resp.json()
    st.subheader(":green[demographics]")
    st.badge("average life expectancy",  color="blue")
    st.markdown(pre["demographics"]["average_life_expectancy"])
    st.badge("child mortality rate",  color="blue")
    st.markdown(pre["demographics"][ "child_mortality_rate"])
    st.badge("gender ratio",  color="blue")
    st.markdown(pre["demographics"]["gender_ratio"])
    
    st.subheader(":green[dominant species]")
    st.badge("dominant species",  color="blue")
    dominant_species=['Homo habilis', 'Neanderthals', 'Woolly Mammoths']
    st.write()
    for item in dominant_species:
        st.write(item)   
    
    st.subheader(":green[fun fact]")
    st.badge("fun fact",  color="blue")
    st.markdown(pre["fun_fact"])
    
    keyevents={'event': 'First stone tools used', 'year': -2500000}
    st.subheader(":green[key events]")
    st.badge("key events 01",  color="blue")
    st.write()
    st.write("event:",keyevents["event"])
    st.write()
    st.write("year:",keyevents["year"])

    st.subheader(":green[map regions]")
    st.badge("map regions",  color="blue")
    map={'Africa', 'Eurasia', 'Ice Age landscapes'}
    st.write()
    for item in map:
        st.write(item)
    
    st.subheader(":green[population estimate]")
    st.badge("population estimate",  color="blue")
    st.markdown(pre[ "population_estimate"])
    
    st.subheader(":green[year range]")
    st.badge("year range",  color="blue")
    st.markdown(pre["year_range"])


if option == "Prehistory":
    st.image("https://humanidades.com/wp-content/uploads/2017/05/prehistoria-5-e1567907866390.jpg")
    prehistory()
    video_file = open("myvideo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    
  

elif option == "Classic Era":
    st.image("https://images.saymedia-content.com/.image/t_share/MTg4NzM3NDAxNTYzMzI2MTk2/classical-era-in-music-the-age-of-enlightenment.jpg")
    #video_file = open("classicera.mp4", "rb")
    #video_bytes = video_file.read()
    #st.video(video_bytes)
    st.video("https://youtu.be/vfT4xyKQOzY?si=WeofFXM5Xp16rP9P")

elif option == "Early Modern era":
    st.image("https://www.open.edu/openlearn/pluginfile.php/1115923/tool_ocwmanage/image/0/a223_1_OLHP_786x400.jpg")
    #video_file = open("earlymodern.mp4", "rb")
    #video_bytes = video_file.read()
    #t.video(video_bytes)
    st.video("https://youtu.be/yIGBjoXfaVw?si=h1ONajYzhmxV7q_C")

elif option == "Future":
    st.image("https://blog.en.erste-am.com/wp-content/uploads/2018/01/Szenario-Stadt-und-Energie-cSiemens-Pictures-of-the-Future-scaled-3.jpg")
    video_file = open("future.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    
elif option == "Middle Age":
    st.image("https://www.paragkhanna.com/wp-content/uploads/2020/07/joan-of-arc-leads-french-army-against-english-defenders-of-les-tourelles-gate-in-siege-of-orleans-may-7-1429-from-19th-century-chromolithograph.jpg")
    #video_file = open("middle.mp4", "rb")
    #video_bytes = video_file.read()
    #st.video(video_bytes)
    st.video("https://youtu.be/tRo4SeA-wbo?si=UpMPF0ETuPl4f0NE")
else :
    st.image("https://study.com/cimages/multimages/16/800px-la_scuola_di_atene175394020409963521.jpg")
    #video_file = open("else.mp4", "rb")
    #video_bytes = video_file.read()
    #st.video(video_bytes)
    st.video("https://youtu.be/fJ6eu2GSS7o?si=CpP5BNUCg5EDn4ox")
st.logo(
    "logo.png"
)

