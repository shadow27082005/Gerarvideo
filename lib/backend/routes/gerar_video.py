from flask import Blueprint, jsonify
from gtts import gTTS
from moviepy.editor import *
import os

video_bp = Blueprint('video_bp', __name__)

@video_bp.route('/gerar-video', methods=['GET'])
def gerar_video():
    try:
        # CONFIGURAÇÕES
        NOME_AUDIO = "narracao.mp3"
        NOME_VIDEO = "video_final.mp4"
        COR_FUNDO = (0, 48, 73)  # azul escuro
        DURACAO = 15
        RESOLUCAO = (1080, 1920)

        with open("entrada.txt", "r", encoding="utf-8") as f:
            texto = f.read()

        tts = gTTS(text=texto, lang='pt-br')
        tts.save(NOME_AUDIO)

        fundo = ColorClip(size=RESOLUCAO, color=COR_FUNDO, duration=DURACAO)

        txt = TextClip("AurusDesk", fontsize=90, color='white', font="Arial-Bold")
        txt = txt.set_position(("center", 600)).set_duration(DURACAO)

        cta = TextClip("Teste grátis • aurustech.com.br", fontsize=50, color='white', font="Arial-Bold")
        cta = cta.set_position(("center", 900)).set_duration(DURACAO)

        clips = [fundo, txt, cta]
        if os.path.exists("logo.png"):
            logo = ImageClip("logo.png").set_duration(DURACAO).resize(height=150).set_position(("center", 100))
            clips.insert(1, logo)

        audio = AudioFileClip(NOME_AUDIO)
        video = CompositeVideoClip(clips).set_audio(audio)
        video.write_videofile(NOME_VIDEO, fps=24, codec="libx264")

        return jsonify({"status": "sucesso", "mensagem": "Vídeo gerado com sucesso!"})

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)})