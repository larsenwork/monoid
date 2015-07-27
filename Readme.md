<table>
    <tr>
        <td colspan="6"><img width="100%" src="https://github.com/andreaslarsen/monoid/raw/master/Utilities/Images/Monoid1.png" /></td>
    </tr>
    <tr>
        <td><a href="http://larsenwork.com/monoid/">WebPage</a></td>
        <td><a href="#guide">Guide</a></td>
        <td><a href="#links">Links</a></td>
        <td><a href="#font_log">Log</a></td>
        <td><a href="#license">License</a></td>
    </tr>
</table>

<a name="guide"></a>
------
#Guide

###Stylistic Alternates
The font contains more alternates than available on the webpage - see [StylisticAlternates.fea](https://github.com/larsenwork/monoid/blob/master/Utilities/StylisticAlternates.fea) for details. You can access these using `font-feature-settings` in your code editor stylesheet.

###Editor Support (ligatures)
I'm using opentype features `calt` + `liga` to create the ligatures. These are unfortunately not supported by all editors. You need to use the "Ligatures: Off" version if you're experiencing problems related to the ligatures.
#####Confirmed working
* Atom - Mac, Win, Linux
* Eclipse - all platforms
* gEdit - Linux
* LibreOffice Writer (yes, no editor, but support for ligatures) - Linux
* xCode - Mac

#####Not working
* Gnome Terminal - Linux
* gVim - Linux

#####Tips
* Atom Editor [Stylesheet](https://gist.github.com/larsenwork/255432b5101093fb07bc)


<a name="links"></a>
------
#Links
I did a talk on Monoid at a frontenders meetup and these are some links relevant to that talk.

* [Monoid Talk Slideshow](https://www.youtube.com/watch?v=hdld21mlzbY) - From Cph Frontenders meetup in june
* [FontForge](https://fontforge.github.io) - Free Font Editor
* [Design With FontForge](https://designwithfontforge.com) - Ebook to get you started with type designing
* [Cloudflare](https://cloudflare.com) - Cache, minification and no 302
* [RawGit](https://rawgit.com) - Serve download files with proper Content-Type headers
* [ WWDC Video](https://developer.apple.com/videos/wwdc/2015/?id=804) - San Francisco typefaces + general intro to type design
* [Ligatures & Coding Font](https://medium.com/@larsenwork/ligatures-coding-fonts-5375ab47ef8e) - short article I wrote pushing the envelope for coding fonts


<a name="font_log"></a>
------
#Font Log
Follow the [GitHub guide for contributing](https://guides.github.com/activities/contributing-to-open-source/#contributing) for issues, pull requests etc.<br>
Remember to update the Font Log when you make contributions.
<table>
    <tr>
        <td><a href="https://github.com/chase"><img src="https://avatars1.githubusercontent.com/u/5411?v=3&s=460" height="80" /><br>Chase</td>
        <td><a href="https://twitter.com/andreaslarsendk"><img src="https://avatars2.githubusercontent.com/u/3859425?v=3&s=460" height="80" /><br>Andreas</td>
    </tr>
</table>
<table>
    <tr>
        <td><b>Version</b></td>
        <td><b>Date</b></td>
        <td><b>Change</b></td>
        <td><b>Author</b></td>
    </tr>
    <tr>
        <td>0.10</td>
        <td>2015.04.03</td>
        <td>Latin basic</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.20</td>
        <td>2015.04.04</td>
        <td>Latin extended</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.24</td>
        <td>2015.04.06</td>
        <td>Cyrillic, feedback from <a href="https://github.com/K900">k900</a></td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.27</td>
        <td>2015.04.11</td>
        <td>Greek</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.28</td>
        <td>2015.04.12</td>
        <td>Misc. symbols</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.29</td>
        <td>2015.04.21</td>
        <td>CircleCI automation + build scripts</td>
        <td>Chase</td>
    </tr>
    <tr>
        <td>0.30</td>
        <td>2015.04.21</td>
        <td>Powerline symbols + major website update</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.31</td>
        <td>2015.06.03</td>
        <td>Alt s, smoother curves + bigger apertures</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.32</td>
        <td>2015.06.15</td>
        <td>New comma and many small adjustments to make it cleaner+sharper.</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.33</td>
        <td>2015.06.16</td>
        <td>Perfecting/many of the curved characters˛</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.34</td>
        <td>2015.06.17</td>
        <td>Updated metrics (note that default font-size is now 15px)</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.35</td>
        <td>2015.06.30</td>
        <td>Regular + retina version greatly improved. Oblique 80% done and bold(black) has basic latin.</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.40</td>
        <td>2015.07.14</td>
        <td>Bold, Oblique and retina version (basic letters)</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.41</td>
        <td>2015.07.21</td>
        <td>Super fast parallel builds, improved push checks, zipped font packages, automatic Github Pages font update</td>
        <td>Chase</td>
    </tr>
    <tr>
        <td>0.50</td>
        <td>2015.07.21</td>
        <td>Completed Bold, Oblique and Retina with all glyphs and ligatures.</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>0.51</td>
        <td>2015.07.22</td>
        <td>Fixed font naming issues and improved build times.</td>
        <td>Chase</td>
    </tr>
    <tr>
        <td>0.52</td>
        <td>2015.07.24</td>
        <td>Class based contextual positioning - regular only</td>
        <td>Andreas</td>
    </tr>
    <tr>
        <td>Wish List</td>
        <td>2015.xx.xx</td>
        <td>Download stats, generate versions live on site, ...</td>
        <td></td>
    </tr>
</table>

<a name="license"></a>
------
#Licenses
Monoid is dual licensed with MIT and OFL licenses. Pick one:)

###The MIT License (MIT)

Copyright (c) 2015, Andreas Larsen (@larsenwork) and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

###SIL OPEN FONT LICENSE
Copyright (c) 2015, Andreas Larsen (@larsenwork) and contributors.

This Font Software is licensed under the SIL Open Font License, Version 1.1.

This license is copied below, and is also available with a FAQ at: http://scripts.sil.org/OFL

#####SIL OPEN FONT LICENSE

Version 1.1 - 26 February 2007

#####PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded,
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

#####DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting — in part or in whole — any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

#####PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

#####TERMINATION
This license becomes null and void if any of the above conditions are
not met.

#####DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.
