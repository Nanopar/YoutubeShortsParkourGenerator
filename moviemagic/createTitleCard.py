from moviepy import ImageClip, TextClip, CompositeVideoClip

def createCard(title):
    template = ImageClip("titleCardTemplate.png")
    text = TextClip(
            text=title, 
            font_size=37, 
            color='white', 
            font="ARIAL.TTF",
            method="caption",  # Enables word wrapping
            size=(546, 110)
        )
    text = text.with_position((67, 580)).with_duration(5)
    final = CompositeVideoClip([template, text])
    final.save_frame("outputs/titleCard.png", t=0)