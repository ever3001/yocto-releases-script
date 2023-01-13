# yocto-releases-script
This repository contains a Python script that provides a simple and efficient way to retrieve the versions of the Yocto Project.

## Prerequisites

The script is written in Python 3 and requires the following packages to be installed:

* html_to_json: https://pypi.org/project/html-to-json/

```bash
$ pip3 install html-to-json
```

## Usage

The script can be run with the following command:

```bash
./yocto_releases_script.py <method> <args>
```

The script supports the following methods:

* `--help`: Prints the help message.
* `--get_version_by_codename <codename>`: Returns the version of the Yocto Project corresponding to the given codename.
* `--get_codename_by_version <version>`: Returns the codename of the Yocto Project corresponding to the given version.

For example, to get the version of the Yocto Project corresponding to the `dunfell` codename, run the following command:

```bash
./yocto_releases_script.py --get_version_by_codename dunfell
```

The output of the command will be:

```bash
3.1
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* The script uses the Yocto Project release page: https://wiki.yoctoproject.org/wiki/Releases

## Authors
- [ever3001](https://github.com/ever3001)
- [Aderr0](https://github.com/Aderr0)

