# Miiyoo - Kiiroo Sex Toy Access Library and Server Simulator - DEPRECATED

**DEPRECATED** - Work moved to the [Buttplug Sex Toy Framework](https://buttplug.io)

Miiyoo is a library for providing bluetooth access to Kiiroo sex toys,
as well as creating a simulation of the web server that comes with the
Kiiroo server software.

## Kiiroo Protocol Documentation

Documentation about the low level Kiiroo protocol is at

[https://miiyoo.readthedocs.io](https://miiyoo.readthedocs.io)

The documentation repository is available at

[https://github.com/metafetish/miiyoo-docs](https://github.com/metafetish/miiyoo-docs)

## Kiiroo Platform Web Server Information

The Kiiroo Platform (available
from [Kiiroo's Website](https://www.kiiroo.com/download/)) is a nw.js
(node.js with embedded webkit instance) application that runs on the
desktop computer of a Kiiroo toy owner. This application opens an
unsecured http server at http://localhost:6969 (Yes. The port number
is NICE NICE. Nice.). Kiiroo products then communicate with the web
server via XHR requests.

To see a demo of this and read the code for accessing kiiroo toys
through this webserver, download one of the free videos
at [flicker.tv](http://flicker.tv). These video packs contain a small
web application that can be opened in the browser, to play videos and
synchronize with the toy. All javascript required for running the toy
is available in these archives in un-minified form.

## Disclaimer

The Miiyoo project is in no way affiliated with Kiiroo or any of its
partners. The documentation and libraries have been created via
information gathered from various sources (clean room reverse
engineering, reading javascript in webpages, etc), are provided with
no guarantees, as outlined by the license agreement. Usage of these
libraries and information is in no way condoned by Kiiroo and may void
the warranty of your toy.

## License

tl;dr: BSD 3-Clause License

Copyright (c) 2016, Metafetish Project
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name of the authors nor the names of its contributors
  may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY The Authors ''AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL The Authors BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE

