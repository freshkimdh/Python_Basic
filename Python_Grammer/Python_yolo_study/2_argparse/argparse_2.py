import argparse

parser = argparse.ArgumentParser(description="Thise is test script")
parser.add_argument("-v", "--verbosity", action='store_true', help="enable verbosity")
parser.parse_args()

if args.verbosity:
    print("verbosity enabled")

# Flag 형태 옵션 추가하기
# Short Option : single dash(-)
# Long Option : Double dash(--)