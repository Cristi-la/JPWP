import argparse
import os
import shutil


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='.', help='Destination directory')
    parser.add_argument('--folder', type=str, default='crab', help='Creates folder for CRAB files')
    parser.add_argument('--create', action='store_true')

    args = parser.parse_args()

    if args.create:
        create_command(args.path, args.folder)

def create_command(path, folder):
    """Copy package template folder to current / specified location"""

    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    dest_dir = os.getcwd() if path is None else path

    try:
        shutil.copytree(template_dir, os.path.join(dest_dir, folder))
        print(f"CRAB successfully created to {dest_dir}")
    except FileExistsError:
            print(f"ERROR! Directory already exists at {os.path.join(dest_dir, folder)}")
    except Exception as e:
        print(f"ERROR! While copying templates file: {e}")


if __name__ == '__main__':
    run()