#!/bin/bash
#Try to get upstream latest files

DATE=$(date -u +%Y%m%d)
ARCHIVE="google-droid-fonts-$DATE"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp getdroid-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"
git init
git remote add -t HEAD origin https://android.googlesource.com/platform/frameworks/base.git
git config core.sparseCheckout true
cat > .git/info/sparse-checkout << EOF
data/fonts/*
!data/fonts/*ttf
data/fonts/Droid*
EOF
git pull --depth=1 --no-tags origin HEAD
mv data/fonts "$ARCHIVE"
chmod -x "$ARCHIVE/*.ttf"
tar -cvJf "$ARCHIVE.tar.xz" "$ARCHIVE"
popd
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
