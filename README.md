# mouse data analysis with data from 1/8

- Ines used their camera to record
- We forgot to record the moment the bio-logger was attached, but we do have when it was taken off (my watch is in view at the end)
- Since EEG is 250Hz, you can backout when the recording started and align the video to the raw data
- data.csv are int32 and type.csv are uint8

## tasks

- In the final version of the biologgers, I would like to have a ‘sync’ data type to align the data.
- The data I’m giving you are more like how they might do it with axy collars (using a watch).
- I want you to think through the syncing problem by trying to align data with the video.
- In the past, I’ve implemented some method of syncing, then exported video frames in a figure with data plotted below it, or created a synced video for it all (which might be overkill here), but the point is, you need to prove to yourself you didn’t make a mistake, which should be straightforward with axy data.
- Video end time is 12:11pm, so start time should be around 10:43am

## based on prev coding task

- EEG 1-4 were types 2-5 respectively
- Axy XYZ were types 7-9