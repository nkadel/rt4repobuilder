#!/bin/sh

@@PERL_PROV@@ "$@" | sed -e '/^perl(MyApp::/d'
