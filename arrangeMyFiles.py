import shutil
import os
import sys, traceback
import json
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


with open('arrangeCfg.json', "r", encoding="utf-8") as config_file:
    data = json.load(config_file)
    source = data['source']

def main():
    logging.info(f'source: {source} ')
    fileTypes = data['fileTypes']
    fileTypesKeys = fileTypes.keys()
    for key in fileTypes:
        extensions = fileTypes[key]['extension']
        destination = fileTypes[key]['destination']
        destinationSubFolders = os.listdir(destination)

        for extension in extensions:
            source_files = os.listdir(source)
            for file in source_files:
                if extension in file:
                    for folder in destinationSubFolders:
                        if os.path.isdir(destination+"\\"+folder):
                            if folder in file:
                                print("folder: --}",destination+"\\"+folder,'file:-->',file)
                                if os.path.exists(os.path.join(destination,folder,file)):
                                    print( file + ': the file will be renamed')
                                    logging.info(f'the file: {file} will be renamed')
                                    copy_file_name = 'copy_'+ file
                                    shutil.move(os.path.join(source , file), os.path.join(destination,folder,copy_file_name))
                                    source_files.remove(file)
                                else:
                                    shutil.move(os.path.join(source.replace("'",""), file),os.path.join(destination,folder,file))
                                    source_files.remove(file)
                            else:
                                try:
                                    if os.path.exists(os.path.join(destination,file)):
                                        print( file + ': the file will be renamed')
                                        logging.info(f'the file: {file} will be renamed')
                                        copy_file_name = 'copy_'+ file
                                        shutil.move(os.path.join(source , file), os.path.join(destination, copy_file_name))
                                        source_files.remove(file)
                                    else:
                                        shutil.move(os.path.join(source.replace("'",""), file),os.path.join(destination,file))
                                        source_files.remove(file)
                                except Exception as Ex:
                                    print(Ex)
                                    logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    main()
