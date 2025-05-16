from fasthtml.common import *
import random
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;} body{   text-align: center; background-url(https://media.tenor.com/LH6VcfpgfaAAAAAM/warp-space.gif); background:fill;}')

app = FastHTML(hdrs=(picolink, css))


@app.route("/", methods=['get'])
def home():
    return H1('Hello, World')

@app.route("/", methods=['post', 'put'])
def post_or_put():
    return "got a POST or PUT request"


@app.get("/")
def home():
    return Title("Clone Chooser"), Main(
        H1("what clone are you?"),

        Button("click me!", hx_post="/choose", hx_target=".clone", hx_swap="innerHTML"),
        Div(cls='clone')
    )





@app.post("/choose")
def choose():
    rnd = random.randint(1, 10)
    character_text = ""
    image_text = ""
    match rnd:
        case 1:
            character_text = "you are Captain Rex!"
            image_text = "https://werewolves.world/pics/1.gif"
        case 2:
            character_text = "you are ARC Trooper Fives!"
            image_text = "https://werewolves.world/pics/2.gif"
        case 3:
            character_text = "you are ARC Trooper Echo!"
            image_text = "https://werewolves.world/pics/3.gif"
        case 4:
            character_text = "you are Commander Cody!"
            image_text = "https://werewolves.world/pics/4.gif"
        case 5:
            character_text = "you are ARC Trooper Jesse!"
            image_text = "https://werewolves.world/pics/5.gif"
        case 6:
            character_text = "you are Trooper Hardcase!"
            image_text = "https://werewolves.world/pics/6.gif"
        case 7:
            character_text = "you are Trooper Hevy!"
            image_text = "https://werewolves.world/pics/7.gif"
        case 8:
            character_text = "you are Medic Kix!"
            image_text = "https://werewolves.world/pics/8.gif"
        case 9:
            character_text = "you are Trooper Waxer!"
            image_text = "https://werewolves.world/pics/9.gif"
        case 10:
            character_text = "you are Trooper Boil!"
            image_text = "https://werewolves.world/pics/10.gif"

    return(
        P(character_text), Br(), Img(src=image_text)

    )



serve()