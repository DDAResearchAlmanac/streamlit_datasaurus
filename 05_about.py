import streamlit as st

def display_page():
    # Set title
    st.title("About")

    # Columns
    c1, c2  = st.columns([2,8])

    # Image
    image_markdown_format = "![Alt Text](https://github.com/sebastiandres/streamlit_datasaurus/blob/main/images/{}?raw=true)"
    c1.markdown(image_markdown_format.format("mrdna.png"))

    # Authors
    c2.header("The authors")
    c2.markdown("""
    * Diego Rojo:\t\t[website](https://www.93degree.me/) - [github](https://github.com/93degree) - [linkedin](https://www.linkedin.com/in/diego-rojo/) - [twitter](https://twitter.com/Diego_Rojo_)
    * Sebastián Flores:\t\t[website](https://sebastiandres.github.io/blog/) - [github](https://github.com/sebastiandres) - [linkedin](https://www.linkedin.com/in/sebastiandres/) - [twitter](https://twitter.com/sebastiandres)""")

    # Anscombe
    c2.header("The Anscombe Dataset")
    c2.markdown("""
    * [Original publication by Francis Anscombe on 1973](https://www.tandfonline.com/doi/abs/10.1080/00031305.1973.10478966)
    * [Wikipedia's entry on Anscombe's Quarter](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)
    """)    


    # Datasaurius
    c2.header("The Datasaurus")
    c2.markdown("""
    * [The tweet that originated the madness](https://twitter.com/albertocairo/status/765167969139765250) by Alberto Cairo.
    * [Same Stats, Different Graphs - also known as the Datasaurus paper](https://www.autodesk.com/research/publications/same-stats-different-graphs) by Justin Matejka and George Fitzmaurice.
    * [Python implementation of Same Stats, Different Graphs](https://github.com/jmatejka/same-stats-different-graphs) by jmatejka.
    """)

    # Other links and references
    c2.header("Links and references")
    c2.markdown("""
    * All characters from Jurassic Park's franchise have been used in good faith with no comercial intention.
    * The gifs: made with [youtube](https://www.youtube.com/watch?v=h58lRIVHhGc) and [gifrun](https://gifrun.com/).
    * [Dinosaur Supervisor Phil Tippett](https://github.com/sebastiandres/streamlit_datasaurus/blob/main/images/phil.jpg?raw=true). You had one job, Phil one job.
    """)
