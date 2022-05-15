#importing packages
import ffmpeg
import sys, os

#ffmpeg file path
sys.path.append(r'C:\Program Files\ffmpeg-4.4\bin') 

#Class declaration
class PythonSwitch:
    def video(self, choices):

        default = "Incorrect Option"

        return getattr(self, 'case_' + str(choices), lambda: default)()

    #For trimming the video
    def case_Trim(self):
        os.system("ffmpeg -ss 00:00:10 -to 00:00:25  -i Nature.mp4 -c copy Trim.mp4")
        return print("Triming Done")
    
    #For Changing the aspect ration to scale of 640:360
    def case_Aspectratio(self):
        os.system("ffmpeg -i Nature.mp4 -vf scale=720x406,setdar=16:9 -preset slow -crf 18 AspectRatio.mp4")
        return print("Changing Aspect Ratio")
    
    #For changing the bitrate to 1.5
    def case_Bitrate(self):
        os.system("ffmpeg -i Nature.mp4 -b:v 1.5M Bitrate.mp4")
        return print("Changing Bit Rate")
    
    #For changing the Framerate to 40
    def case_Framerate(self):
        os.system("ffmpeg -y -r 40 -i Nature.mp4 Framerate.mp4")
        return print("Changing Frame Rate")
    
    #For changing the Frame to 320:240
    def case_Framesize(self):
        os.system("ffmpeg -i Nature.mp4 -vf scale=320:240,setsar=1:1 Framesize.mp4")
        return print("Changing Frame Size")
    
    #For removing the audio / Mute audio
    def case_Mute(self):
        os.system("ffmpeg -i Nature.mp4 -c copy -an Mute.mp4")
        return print("Muting the Audio")
    
    #Only Audio / Remove Video
    def case_Remove(self):
        os.system("ffmpeg -i Nature.mp4 -map 0 -c copy Audio.mp4")
        return print("Removing Video")
    
    #mp4 to HTTP Live Streaming (HLS)
    def case_Convert(self):
        os.system("ffmpeg -i Nature.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls HLS.m3u8")
        return print("converting Mp4 to HLS")

    #get the images from video
    def case_Image(self):
        os.system("ffmpeg -i Nature.mp4 -r 1 -f image2 image-%2d.png")
        return print("Images Generated")

    #Split the video
    def case_Split(self):
        os.system("ffmpeg -i Nature.mp4 -t 00:00:30 -c copy part1.mp4 -ss 00:00:30 -codec copy part2.mp4")
        return print("Video Splitted")

    #Play the File
    def case_Play(self):
        os.system("ffplay Nature.mp4")
        return print("Started")
my_switch = PythonSwitch()

print("\n1.Trim\n 2.Change Aspect Ratio\n 3.Change Bitrate\n 4.Change Frame Rate\n 5.Change Frame Size\n 6.Mute Audio\n 7.Mute Video\n 8.Convert MP4 to HLS \n 9.Generate Images \n 10. Split Video \n 11.Play Video")
#Getting input from the user for how many operation user wants to perform
value = int(input("How many operation do you want to perform?"))

#Getting the list of operations to be performed
operations=[]
for i in range(value):
    range(0,value)
    operations.append(input("Operation name to be performed: "))

#Showing the functions that need to be operated
print("Below are the functions you want to perform:")
print(operations)

#Condition checking for the user input and operating as per the user input
if 'Trim' in operations:
    my_switch.video('Trim')

if 'Change aspect ratio' in operations:
    my_switch.video('Aspectratio')

if 'Change Bitrate' in operations:
    my_switch.video('Bitrate')

if 'Change Frame Rate' in operations:
    my_switch.video('Framerate')

if 'Change Frame Size' in operations:
    my_switch.video('Framesize')

if 'Mute Audio'  in operations:
    my_switch.video('Mute')

if 'Remove Video' in operations:
    my_switch.video('Remove')

if 'Convert MP4 to HLS' in operations:
    my_switch.video('Convert')

if 'Generate Images' in operations:
    my_switch.video('Image')

if 'Split Video' in operations:
    my_switch.video('Split')

if 'Play File' in operations:
    my_switch.video('Play')

