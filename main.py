import os
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw

def generar_fondo_infantil(nombre_archivo="fondo.png"):
    # Crea una imagen de fondo vertical (ideal para YouTube Shorts)
    ancho, alto = 1080, 1920
    img = Image.new("RGB", (ancho, alto), color=(135, 206, 250)) # Azul cielo
    draw = ImageDraw.Draw(img)
    
    # Dibuja un sol alegre de fondo
    draw.ellipse([800, 100, 980, 280], fill=(255, 215, 0))
    
    img.save(nombre_archivo)
    print("🎨 Fondo infantil generado automáticamente.")

def generar_voz_narrador(texto, archivo_audio="audio.mp3"):
    print("🗣️ Generando la voz en off automáticamente...")
    tts = gTTS(text=texto, lang='es', slow=False)
    tts.save(archivo_audio)
    print("✅ Audio generado con éxito.")

def crear_video_completo():
    texto_cuento = "¡Hola amiguitos! Bienvenidos a un nuevo video de curiosidades. ¿Sabías que los delfines duermen con un ojo abierto? ¡Qué dato tan asombroso!"
    archivo_audio = "audio.mp3"
    imagen_fondo = "fondo.png"
    video_salida = "video_final.mp4"
    
    # 1. Generar recursos automáticamente
    generar_fondo_infantil(imagen_fondo)
    generar_voz_narrador(texto_cuento, archivo_audio)
    
    print("🎬 Ensamblando el video...")
    
    # 2. Cargar audio y calcular duración
    audio_clip = AudioFileClip(archivo_audio)
    duracion = audio_clip.duration
    
    # 3. Crear clip de imagen ajustado al audio
    imagen_clip = ImageClip(imagen_fondo).set_duration(duracion)
    
    # 4. Crear subtítulos grandes para niños
    txt_clip = TextClip(
        texto_cuento, 
        fontsize=60, 
        color='yellow', 
        font='sans-serif', 
        stroke_color='black', 
        stroke_width=3,
        size=(imagen_clip.w * 0.85, None), 
        method='caption'
    ).set_duration(duracion).set_position(('center', 'center'))
    
    # 5. Combinar imagen, texto y audio
    video_base = CompositeVideoClip([imagen_clip, txt_clip])
    video_final = video_base.set_audio(audio_clip)
    
    print("🚀 Renderizando el video final...")
    video_final.write_videofile(
        video_salida, 
        fps=24, 
        codec='libx264', 
        audio_codec='aac'
    )
    print(f"🎉 ¡Proceso terminado! Video listo: {video_salida}")

if __name__ == "__main__":
    crear_video_completo()
