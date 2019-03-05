import subprocess as sp
import sys
import os


FFMPEG_BIN = "C:/ffmpeg/bin/ffmpeg.exe"
command = [ FFMPEG_BIN, '-y',
            '-f', 'dshow', '-rtbufsize', '100M',
            '-i', 'video=Datapath VisionAV Video 01' ,
             '-video_size', '640x480',
              '-pix_fmt', 'bgr24', '-r','25',  
          '-f', 'image2pipe', '-' ]    


try:    
    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True)`

    ffmpeg_output, _ = pipe.communicate()

except  sp.CalledProcessError as err:
     print("FFmpeg stdout output on error:\n" + err.output)
