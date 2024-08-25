import pysrt

# Load the subtitle file
subs = pysrt.open('your_subtitle_file.srt')

# Set the target start time from where the subtitle should start {Here subtitle will start from 1 minute and 3 seconds}
target_time = pysrt.SubRipTime(minutes=1, seconds=3)

first_sub_time = subs[0].start
time_shift = target_time - first_sub_time

for sub in subs:
    sub.start += time_shift
    sub.end += time_shift

subs.save('new_subtitle.srt')
