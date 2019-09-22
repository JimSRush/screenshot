# screenshot.py

This is a small command line python script that:
- takes a file from the command line with a list of relative paths
- loops through the file and uses [`pageres`](https://github.com/sindresorhus/pageres-cli) to screenshot and dump out jpg images of what it sees.

This is particularly useful for large CMS driven websites in lieu of comprehensive visual regression. or whatever

## What the file needs to look like

```/path-to/some-url
/path-to/some-other-url
/path-to/some-new-url
/path-to/some-oh-you-get-it
```

## Prerequisites

`npm i pagres-cli`
`python3`

## usage

`python3 snapshot.py -b https://mycool.website -f myAwesomeFile`
