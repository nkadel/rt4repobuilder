#!/bin/sh

@@PERL_REQ@@ "$@" | sed -e '/^perl(MasonX::Request::PlusApacheSession)$/d'
