
import yocto_releases.classes as classes
import yocto_releases.cmd_parser as cmd_parser


def main():
    parser = cmd_parser.init_argparse()
    args = parser.parse_args()
    yocto_releases_table = classes.YoctoReleasesTable()
    if args.codename:
        codename = yocto_releases_table.get_version_from_codename(args.codename)
        print(codename)
        return codename
    elif args.version:
        version = yocto_releases_table.get_codename_from_version(args.version)
        print(version)
        return version
    else:
        parser.print_help()
        return -1


if __name__ == '__main__':
    main()
