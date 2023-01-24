# pdfparanoia

pdfparanoia is a PDF watermark removal library for academic papers. Some
publishers include private information like institution names, personal names,
ip addresses, timestamps and other identifying information in watermarks on
each page.

pdfparanoia это библиотека для удаления водяных знаков из PDF файлов научных
статей. Некоторые издатели включают личную информацию, такую как названия
институтов, имена, IP-адреса, время и дату и другую информацию в водяные знаки
содержащиеся на каждой странице.

## Installing

Simple.

``` bash
sudo pip install pdfparanoia
```

or,

``` bash
sudo python setup.py install
```

## Usage

``` python
import pdfparanoia

with open("nmat91417.pdf", "rb") as inputF:
    with open("output.pdf", "wb") as outputF:
        outputF.write(pdfparanoia.scrub(inputF.read()))
```

or from the shell,

``` bash
pdfparanoia --verbose input.pdf -o output.pdf
```

## Supported

* AIP
* IEEE
* JSTOR
* RSC
* SPIE (sort of)

## Changelog

* 0.0.13 - RSC
* 0.0.12 - SPIE
* 0.0.11 - pdfparanoia command-line interface. Use it by either piping in pdf data, or specifying a path to a pdf in the first argv slot.
* 0.0.10 - JSTOR
* 0.0.9 - AIP: better checks for false-positives; IEEE: remove stdout garbage.
* 0.0.8 - IEEE

## License

BSD.
