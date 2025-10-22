# pdfparanoia

This repository is a fork of [pdfparanoia](https://github.com/kanzure/pdfparanoia). The code was rewritten to use pdfminer.six, Python 3 and a modern build system.

pdfparanoia is a PDF watermark removal library for academic papers. Some publishers include private information, like institution names, personal names, IP addresses, timestamps, and other identifying information, in watermarks on each page.

## Installation

```bash
git clone https://github.com/snake-4/pdfparanoia.git
cd pdfparanoia
pip install .
```

## Usage

### As a library

```python
import pdfparanoia

with open("nmat91417.pdf", "rb") as fin:
    with open("output.pdf", "wb") as fout:
        fout.write(pdfparanoia.scrub(fin.read()))
```

### From the command line

```bash
pdfparanoia --verbose input.pdf -o output.pdf
```

## Supported Publishers

* AIP
* IEEE
* JSTOR
* RSC
