import argparse
from . import svn_client


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple SVN client wrapper")
    subparsers = parser.add_subparsers(dest="command")

    checkout_parser = subparsers.add_parser("checkout", help="Checkout repository")
    checkout_parser.add_argument("url")
    checkout_parser.add_argument("dest")

    commit_parser = subparsers.add_parser("commit", help="Commit changes")
    commit_parser.add_argument("message")

    args = parser.parse_args(argv)

    if args.command == "checkout":
        svn_client.checkout(args.url, args.dest)
    elif args.command == "commit":
        svn_client.commit(args.message)
    else:
        parser.print_help()
