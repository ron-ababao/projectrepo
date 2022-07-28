import logging
import re
import glob
import shutil
import sys
import argparse
from pathlib import Path

log = logging.getLogger('bulk_renamer')
logging.basicConfig(
    level=logging.DEBUG,
    format=(
        '[%(asctime)s] %(levelname)s %(module)s '
        '%(funcName)s:%(lineno)d - %(message)s'
    ),
)

def search_files(pat, target_dir):
    found = []
    substring=pat
    folder_path=Path(target_dir).glob('**/*')
    for files in folder_path:
        if re.match(substring,Path(files).name):
            found.append(Path(files).name)

    log.info(f'Searching for files in {target_dir}')
    log.debug(f'pat - {pat}')
    log.debug(f'target_dir - {target_dir}')
    log.debug(f'found - {found}')
    log.info(f'Found {len(found)} files!')
    return found

def rename_file(name_change,old_file_name, directory_container):
    count=1
    path=directory_container
    folder_path=Path(path).glob('**/*')
    substring = old_file_name
    for files in folder_path:
        if re.match(substring,Path(files).name):
            source = path+'/'+Path(files).stem+Path(files).suffix
            destination=path+'/'+name_change+str(count)+Path(files).suffix
            if Path(destination).exists():
                while(Path(destination).exists()):
                    log.info(f'{Path(destination).name} exists. Finding available index')
                    print(f'{Path(destination).name} exists. Finding available index')
                    destination=path+'/'+name_change+str(count)+Path(files).suffix
                    count+=1
            shutil.move(source,destination)
            count+=1
            log.info(f'File name {Path(files).name} is now {Path(destination).name}')

def main(xargs):
    log.info('Start processing...')
    log.debug(f'xargs.new_name - {xargs.new_name}')
    log.debug(f'xargs.filter_pat - {xargs.filter_pat}')
    log.debug(f'xargs.target_dir - {xargs.target_dir}')
    found = search_files(xargs.filter_pat, xargs.target_dir)
    rename_file(xargs.new_name, xargs.filter_pat, xargs.target_dir)
    if not Path(xargs.target_dir).exists():
        log.error(f'xargs.target_dir "{xargs.target_dir}" does not exist.')
        print(f'The directory "{xargs.target_dir}" does not exist!')
        sys.exit(1)       
    else:
        sys.exit(0)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('new_name', help=('The new name of the files. This will be appended with a number.'))
    parser.add_argument('filter_pat', help='The name pattern to search.')
    parser.add_argument('target_dir',help='The directory to search.')
    xargs = parser.parse_args()
    
    main(xargs)
