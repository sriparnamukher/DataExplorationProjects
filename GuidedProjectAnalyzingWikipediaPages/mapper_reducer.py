import os
foldername = "wiki"
def map_lines_count(filenames_chunk):
    lines_count_chunk = 0
    for filename in filenames_chunk:
        with open(os.path.join(foldername, filename), encoding='utf-8') as f:
            lines_count_chunk += len(f.readlines())
    return(lines_count_chunk)

def reduce_lines_count(count1, count2):
    return (count1 + count2)



target_word = 'data'
def map_word_locs_chunk(filenames_chunk):
    word_locs = {}
    for filename in filenames_chunk:
        with open(os.path.join(foldername, filename), encoding='utf-8') as f:
            locs_in_file = []
            for idx, line in enumerate(f.readlines()):
                if target_word in line:
                    locs_in_file.append(idx)
        word_locs[filename] = locs_in_file
    return(word_locs)

def reduce_word_locs(locs1, locs2):
    locs1.update(locs2)
    return(locs1)

def map_word_locs_chunk_case_insen(filenames_chunk):
    word_locs = {}
    for filename in filenames_chunk:
        with open(os.path.join(foldername, filename), encoding='utf-8') as f:
            locs_in_file = []
            for idx, line in enumerate(f.readlines()):
                if target_word.lower() in line.lower():
                    locs_in_file.append(idx)
        word_locs[filename] = locs_in_file
    return(word_locs)

import re
def map_word_locs_rowcol_chunk_case_insen(filenames_chunk):
    word_locs = {}
    for filename in filenames_chunk:
        with open(os.path.join(foldername, filename), encoding='utf-8') as f:
            locs_in_file = []
            for idx, line in enumerate(f.readlines()):
                locs_line = [(idx, match.start()) for match in re.finditer('data'.lower(), line.lower())]
                locs_in_file.extend(locs_line)
        word_locs[filename] = locs_in_file
    return(word_locs)

def map_science_locs_rowcol_chunk_case_insen(filenames_chunk):
    word_locs = {}
    for filename in filenames_chunk:
        with open(os.path.join(foldername, filename), encoding='utf-8') as f:
            locs_in_file = []
            for idx, line in enumerate(f.readlines()):
                locs_line = [(idx, match.start()) for match in re.finditer('science'.lower(), line.lower())]
                locs_in_file.extend(locs_line)
        word_locs[filename] = locs_in_file
    return(word_locs)
