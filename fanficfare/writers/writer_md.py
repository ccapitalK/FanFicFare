# -*- coding: utf-8 -*-

# Copyright 2011 Fanficdownloader team, 2015 FanFicFare team
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
#

import logging
import string
from base_writer import *
from writer_txt import TextWriter

## Since TextWrite uses html2text under the hood, which happens to output
## valid markdown, all we really need to do is change the format functions
## and default string templates
class MarkdownWriter(TextWriter):

    @staticmethod
    def getFormatName():
        return 'markdown'

    @staticmethod
    def getFormatExt():
        return '.md'

    def __init__(self, config, story):
        
        BaseStoryWriter.__init__(self, config, story)
        
        self.TEXT_FILE_START = string.Template(u'''


# ${title}

#### by ${author}


''')

        self.TEXT_TITLE_PAGE_START = string.Template(u'''
''')

        self.TEXT_TITLE_ENTRY = string.Template(u'''- **${label}:** ${value}
''')

        self.TEXT_TITLE_PAGE_END = string.Template(u'''


''')

        self.TEXT_TOC_PAGE_START = string.Template(u'''

## TABLE OF CONTENTS

''')

        self.TEXT_TOC_ENTRY = string.Template(u'''
- ${chapter}
''')
                          
        self.TEXT_TOC_PAGE_END = string.Template(u'''
''')

        self.TEXT_CHAPTER_START = string.Template(u'''

## ${chapter}

''')
        self.TEXT_CHAPTER_END = string.Template(u'''
---

''')

        self.TEXT_FILE_END = string.Template(u'''
''')
