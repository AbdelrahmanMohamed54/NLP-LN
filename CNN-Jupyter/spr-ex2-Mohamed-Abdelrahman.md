Mohamed, Abdelrahman, 22201965


1) What are the used (voice) commands?
- down
- go
- left
- no
- right
- stop
- up
- yes

2) Write down the value of your seed:
100

3) What is the number of samples?
Number of samples in training dataset: 100
Number of samples in validation dataset: 25
Number of samples in test dataset: 13
Total number of samples: 138

4) Split filenames into training, validation and test sets. The default is a 80:10:10
ratio, respectively. Use a good variation of this default. What is your number of
training files?
90:5:5
number of training files:- 57607 files

5) What is the name of the first file shown in the waveform diagram?
The first command is 'right', the name of the first file is 0ab3b47d_nohash_0.wav

6) Hear different WAV-files with an appropriate player-program. Describe the differences between the sounds you hear!
Pitch and Tone: Across different commands, variations in pitch and tone are noticeable. For instance, commands like "up" and "down" exhibit clear differences in pitch, with "up" having a higher pitch compared to "down." This difference in pitch helps distinguish between the two commands even without visual cues.
Background Noise: Some WAV-files contain background noise or ambient sounds, particularly noticeable in commands like "stop" or "go." This noise can vary in intensity and type, with some files having a faint hum while others have more pronounced background chatter. The presence of background noise can affect the clarity and intelligibility of the spoken command.
Clarity and Intensity: The clarity and intensity of the spoken commands vary across different recordings. Commands like "yes" and "no" tend to have clear and distinct enunciations, making them easily recognizable. However, in some recordings of commands like "left" or "right," the speaker's voice may sound muffled or less distinct, possibly due to recording conditions or speaker variations.
Speed and Pronunciation: In certain WAV-files, variations in the speed of speech and pronunciation become evident. For example, some recordings of the command "go" may sound faster-paced and more energetic, while others may sound slower and more deliberate. These differences in speed and pronunciation contribute to the overall variability in the dataset.
Overall, the WAV-files exhibit a range of acoustic characteristics, including differences in pitch, background noise, clarity, and speed of speech. These variations reflect the diversity of real-world audio recordings and highlight the challenges inherent in automatic speech recognition systems when dealing with different acoustic environments and speaking styles.

7) What is the sample rate for the WAV-file?
16000 Hz

8) Experiment with value of EPOCHs and change the default value. Write down the value of
your number of epochs.
30

9) What is the final test accuracy of your CNN?
0.8125

10) Describe the classification process in your own words! What do you think are the
features used for classification?
When it comes to classifying spoken words, the process is pretty fascinating. Imagine looking at a graph that shows how loud different pitches of sound are over time. That's essentially what a spectrogram is. Now, think about training a computer program, like a convolutional neural network (CNN), to understand these graphs and recognize patterns in them.
During training, the CNN learns to pick up on specific features in these spectrograms that are unique to each word. It's like teaching a friend to recognize the shape of different fruits by showing them pictures and pointing out key details. For instance, it might learn that the shape of the sound graph for "cat" is different from that of "dog" because of certain peaks and valleys at specific points.
Once the CNN has been trained on a bunch of these spectrograms paired with their corresponding words, it's like your friend has seen enough fruit pictures to recognize most of them. When you give the CNN a new spectrogram, it looks at the features it's learned and tries to match them up with the words it knows. Then, it makes a guess about what word it thinks the spectrogram represents based on the similarities it finds.
So, in essence, the CNN is like a friend who's become really good at recognizing different fruits just by looking at their shapes. It's all about teaching the computer to understand the unique features of each spoken word so it can make accurate guesses when it hears something new.