#!/usr/bin/env python
#
# Copyright 2018 WebAssembly Community Group participants
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import argparse
import hashlib
import sys


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?')
    options = parser.parse_args(args)

    if options.file is None:
        parser.error('Expected a file')

    m = hashlib.sha256()
    with open(options.file, 'rb') as f:
        m.update(f.read())
    print('%s  %s' % (m.hexdigest(), options.file))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
