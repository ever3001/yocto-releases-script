#!/usr/bin/env python3

import sys
import html_to_json
import subprocess
import argparse

URL_YOCTO_RELEASES = "https://wiki.yoctoproject.org/wiki/Releases"

def generate_json_from_html_page(url=URL_YOCTO_RELEASES):
    html_page_content: str = str(subprocess.check_output(f"curl {url}", shell=True, stderr=subprocess.DEVNULL))
    html_page_content = html_page_content.replace('\\n', "")
    list_json_tables: list = html_to_json.convert_tables(html_string=html_page_content)
    yocto_releases_table: list = list_json_tables[0]
    yocto_releases: list[YoctoRelease] = [] 
    for row in yocto_releases_table:
        yocto_releases.append(YoctoRelease(row))
    return yocto_releases


class YoctoRelease:
    def __init__(self, yocto_version):
        self._codename:              str = yocto_version["Codename"]
        self._yocto_project_version: str = yocto_version["Yocto Project Version"]
        self._release_date:          str = yocto_version["Release Date"]
        self._current_version:       str = yocto_version["Current Version"]
        self._support_level:         str = yocto_version["Support Level"]
        self._poky_version:          str = yocto_version["Poky Version"]
        self._bit_bake_branch:       str = yocto_version["BitBake branch"]
        self._maintainer:            str = ""

    def get_version(self):
        return self._yocto_project_version
    
    def get_codename(self):
        return self._codename

class YoctoReleasesTable:
    def __init__(self):
        self.yocto_releases = generate_json_from_html_page()

    def get_yocto_releases(self):
        return self.yocto_releases
    
    def get_version_from_codename(self, codename: str):
        yocto_release_version = None
        yocto_release_filter = list(filter(lambda yocto_release : yocto_release.get_codename().lower() == codename.lower(), self.yocto_releases))
        if len(yocto_release_filter) != 1:
            raise Exception(f"The length of the list is not 1, it is {len(yocto_release_filter)}")
        yocto_release_version = yocto_release_filter[0].get_version()
        print(yocto_release_version)
        return yocto_release_version
        
    def get_codename_from_version(self, version: str):
        yocto_release_codename = None
        yocto_release_filter = list(filter(lambda yocto_release : yocto_release.get_version() == version, self.yocto_releases))
        if len(yocto_release_filter) != 1:
            raise Exception(f"The length of the list is not 1, it is {len(yocto_release_filter)}")
        yocto_release_codename = yocto_release_filter[0].get_codename()
        print(yocto_release_codename)
        return yocto_release_codename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--get_version_by_codename', dest='codename', type=str)
    parser.add_argument('-c', dest='codename', type=str)
    parser.add_argument('--get_codename_by_version', dest='version', type=str)
    parser.add_argument('-v', dest='version', type=str)
    args = parser.parse_args()
    yocto_releases_table = YoctoReleasesTable()
    if args.codename:
        yocto_releases_table.get_version_from_codename(args.codename)
    elif args.version:
        yocto_releases_table.get_codename_from_version(args.version)
    else:
        print('Please provide either --get_version_by_codename or --get_codename_by_version')

if __name__ == '__main__':
    main()