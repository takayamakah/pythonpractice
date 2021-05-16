# instalar biblioteca
# pip install moviepy

import moviepy.editor

#Captura caminho do vídeo a converter
path_video = input('Path Video [in]: ')

#Captura caminho para salvar o áudio 
path_audio = input('Path Audio [out]: ')

# Como parametro, passe a localização do video
video = moviepy.editor.VideoFileClip(path_video)
audio_video = video.audio

# Como parametro, passe o local onde sera salvo o audio
audio_video.write_audiofile(path_audio)