from yocto_releases.constants import URL_YOCTO_RELEASES
import requests
import html_to_json


class YoctoRelease:
    def __init__(self, yocto_version):
        """
        Initialize YoctoRelease attributes with the values from yocto_version dictionary
        :param yocto_version:  a dictionary that contains the Yocto release information
        """
        self._codename:                 str = yocto_version["Codename"]
        self._yocto_project_version:    str = yocto_version["Yocto Project Version"]
        self._release_date:             str = yocto_version["Release Date"]
        self._current_version:          str = yocto_version["Current Version"]
        self._support_level:            str = yocto_version["Support Level"]
        self._poky_version:             str = yocto_version["Poky Version"]
        self._bit_bake_branch:          str = yocto_version["BitBake branch"]
        self._maintainer:               str = ""

    def get_version(self):
        """
        :return: yocto project version
        """
        return self._yocto_project_version

    def get_codename(self):
        """
        :return: yocto project codename
        """
        return self._codename


class YoctoReleasesTable:
    def __init__(self):
        self.yocto_releases = self.generate_json_from_html_page()

    def get_yocto_releases(self):
        """
        :return: list of YoctoRelease objects
        """
        return self.yocto_releases

    def get_version_from_codename(self, codename: str):
        """
        Find the yocto project version from a given codename
        :param codename: yocto project codename
        :return: yocto project version
        """
        yocto_release_version = None
        yocto_release_filter = list(filter(lambda yocto_release: yocto_release.get_codename(
        ).lower() == codename.lower(), self.yocto_releases))
        if len(yocto_release_filter) != 1:
            raise Exception(
                f"The length of the list is not 1, it is {len(yocto_release_filter)}")
        yocto_release_version = yocto_release_filter[0].get_version()
        return yocto_release_version

    def get_codename_from_version(self, version: str):
        """
        Find the yocto project codename from a given version
        :param version: yocto project version
        :return: yocto project codename
        """
        yocto_release_codename = None
        yocto_release_filter = list(filter(
            lambda yocto_release: yocto_release.get_version() == version, self.yocto_releases))
        if len(yocto_release_filter) != 1:
            raise Exception(
                f"The length of the list is not 1, it is {len(yocto_release_filter)}")
        yocto_release_codename = yocto_release_filter[0].get_codename()
        return yocto_release_codename

    def generate_json_from_html_page(self, url_html: str = URL_YOCTO_RELEASES):
        """
        Retrieve the Yocto releases information from the Yocto website, converts the HTML table to JSON,
        and returns a list of YoctoRelease objects
        :param url_html: URL of the Yocto releases webpage
        :return: list of YoctoRelease objects
        """
        r = requests.get(url_html)
        html_page_content: str = r.text
        html_page_content = html_page_content.replace('\n', "")
        list_json_tables: list = html_to_json.convert_tables(
            html_string=html_page_content)
        yocto_releases_table: list = list_json_tables[0]
        yocto_releases: list[YoctoRelease] = []
        for row in yocto_releases_table:
            yocto_releases.append(YoctoRelease(row))
        return yocto_releases
