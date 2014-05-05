#! /bin/bash
#
# gen_spec.sh
# Copyright (C) 2014 tim <tim@titanium.co.goldfish>
#
# Distributed under terms of the MIT license.
#


############# gen spec
GEM=$1
[ ! -z $2 ] && VERSION=" -v $2" || VERSION=''

gem list --remote -a $GEM
GEM_VERSION=''
TMPDIR=$(mktemp -d)
RETOUT=$(cd ${TMPDIR} && gem fetch ${GEM}$VERSION)
RETVAL=$?
if [ ${RETVAL} -eq 0 ]
then 
    GEM_VERSION=$(echo ${RETOUT}|awk '{print $2}')
    echo "Downloaded: ${GEM_VERSION}"
else 
    echo "Error: ${RETOUT}"
fi
TMPL=rubygem-${GEM}.spec.template
if [ ! -f ${TMPL} ]
then
    gem2rpm -T > ${TMPL}
    echo "Generated new spec template: ${TMPL}"
fi
if [ -f rubygem-${GEM}.spec.template ] 
then
    gem2rpm -t rubygem-${GEM}.spec.template ${TMPDIR}/${GEM_VERSION}.gem > rubygem-${GEM}.spec || exit 1
fi
[ -d ${TMPDIR} ] && rm -rf ${TMPDIR}  || exit 1

############ Build
SPEC=rubygem-${GEM}.spec
BUILD_DATE=$(date +%Y%m%d%H%M%S)
spectool -gf --sourcedir ${SPEC}  || exit 1
mock -r epel-6-x86_64 --buildsrpm --spec=${SPEC} --sources ~/rpmbuild/SOURCES/  || exit 1
BUILD_DIR=${TMPDIR}/${SPEC}/${BUILD_DATE}
mkdir -p ${BUILD_DIR}
rsync -av /var/lib/mock/epel-6-x86_64/result/ $BUILD_DIR 
for SRPM in ${BUILD_DIR}/*.src.rpm ;
do
    echo Building ${SRPM}
    mock -r epel-6-x86_64  rebuild  ${SRPM}  || exit 1
done

