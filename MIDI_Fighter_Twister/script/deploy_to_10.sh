# removes the old scripts, and replaces with the ones in this folder

rm -rf /Applications/Ableton\ Live\ 10\ Suite.app/Contents/App-Resources/MIDI\ Remote\ Scripts/MIDI_Fighter_Twister

mkdir /Applications/Ableton\ Live\ 10\ Suite.app/Contents/App-Resources/MIDI\ Remote\ Scripts/MIDI_Fighter_Twister

cp ./*.py /Applications/Ableton\ Live\ 10\ Suite.app/Contents/App-Resources/MIDI\ Remote\ Scripts/MIDI_Fighter_Twister
