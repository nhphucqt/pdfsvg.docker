import json
import subprocess
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Extract figures from a PDF file as SVG images.")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("-d", "--figure-data-prefix", default="figure_data/", help="Prefix for the JSON file with figures' metadata")
    parser.add_argument("-m", "--figure-prefix", default="figure/", help="Prefix for the output SVG files")
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_args()

    basename_noext = os.path.splitext(os.path.basename(args.pdf))[0]

    # java -jar pdffigures2.jar /home/pdfs/2309.01083v1.pdf -m /home/images/ -d /home/outputs/
    subprocess.run([
        "java", "-jar", "pdffigures2.jar",
        args.pdf, "-m", args.figure_prefix, "-d", args.figure_data_prefix
    ])

    # Load the JSON file with figures' metadata
    json_path = args.figure_data_prefix + f"{basename_noext}.json"
    with open(json_path) as f:
        figures = json.load(f)

    # Process each figure
    for i, fig in enumerate(figures):
        # Get page number and bounding box from the JSON data
        page = fig['page'] + 1  # Pages in pdftocairo are 1-based
        region = fig['regionBoundary']
        x1, y1 = map(int, (region['x1'], region['y1']))
        x2, y2 = map(int, (region['x2']+1, region['y2']+1))
        width = x2 - x1
        height = y2 - y1

        # Output SVG filename
        output_svg = os.path.splitext(fig['renderURL'])[0] + ".svg"

        # Run pdftocairo command
        subprocess.run([
            "pdftocairo", "-svg", "-f", str(page), "-l", str(page),
            "-x", str(int(x1)), "-y", str(int(y1)),
            "-W", str(int(width)), "-H", str(int(height)),
            args.pdf, output_svg
        ])

        print(f"Saved as {output_svg}")

if __name__ == "__main__":
    main()