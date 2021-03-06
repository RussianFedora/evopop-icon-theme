#!/bin/sh

NAME=$(rpm -q --specfile *.spec --qf "%{name}")
VERSION=$(rpm -q --specfile *.spec --qf "%{version}")
GITNAME=$(echo $NAME | sed 's@-0.7.*@@g')

rm -rf $NAME-$VERSION
git clone https://github.com/RussianFedora/$GITNAME-source.git $NAME-$VERSION --depth 1

cd $NAME-$VERSION
DATE=$(git log -1 --date=iso | awk '/Date:/ { print $2 }' | sed 's@-@@g')
REV=$(git log -1 | awk '/commit / { print $2 }' | cut -b 1-6)

cd ..
tar -ca --exclude-vcs --exclude-vcs-ignores -f $NAME-$VERSION-${DATE}git${REV}.tar.xz $NAME-$VERSION
rm -rf $NAME-$VERSION
