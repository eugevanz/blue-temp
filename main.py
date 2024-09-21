from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Title, Div

app = FastHTML(
    hdrs=(
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js'),
        Script(src='https://unpkg.com/hyperscript.org@0.9.12'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css'),
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet',
             href='https://fonts.googleapis.com/css2?family=Playfair+Display+SC:ital,wght@0,700;0,900;1,'
                  '700&display=swap'),
        Title('Blue Chip Invest')
    ), surreal=False, pico=False
)


@app.get("/")
def home():
    return Div(
        Div(
            Div('Item', cls='uk-card uk-card-default uk-card-body')
        ),
        Div(
            Div('Item', cls='uk-card uk-card-default uk-card-body')
        ),
        Div(
            Div('Item', cls='uk-card uk-card-default uk-card-body')
        ),
        data_uk_grid='',
        cls='uk-child-width-expand@s uk-text-center'
    )


serve()
