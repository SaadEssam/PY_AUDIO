import os
import eyed3

def rewrite_audio_titles(source_folder, reference_folder):
    # Get a list of audio files in the source folder
    audio_files = [file for file in os.listdir(source_folder) if file.endswith('.mp3')]

    for file in audio_files:
        # Load the audio file
        audio_path = os.path.join(source_folder, file)
        audio = eyed3.load(audio_path)

        if audio is not None:
            # Get the corresponding reference audio file
            reference_file = os.path.join(reference_folder, file)
            reference_audio = eyed3.load(reference_file)

            if reference_audio is not None and reference_audio.tag.title is not None:
                new_title = reference_audio.tag.title
                print(f'Rewriting title of {file} to "{new_title}"')

                # Set the new title
                audio.tag.title = new_title

                # Save the changes
                audio.tag.save()

# replace paths with the actual paths to your audio files folder and reference files folder
source_folder = 'E:\Quran\Quran-Ahmed-khalil-shaheen'
reference_folder = 'E:\Quran\Quran-Yasser-Al_Dosari'

rewrite_audio_titles(source_folder, reference_folder)
