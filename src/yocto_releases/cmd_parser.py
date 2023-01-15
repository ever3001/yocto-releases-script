import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        "yocto_releases",
        description="A Python module to get the Yocto Project releases from the Yocto Project website",
        add_help=True
    )

    parser.add_argument(
        '-c',
        '--get_version_by_codename',
        dest='codename',
        help="Get the version of a Yocto Project release by its codename. Usage: yocto_releases -c <codename>. Example: yocto_releases -c kirkstone",
        type=str
    )

    parser.add_argument(
        '-v',
        '--get_codename_by_version',
        dest='version',
        help="Get the codename of a Yocto Project release by its version. Usage: yocto_releases -v <version>. Example: yocto_releases -v 4.1",
        type=str
    )

    return parser
