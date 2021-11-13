import unicodedata
import os
import codecs

# absolute path of your PRUS.txt
input_text_file = 'C:\\Users\\Haris Bin Zia\\Desktop\\Project\\PRUS.txt'
# absolute path of new PRUS.txt
output_text_file = 'C:\\Users\\Haris Bin Zia\\Desktop\\Project\\PRUS_NEW.txt'
# absolute path of your recordings folder
wav_input_folder = 'C:\\Users\\Haris Bin Zia\\Desktop\\Project\\21100000\\'
# your roll number
rollnumber = '21100000'
f = codecs.open(input_text_file, 'r', encoding='utf-8')
p = codecs.open(output_text_file, 'w', encoding='utf-8')
i = 1
for line in f:
    line = line.replace(u'\ufeff','')
    line = line.replace(u'\u200C','')
    line = unicodedata.normalize('NFC',line)
    p.write(rollnumber + '_' + str(i).zfill(3) + ' ' +line.strip() + '\n')
    i += 1
f.close()
p.close()
print("Done writing new file at: ", output_text_file)
for filename in os.listdir(wav_input_folder):
    source =  wav_input_folder + filename
    dest =  wav_input_folder + rollnumber + '_' + filename[:-4].zfill(3) + filename[-4:]
    os.rename(source, dest)
print("Done renaming wav files at: ", wav_input_folder)

