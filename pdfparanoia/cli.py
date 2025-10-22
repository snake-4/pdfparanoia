import sys
import pdfparanoia
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="pdfparanoia is a PDF watermark removal library for academic papers. Some publishers include private information like institution names, personal names, ip addresses, timestamps and other identifying information in watermarks on each page."
    )
    parser.add_argument("input", nargs=1)
    parser.add_argument("-o", "--output", default=sys.stdout)
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Output more information, which may be sensitive or excessive.",
    )
    args = parser.parse_args()

    inputContent = None
    with open(args.input[0], "rb") as input_file:
        inputContent = input_file.read()

    outputContent = pdfparanoia.scrub(inputContent, verbose=args.verbose)
    with open(args.output, "wb") as output_file:
        output_file.write(outputContent)
