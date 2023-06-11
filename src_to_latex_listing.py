"""
This script will take all files in `SRC_DIRECTORY`
and print them to `SRC_LISTING_FILE`
"""
import os

SRC_DIRECTORY = "src"
SRC_LISTING_FILE = "doc/src_listing.tex"

# pylint: disable-next=unspecified-encoding
with open(SRC_LISTING_FILE, "w") as f:
    for root, _, files in os.walk(SRC_DIRECTORY):
        for filename in files:
            if filename.endswith(".py"):
                filepath = os.path.join('..', root, filename)
                f.write(f"\\centerline{{\"{filepath}\"}}\n".replace('_', '\\_'))
                f.write(f"\\verbatiminput{{{filepath}}}\n")
