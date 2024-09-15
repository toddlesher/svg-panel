# svg panel

## Usage

venv ...
cd py/svgpanel
.

## Requirements

* Python 3.10+ (no reason - 3.10.12 is currently on this machine)

## Pre-requisites

You can install pre-requisites by running `./bootstrap` from the current
directory. This will install or update any requirements for running scripts. It
is safe to re-run this script multiple times. If you see errors that look like
missing dependencies, try re-running `./bootstrap` in case new dependencies
were added.

For doing development, you should run `./bootstrap --dev` as it installs
various additional requirements that are needed for running tests, etc.

## Organization

None, really. Just trying out this copied structure.

## Style Guide

* This repo tries to follow the Google python style guide
  (https://google.github.io/styleguide/pyguide.html) where it makes sense.
* All code gets autoformatted with `black` and imports are sorted with `isort`.
