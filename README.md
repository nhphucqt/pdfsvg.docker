# pdfsvg with pdffigures2 and pdftocairo

## Installation

### Build docker image

```bash
docker build . -t "pdfsvg:1.0" 
```

### Create container

```bash
docker run -it --name pdfsvg -v /path/to/pdf/directory:/mnt/pdf pdfsvg:1.0
```

## Usage

```
usage: extract_svg.py [-h] [-d FIGURE_DATA_PREFIX] [-m FIGURE_PREFIX] pdf

Extract figures from a PDF file as SVG images.

positional arguments:
  pdf                   Path to the PDF file

options:
  -h, --help            show this help message and exit
  -d FIGURE_DATA_PREFIX, --figure-data-prefix FIGURE_DATA_PREFIX
                        Prefix for the JSON file with figures' metadata
  -m FIGURE_PREFIX, --figure-prefix FIGURE_PREFIX
                        Prefix for the output SVG files
```

### Example

```bash
python3 extract_svg.py /mnt/pdf/path/to/pdf_file.pdf -d /mnt/pdf/outputs/ -m /mnt/pdf/images/
```

# References

```
@article{pdffigures2,
     title = {PDFFigures 2.0: Mining Figures from Research Papers},
     author = {Christopher Clark and Santosh Divvala},
     booktitle = {JCDL},
     year = {2016}
}
```