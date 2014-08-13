#!/bin/bash

#Generate movies using ffmpeg
ffmpeg -y -r 5 -i frames/%03d.png -vcodec libx264 -r 25 -pix_fmt yuv420p figs/movie.mp4 
