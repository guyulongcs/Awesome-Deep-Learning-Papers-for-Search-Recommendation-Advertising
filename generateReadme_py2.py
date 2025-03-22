#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib

""" generate readme.md """
__author__ = 'Yulong Gu'

sort_reverse = False


paper_class_map = {}
paper_map = {}

all_lines = []
if(os.path.exists('./README.md')):
    file_object = open('./README.md')
    all_lines = file_object.readlines()
    file_object.close()

out_file = open('./README.md', 'w')

paper_class_flag = 0
paper_class_name = ""
paper_flag = 0
paper_name = ""
catalog_flag = 0

for line in all_lines:
    if catalog_flag != 1:
        out_file.write(line)
    if line.startswith("##"):
        catalog_flag = 1

    if paper_class_flag == 1 and not line.startswith("*") and not line.startswith("#"):
        paper_class_map[paper_class_name] = line.strip()
        #print paper_class_name, line.strip()
    paper_class_flag = 0

    if paper_flag == 1 and not line.startswith("*") and not line.startswith("#"):
        paper_map[paper_name] = line.strip()
        #print "\t", paper_name, line.strip()

    paper_flag = 0

    if catalog_flag == 1:
        if line.startswith("*"):
            paper_flag = 1
            paper_name = line[line.find("[")+1:line.find("]")].strip()

    if line.startswith("##"):
        paper_class_flag = 1
        paper_class_name = line[3:].strip()

github_root = "https://github.com/guyulongcs/Deep-Learning-for-Search-Recommendation-Advertisements/blob/master/"
all_dir = os.listdir("./")
all_dir.sort()
for one_dir in all_dir:
    if os.path.isdir(one_dir) and not one_dir.startswith('.'):
        out_file.write("\n## " + one_dir+"\n")
        if one_dir.strip() in paper_class_map:
            out_file.write(paper_class_map[one_dir.strip()] + "\n")
        all_sub_files = os.listdir(one_dir)
        all_sub_files.sort(reverse=sort_reverse)
        for one_file in all_sub_files:
            # print("one_file:%s, is_dir:%d" % (one_file, os.path.isdir(os.path.join(one_dir, one_file))))
            one_file_2=os.path.join(one_dir, one_file)
            if not os.path.isdir(one_file_2) and not one_file.startswith('.'):
                out_file.write("* [" + ('.').join(one_file.split('.')[:-1]) + "]("+github_root + one_dir.strip()+"/"
                               + urllib.quote(one_file.strip()) +") <br />\n")
                if one_file.strip() in paper_map:
                    out_file.write(paper_map[one_file.strip()] + "\n")

        all_sub_files.sort(reverse=sort_reverse)
        for one_file in all_sub_files:
            one_file_2=os.path.join(one_dir, one_file)
            if os.path.isdir(one_file_2) and not one_file_2.startswith('.'):
                one_dir_second = one_file_2
                # print("one_dir_second:",one_dir_second)
                out_file.write("\n#### " + one_file +"\n")
                all_sub_files_second = os.listdir(one_dir_second)
                all_sub_files_second.sort(reverse=sort_reverse)
                for one_file_second in all_sub_files_second:
                    # print("one_file_second:",one_file_second)
                    if not os.path.isdir(one_file_second) and not one_file_second.startswith('.'):
                        out_file.write("* [" + ('.').join(one_file_second.split('.')[:-1]) + "]("+ github_root 
                                + urllib.quote(one_dir_second.strip())+"/"
                               + urllib.quote(one_file_second.strip())+") <br />\n")


out_file.close()
